#!/usr/bin/env bash

export BROWSER_HOMEPAGE="file:///etc/core/home.html"
alias firefox='firefox --new-window $BROWSER_HOMEPAGE'
alias chromium='chromium --homepage=$BROWSER_HOMEPAGE'
sudo rm /etc/xdg/autostart/en-system-manager.desktop || true
sudo rm /etc/xdg/autostart/grub.desktop
sudo cp -rf /etc/core/* /usr/lib/
sudo cp -f /etc/core/main.xml /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml

systemctl enable NetworkManager
systemctl start NetworkManager

script_cmdline() {
    local param
    for param in $(</proc/cmdline); do
        case "${param}" in
            script=*)
                echo "${param#*=}"
                return 0
                ;;
        esac
    done
}

automated_script() {
    local script rt
    script="$(script_cmdline)"
    if [[ -n "${script}" && ! -x /tmp/startup_script ]]; then
        if [[ "${script}" =~ ^((http|https|ftp|tftp)://) ]]; then
            printf '%s: waiting for network-online.target\n' "$0"
            until systemctl --quiet is-active network-online.target; do
                sleep 1
            done
            printf '%s: downloading %s\n' "$0" "${script}"
            curl "${script}" --location --retry-connrefused --retry 10 --fail -s -o /tmp/startup_script
            rt=$?
        else
            cp "${script}" /tmp/startup_script
            rt=$?
        fi
        if [[ ${rt} -eq 0 ]]; then
            chmod +x /tmp/startup_script
            printf '%s: executing automated script\n' "$0"
            /tmp/startup_script
        fi
    fi
}

if [[ $(tty) == "/dev/tty1" ]]; then
    automated_script
    cp -r /etc/skel/. /root/ 2>/dev/null || true

    echo "Setting up SDDM autologin..."
    mkdir -p /etc/sddm.conf.d

    cat > /etc/sddm.conf << 'EOF'
[Autologin]
User=root
Session=plasma.desktop
Relogin=true

[General]
HaltCommand=/usr/bin/systemctl poweroff
RebootCommand=/usr/bin/systemctl reboot

[Theme]
Current=breeze

[Users]
MaximumUid=65000
MinimumUid=1000

[Wayland]
EnableHiDPI=true

[X11]
EnableHiDPI=true
ServerArguments=-nolisten tcp

[Daemon]
DisplayServer=x11
AutologinSession=plasma.desktop
AutologinUser=root
EOF

    cat > /etc/sddm.conf.d/autologin.conf << 'EOF'
[Autologin]
User=root
Session=plasma.desktop
Relogin=true

[Daemon]
AutologinSession=plasma.desktop
AutologinUser=root
EOF

    if ! grep -q "^root:" /etc/passwd; then
        echo "Creating root user entry..."
        echo "root:x:0:0:root:/root:/bin/bash" >> /etc/passwd
    fi

    mkdir -p /root/.config
    cp -r /etc/skel/.config/* /root/.config/ 2>/dev/null || true

    echo "Checking if root has home directory..."
    if [ ! -d "/root" ]; then
        mkdir -p /root
        chown root:root /root
    fi

    echo "root:000000" | chpasswd 2>/dev/null || true

    echo "Starting SDDM..."
    systemctl enable sddm --now

    sleep 5

    if ! systemctl is-active sddm >/dev/null 2>&1; then
        echo "SDDM not starting via systemd, starting directly..."
        sddm &
        sleep 10
    fi
fi
