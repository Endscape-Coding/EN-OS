#!/usr/bin/env bash
systemctl enable NetworkManager

sudo cp -rf /etc/calamares/newmodules/* /etc/calamares/modules/

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

    # Копирование всех конфигов из /etc/skel в домашнюю директорию root (включая .config)
    echo "Copying configuration files from /etc/skel to /root..."
    if [[ -d /etc/skel ]]; then
        # Копируем скрытые файлы и папки (включая .config)
        shopt -s dotglob
        for item in /etc/skel/*; do
            if [[ -e "$item" ]]; then
                echo "Copying $item to /root/"
                cp -r "$item" /root/
            fi
        done
        shopt -u dotglob

        # Устанавливаем правильные права
        chown -R root:root /root
        find /root -type d -exec chmod 755 {} \;
        find /root -type f -exec chmod 644 {} \;

        # Особые права для исполняемых файлов в .local/bin если они есть
        if [[ -d /root/.local/bin ]]; then
            chmod -R +x /root/.local/bin
        fi
    else
        echo "Warning: /etc/skel directory not found, skipping config copy"
    fi

    sleep 3

    # Добавленные строки для автоматического запуска KDE
    if ! systemctl is-active sddm; then
        echo "Setting up autologin to KDE Plasma..."
        mkdir -p /etc/sddm.conf.d
        echo -e "[Autologin]\nUser=root\nSession=plasma.desktop" > /etc/sddm.conf.d/autologin.conf

        # Добавленная строка для настройки X11
        echo -e "[Daemon]\nDisplayServer=x11\nGreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell" >> /etc/sddm.conf.d/display.conf

        echo "Starting SDDM..."
        systemctl enable sddm
        systemctl start sddm

        # Дополнительная проверка через 5 секунд
        sleep 5
        if ! systemctl is-active sddm; then
            echo "Fallback: Starting Xorg manually..."
            startx
        fi
        sleep 10
        sudo calamares
    fi
fi
