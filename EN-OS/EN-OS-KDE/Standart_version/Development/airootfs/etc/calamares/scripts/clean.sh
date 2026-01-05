#!/bin/bash

set -euo pipefail

log() { echo -e "[*] $*"; }
ok()  { echo -e "  ✓ $*"; }
warn(){ echo -e "  ⚠ $*"; }
fail(){ echo -e "  ✗ $*"; exit 1; }

check_root() {
    if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
        fail "Этот скрипт должен выполняться с правами root."
    fi
}

remove_sddm_autologin() {
    log "Удаление автоматического входа SDDM..."
    local sddm_conf="/etc/sddm.conf"
    local sddm_conf_d="/etc/sddm.conf.d"

    if [ -f "$sddm_conf" ]; then
        sed -i '/^User=/d;/^Session=/d;/^Autologin=/d' "$sddm_conf" || true
        ok "Основной конфиг SDDM очищен"
    fi

    if [ -d "$sddm_conf_d" ]; then
        find "$sddm_conf_d" -type f -name "*.conf" -exec sed -i '/Autologin/d;/User=/d' {} + 2>/dev/null || true
        rm -f "$sddm_conf_d/autologin.conf" 2>/dev/null || true
        ok "Конфиги в sddm.conf.d очищены"
    fi

    if [ -f /usr/share/EN-OS/sddm/kde_settings.conf ]; then
        cp -f /usr/share/EN-OS/sddm/kde_settings.conf "$sddm_conf_d"/ || true
        ok "Восстановлены стандартные настройки SDDM"
    fi
}

remove_calamares_autostart() {
    log "Удаление Calamares из автозапуска..."
    rm -rf /etc/calamares /etc/calamares/* 2>/dev/null || true
    rm -f /etc/xdg/autostart/calamares.desktop \
          /etc/skel/.config/autostart/calamares.desktop \
          /root/.config/autostart/calamares.desktop \
          /home/*/.config/autostart/calamares.desktop 2>/dev/null || true
    rm -f /etc/systemd/system/calamares.service \
          /etc/systemd/system/multi-user.target.wants/calamares.service 2>/dev/null || true
    systemctl daemon-reload 2>/dev/null || true
    ok "Calamares успешно удалён из автозапуска"
}

remove_installer_packages() {
    log "Удаление пакетов установщика..."
    pacman -Rdd --noconfirm calamares-git arch-install-scripts 2>/dev/null || true
    ok "Пакеты установщика удалены"
}

clean_temporary_files() {
    log "Очистка временных файлов..."
    command -v paccache >/dev/null 2>&1 && paccache -rk1 2>/dev/null || true
    rm -rf /var/log/calamares /tmp/calamares-* /var/tmp/calamares-* 2>/dev/null || true
    rm -f /root/calamares.log /home/*/calamares.log 2>/dev/null || true
    ok "Временные файлы очищены"
}

clean_history_and_cache() {
    log "Очистка истории и кэша..."
    rm -f /root/.bash_history /home/*/.bash_history 2>/dev/null || true
    rm -rf /root/.cache /home/*/.cache 2>/dev/null || true
    find /home -type f -name "*.log" -delete 2>/dev/null || true
    ok "История и кэш очищены"
}

disable_live_services() {
    log "Отключение live-служб..."
    for s in live-setup.service installer-service.service autostart-calamares.service; do
        systemctl disable "$s" 2>/dev/null || true
    done
    systemctl daemon-reload 2>/dev/null || true
    ok "Live-службы отключены"
}

systemctl_starting() {
    log "Включение основных служб..."
    for s in NetworkManager bluetooth; do
        systemctl enable "$s" 2>/dev/null || true
        systemctl start "$s" 2>/dev/null || true
    done
    chmod +x /usr/share/EN-OS/scripts/postinstall.sh 2>/dev/null || true
    systemctl daemon-reload 2>/dev/null || true
    systemctl enable sddm
    systemctl enable postinstall.service 2>/dev/null || true
    bash /usr/share/EN-OS/scripts/keys.sh 2>/dev/null || true
    ok "Основные службы активированы"
}

plymouth_fix() {
    log "Настройка Plymouth..."
    if command -v plymouth-set-default-theme >/dev/null 2>&1; then
        plymouth-set-default-theme -R en-os || true
        ok "Тема Plymouth установлена"
    else
        warn "Plymouth не установлен, пропускаем"
    fi
}

zram_setup() {
    log()  { echo "[ZRAM] $*"; }
    ok()   { echo "[OK] $*"; }
    warn() { echo "[WARN] $*" >&2; }

    local script_path="/usr/local/bin/zram-setup.sh"
    local service_path="/etc/systemd/system/zram.service"

    log "Настройка ZRAM..."

    cat > "$script_path" <<'EOF'
#!/bin/bash

log()  { echo "[ZRAM] $*"; }
ok()   { echo "[OK] $*"; }
warn() { echo "[WARN] $*" >&2; }

modprobe zram || exit 0

swapoff /dev/zram0 2>/dev/null
[ -e /sys/block/zram0/reset ] && echo 1 > /sys/block/zram0/reset

mem_kb=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
mem_gb=$((mem_kb / 1024 / 1024))

if [ "$mem_gb" -le 8 ]; then
    zram_size=$((mem_gb * 50 / 100))G
elif [ "$mem_gb" -le 16 ]; then
    zram_size=$((mem_gb * 40 / 100))G
else
    zram_size=$((mem_gb * 25 / 100))G
fi

[ "$zram_size" = "0G" ] && zram_size="1G"

echo lz4 > /sys/block/zram0/comp_algorithm 2>/dev/null

echo "$zram_size" > /sys/block/zram0/disksize || exit 0
mkswap /dev/zram0 >/dev/null 2>&1 && \
swapon /dev/zram0 -p 100 && \
ok "ZRAM: $zram_size (lz4)" || \
warn "Ошибка запуска ZRAM"
EOF

    chmod +x "$script_path"

    cat > "$service_path" <<EOF
[Unit]
Description=EN-OS ZRAM auto setup
DefaultDependencies=no
Before=swap.target
Conflicts=shutdown.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/zram-setup.sh
RemainAfterExit=yes
StandardOutput=journal

ExecStartPre=/bin/sh -c "modprobe zram || true"

[Install]
WantedBy=multi-user.target

EOF

    systemctl daemon-reexec
    systemctl daemon-reload
    systemctl enable zram.service
    systemctl start zram.service

    ok "ZRAM включен и добавлен в автозапуск"
}


initramfs_fix() {
    log "Исправление mkinitcpio (удаление archiso)..."
    local conf="/etc/mkinitcpio.conf"
    local preset="/etc/mkinitcpio.d/linux.preset"
    local backup_suffix=".backup.$(date +%Y%m%d_%H%M%S)"

    [ -f "$conf" ] && cp "$conf" "${conf}${backup_suffix}"
    [ -f "$preset" ] && cp "$preset" "${preset}${backup_suffix}"

    if [ -f /etc/mkinitcpio.conf.d/en-os.conf ]; then
        cp /etc/mkinitcpio.conf.d/en-os.conf "$conf"
    fi

    if [ -f /etc/mkinitcpio.conf.d/archiso.conf ]; then
        sed -i 's/\barchiso\b//g; s/\barchiso_[^ ]*\b//g; s/  / /g; s/^ //; s/ $//' /etc/mkinitcpio.conf.d/archiso.conf
    fi

    if command -v mkinitcpio >/dev/null 2>&1; then
        if mkinitcpio -P 2>&1 | tee /tmp/mkinitcpio.log; then
            ok "Initramfs переконфигурирован успешно!"
        else
            warn "Что то не так, чекни /tmp/mkinitcpio.log"
        fi
    else
        warn "mkinitcpio вообще нет"
    fi
}

multilib(){
    sed -i '/^#\[multilib\]/,/^#Include = \/etc\/pacman.d\/mirrorlist/ s/^#//' /etc/pacman.conf
}

main() {
    check_root
    rm -f /root/.automated_script.sh 2>/dev/null || true

    echo "=== Выполняется постустановочная очистка системы ==="

    remove_sddm_autologin
    remove_calamares_autostart
    remove_installer_packages
    initramfs_fix
    systemctl_starting
    plymouth_fix
    zram_setup
    clean_temporary_files
    clean_history_and_cache
    disable_live_services

    echo "=== Очистка завершена успешно! ==="
    echo "Рекомендуется перезагрузить систему для применения изменений."
}

main "$@"
