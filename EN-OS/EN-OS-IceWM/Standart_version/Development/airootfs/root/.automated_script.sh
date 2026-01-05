#!/usr/bin/env bash

export BROWSER_HOMEPAGE="file:///etc/core/home.html"
alias firefox='firefox --new-window $BROWSER_HOMEPAGE'
alias chromium='chromium --homepage=$BROWSER_HOMEPAGE'

# Удаляем autostart файлы (они специфичны для KDE/Plasma)
sudo rm /etc/xdg/autostart/en-system-manager.desktop 2>/dev/null || true
sudo rm /etc/xdg/autostart/grub.desktop 2>/dev/null || true

if grep -q "copytoram" /proc/cmdline || [ -d "/run/archiso/copytoram" ]; then
    AIROOTFS_SOURCE="/run/archiso/copytoram/airootfs.sfs"
else
    AIROOTFS_SOURCE="/run/archiso/bootmnt/arch/x86_64/airootfs.sfs"
fi

cat > /etc/calamares/modules/unpackfs.conf << EOF
---
unpack:
    -   source: "$AIROOTFS_SOURCE"
        sourcefs: "squashfs"
        destination: ""
EOF

echo "Конфигурация unpackfs создана с путем: $AIROOTFS_SOURCE"


if [ -d "/etc/core/" ]; then
    sudo cp -rf /etc/core/* /usr/lib/ 2>/dev/null || true
fi

systemctl enable NetworkManager --now 2>/dev/null || true

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

    echo "Setting up SDDM autologin for iceWM..."

    mkdir -p /etc/sddm.conf.d

    cat > /etc/sddm.conf << 'EOF'
[Autologin]
User=root
Session=icewm-session
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
AutologinSession=icewm-session
AutologinUser=root
EOF

    cat > /etc/sddm.conf.d/autologin.conf << 'EOF'
[Autologin]
User=root
Session=icewm-session
Relogin=true

[Daemon]
AutologinSession=icewm-session
AutologinUser=root
EOF

    if [ ! -f "/usr/share/xsessions/icewm-session.desktop" ]; then
        mkdir -p /usr/share/xsessions
        cat > /usr/share/xsessions/icewm-session.desktop << 'EOF'
[Desktop Entry]
Name=IceWM
Comment=Lightweight window manager
Exec=icewm-session
Type=Application
EOF
    fi

    if ! grep -q "^root:" /etc/passwd; then
        echo "Creating root user entry..."
        echo "root:x:0:0:root:/root:/bin/bash" >> /etc/passwd
    fi

    mkdir -p /root/.icewm

    if [ ! -f "/root/.icewm/preferences" ]; then
        cat > /root/.icewm/preferences << 'EOF'
# Основные настройки iceWM
Theme="metal"
TitleFontName="-*-fixed-medium-r-*-*-13-*-*-*-*-*-*-*"
MenuFontName="-*-fixed-medium-r-*-*-13-*-*-*-*-*-*-*"
StatusFontName="-*-fixed-medium-r-*-*-13-*-*-*-*-*-*-*"
NormalFontName="-*-fixed-medium-r-*-*-13-*-*-*-*-*-*-*"
EOF
    fi

    if [ ! -f "/root/.icewm/menu" ]; then
        cat > /root/.icewm/menu << 'EOF'
prog "Terminal" terminal xterm
prog "Web Browser" web-browser firefox
prog "File Manager" file-manager thunar
separator
prog "Shutdown" system-shutdown systemctl poweroff
prog "Reboot" system-reboot systemctl reboot
separator
menu "Applications" folder {
    prog "Text Editor" text-editor micro
    prog "Image Viewer" image-viewer feh
}
EOF
    fi

    mkdir -p /root/.config
    cp -r /etc/skel/.config/* /root/.config/ 2>/dev/null || true

    if [ ! -d "/root" ]; then
        mkdir -p /root
        chown root:root /root
    fi

    echo "root:000000" | chpasswd 2>/dev/null || true

    if [ ! -d "/usr/share/sddm/themes/breeze" ]; then
        mkdir -p /usr/share/sddm/themes/simple
        cat > /usr/share/sddm/themes/simple/theme.conf << 'EOF'
[General]
background=#1d1f21
fontColor=#c5c8c6
EOF
        sed -i 's/Current=breeze/Current=simple/' /etc/sddm.conf
    fi

    echo "Starting SDDM for iceWM..."

    systemctl enable sddm --now 2>/dev/null || true

    sleep 5

    if ! systemctl is-active sddm >/dev/null 2>&1 && ! pgrep sddm >/dev/null 2>&1; then
        echo "SDDM not starting via systemd, starting directly..."
        sddm &
        sleep 10
    fi
fi
