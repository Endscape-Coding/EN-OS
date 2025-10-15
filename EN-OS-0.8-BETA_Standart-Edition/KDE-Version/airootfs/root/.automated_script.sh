#!/usr/bin/env bash

export BROWSER_HOMEPAGE="file:///etc/core/home.html"
alias firefox='firefox --new-window $BROWSER_HOMEPAGE'
alias chromium='chromium --homepage=$BROWSER_HOMEPAGE'
#sudo cp /etc/kde_settings.conf /etc/sddm.conf.d/kde_settings.conf
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


    # Создаем конфигурацию для автоматического входа
    echo "Setting up autologin to KDE Plasma..."
    mkdir -p /etc/sddm.conf.d

    # Полная конфигурация автоматического входа
    cat > /etc/sddm.conf.d/autologin.conf << 'EOF'
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
MaximumUid=60000
MinimumUid=1000
EOF

    # Конфигурация дисплея
    cat > /etc/sddm.conf.d/display.conf << 'EOF'
[Wayland]
EnableHiDPI=true

[X11]
EnableHiDPI=true
ServerArguments=-nolisten tcp

[Daemon]
DisplayServer=x11
GreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell
EOF

    # Убедимся, что SDDM включен и запущен
    echo "Starting SDDM service..."
    systemctl enable sddm --now

    # Ждем запуска SDDM
    sleep 5

    # Проверяем статус SDDM и перезапускаем если не активен
    if ! systemctl is-active sddm >/dev/null 2>&1; then
        echo "SDDM not active, restarting..."
        systemctl restart sddm
        sleep 3
    fi

    # Дополнительная проверка через несколько секунд
    sleep 2
    if ! systemctl is-active sddm >/dev/null 2>&1; then
        echo "Warning: SDDM still not active, attempting direct start..."
        # Пытаемся запустить SDDM вручную
        sddm --example-config > /etc/sddm.conf 2>/dev/null || true
        sddm &
        sleep 10
    fi

    # Запускаем Calamares после входа в систему
    sleep 15
    sudo calamares || true

    plasmashell --replace || true
fi
