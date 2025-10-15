#!/bin/bash

# Скрипт очистки live системы после установки
# Убирает автоматический вход, удаляет установщик и выполняет дополнительную очистку

set -e  # Завершать выполнение при любой ошибке

echo "=== Начало очистки системы после установки ==="

# Функция для проверки прав root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка: Этот скрипт должен запускаться с правами root" 
        exit 1
    fi
}

# Функция для удаления автоматического входа в SDDM
remove_sddm_autologin() {
    echo "Удаление автоматического входа SDDM..."
    
    local sddm_conf="/etc/sddm.conf"
    local sddm_conf_d="/etc/sddm.conf.d/"
    
    # Удаляем параметры автовхода из основного конфига
    if [ -f "$sddm_conf" ]; then
        sed -i '/^User=/d' "$sddm_conf"
        sed -i '/^Session=/d' "$sddm_conf"
        sed -i '/^Autologin=/d' "$sddm_conf"
        echo "Основной конфиг SDDM очищен"
    fi
    
    # Ищем и очищаем конфиги в conf.d
    if [ -d "$sddm_conf_d" ]; then
        find "$sddm_conf_d" -name "*.conf" -exec sed -i '/Autologin/d' {} \;
        find "$sddm_conf_d" -name "*.conf" -exec sed -i '/User=/d' {} \;
        echo "Конфиги в sddm.conf.d очищены"
    fi
    
    # Дополнительно: удаляем возможные autologin конфиги
    rm -f /etc/sddm.conf.d/autologin.conf 2>/dev/null || true
    cp -f /usr/share/EN-OS/sddm/kde_settings.conf /etc/sddm.conf.d
}

# Функция для удаления Calamares из автозапуска
remove_calamares_autostart() {
    echo "Удаление Calamares из автозапуска..."
    
    # Удаляем desktop-файлы автозапуска
    rm -f /etc/xdg/autostart/calamares.desktop 2>/dev/null || true
    rm -f /home/*/.config/autostart/calamares.desktop 2>/dev/null || true
    rm -f /root/.config/autostart/calamares.desktop 2>/dev/null || true
    
    # Удаляем из различных менеджеров автозапуска
    rm -f /etc/skel/.config/autostart/calamares.desktop 2>/dev/null || true
    
    # Удаляем системные службы автозапуска
    rm -f /etc/systemd/system/calamares.service 2>/dev/null || true
    rm -f /etc/systemd/system/multi-user.target.wants/calamares.service 2>/dev/null || true
    
    # Перезагружаем демон systemd
    systemctl daemon-reload 2>/dev/null || true
}

# Функция для удаления пакетов установщика
remove_installer_packages() {
    echo "Удаление пакетов установщика..."
    
    # Попытка удалить calamares и связанные пакеты
    if command -v pacman &>/dev/null; then
        pacman -Rns --noconfirm calamares 2>/dev/null || true
        pacman -Rns --noconfirm arch-install-scripts 2>/dev/null || true
        pacman -Rns --noconfirm calamares-branding 2>/dev/null || true
    elif command -v apt &>/dev/null; then
        apt remove --purge -y calamares 2>/dev/null || true
    fi
}

# Функция для очистки временных файлов
clean_temporary_files() {
    echo "Очистка временных файлов..."
    
    # Очистка кэша пакетов
    if command -v paccache &>/dev/null; then
        paccache -rk1 2>/dev/null || true
    fi
    
    # Очистка логов установщика
    rm -rf /var/log/calamares/ 2>/dev/null || true
    rm -f /root/calamares.log 2>/dev/null || true
    rm -f /home/*/calamares.log 2>/dev/null || true
    
    # Очистка временных файлов
    rm -rf /tmp/calamares-* 2>/dev/null || true
    rm -rf /var/tmp/calamares-* 2>/dev/null || true
}

# Функция для очистки истории и кэша
clean_history_and_cache() {
    echo "Очистка истории и кэша..."
    
    # Очистка истории bash
    rm -f /root/.bash_history 2>/dev/null || true
    rm -f /home/*/.bash_history 2>/dev/null || true
    
    # Очистка кэша приложений
    rm -rf /root/.cache/ 2>/dev/null || true
    rm -rf /home/*/.cache/ 2>/dev/null || true
    
    # Очистка временных файлов пользователей
    find /home -type f -name "*.log" -delete 2>/dev/null || true
}

# Функция для отключения live-специфичных служб
disable_live_services() {
    echo "Отключение live-специфичных служб..."
    
    # Попытка отключить различные live-службы
    systemctl disable live-setup.service 2>/dev/null || true
    systemctl disable installer-service.service 2>/dev/null || true
    systemctl disable autostart-calamares.service 2>/dev/null || true
    
    # Перезагрузка демона systemd
    systemctl daemon-reload 2>/dev/null || true
}

systemctl_starting(){
    systemctl enable NetworkManager || true
    systemctl start NetworkManager || true
    systemctl enable sddm || true
    systemctl enable bluetooth || true
    systemctl --user enable --now pipewire.service || true
    systemctl --user enable --now pipewire-pulse.service || true
    chmod +x /usr/share/EN-OS/scripts/postinstall.sh || true
    systemctl daemon-reload || true
    systemctl enable postinstall.service || true

}

plymouth(){
    plymouth-set-default-theme -R en-os

}


initramfs(){
    set -e # Exit on any error

    echo "Fixing archiso hooks in mkinitcpio configuration..."

    # Backup original files
    backup_suffix=".backup.$(date +%Y%m%d_%H%M%S)"
    echo "Creating backups:"
    echo "  /etc/mkinitcpio.conf -> /etc/mkinitcpio.conf$backup_suffix"
    echo "  /etc/mkinitcpio.d/linux.preset -> /etc/mkinitcpio.d/linux.preset$backup_suffix"

    cp /etc/mkinitcpio.conf.d/archiso.conf "/etc/mkinitcpio.conf$backup_suffix"
    cp /etc/mkinitcpio.d/linux.preset "/etc/mkinitcpio.d/linux.preset$backup_suffix"
    cp /etc/mkinitcpio.conf.d/en-os.conf /etc/mkinitcpio.conf

    echo "Fixing /etc/mkinitcpio.conf..."
    if [ -f /etc/mkinitcpio.conf.d/archiso.conf ]; then
        # Remove archiso hooks from HOOKS line
        sed -i 's/\barchiso\b//g; s/\barchiso_[^ ]*\b//g; s/  / /g; s/^ //; s/ $//' /etc/mkinitcpio.conf.d/archiso.conf

        # Remove empty parentheses if somehow created
       # sed -i 's/HOOKS=()/HOOKS=(base udev autodetect modconf block filesystems fsck)/' /etc/mkinitcpio.conf
    fi

    # Fix linux.preset
    #echo "Fixing /etc/mkinitcpio.d/linux.preset..."
    #if [ -f /etc/mkinitcpio.d/linux.preset ]; then
    #    # Change default preset from archiso to default
    #   sed -i 's/^PRESET_DEFAULT=archiso/PRESET_DEFAULT=default/' /etc/mkinitcpio.d/linux.preset

    #    # Remove archiso from PRESETS array
    #    sed -i "s/PRESETS=('archiso'/PRESETS=('default'/" /etc/mkinitcpio.d/linux.preset
    #    sed -i "s/PRESETS=('archiso'/PRESETS=('default'/" /etc/mkinitcpio.d/linux.preset
    #    sed -i "s/PRESETS=('default' 'archiso'/PRESETS=('default'/" /etc/mkinitcpio.d/linux.preset
    #    sed -i "s/PRESETS=('archiso' 'default'/PRESETS=('default'/" /etc/mkinitcpio.d/linux.preset

    #fi

    # Rebuild initramfs
    echo "Rebuilding initramfs..."
    if mkinitcpio -P 2>&1 | tee /tmp/mkinitcpio.log; then
        echo "✓ Initramfs rebuilt successfully"

        # Check for warnings (normal) vs errors (bad)
        if grep -q "ERROR" /tmp/mkinitcpio.log; then
            echo "⚠  Errors detected during build:"
            grep "ERROR" /tmp/mkinitcpio.log
        fi

        if grep -q "WARNING" /tmp/mkinitcpio.log; then
            echo "ℹ  Warnings detected (usually safe to ignore):"
            grep "WARNING" /tmp/mkinitcpio.log | head -5
            echo "  (showing first 5 warnings)"
        fi
    else
        echo "✗ Initramfs rebuild failed"
        echo "Check /tmp/mkinitcpio.log for details"
        exit 1
    fi

}

# Основная функция выполнения
main() {
    check_root
    rm -f /root/.automated_script.sh
    
    echo "Выполняется очистка системы..."
    remove_sddm_autologin
    remove_calamares_autostart
    remove_installer_packages
    initramfs
    systemctl_starting
    plymouth
    clean_temporary_files
    clean_history_and_cache
    disable_live_services
    
    echo "=== Очистка завершена успешно! ==="
    echo "Рекомендуется перезагрузить систему для применения изменений."
}

# Запуск основной функции
main "$@"
