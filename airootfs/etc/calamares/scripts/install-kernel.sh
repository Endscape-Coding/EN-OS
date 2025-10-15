#!/bin/bash

set -e

LOG_FILE="/var/log/calamares-extra-kernel.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Функция проверки выбора ядра
check_kernel_choice() {
    local KERNEL_CHOICE=$(cat /tmp/kernel-choice 2>/dev/null || echo "linux")

    if [ "$KERNEL_CHOICE" = "linux" ]; then
        log "Выбрано стандартное ядро - ничего не делаем"
        exit 0
    fi

    echo "$KERNEL_CHOICE"
}

# Функция удаления стандартного ядра
remove_linux_kernel() {
    log "Удаление стандартного ядра linux..."

    # Удаляем пакеты
    if pacman -Q linux >/dev/null 2>&1; then
        log "Удаление пакета linux..."
        pacman -R --noconfirm linux
    fi

    if pacman -Q linux-headers >/dev/null 2>&1; then
        log "Удаление пакета linux-headers..."
        pacman -R --noconfirm linux-headers
    fi

    # Удаляем ядро из /boot
    if [ -f "/boot/vmlinuz-linux" ]; then
        log "Удаление ядра из /boot..."
        rm -f "/boot/vmlinuz-linux"
    fi
}

# Функция установки альтернативного ядра
install_alternative_kernel() {
    local kernel_choice="$1"

    log "Установка ядра: $kernel_choice"

    case "$kernel_choice" in
        "linux-lts")
            pacman -Sy --noconfirm linux-lts linux-lts-headers
            ;;
        "linux-zen")
            pacman -Sy --noconfirm linux-zen linux-zen-headers
            ;;
        "linux-hardened")
            pacman -Sy --noconfirm linux-hardened linux-hardened-headers
            ;;
        *)
            log "Неизвестный выбор ядра: $kernel_choice"
            exit 1
            ;;
    esac
}

# Функция копирования нового ядра в /etc/linuz
copy_new_kernel() {
    log "Поиск установленного ядра..."

    local new_kernel=$(find /usr/lib/modules -name "vmlinuz" -type f 2>/dev/null | sort -V | tail -n1)

    if [ -z "$new_kernel" ]; then
        log "ОШИБКА: Не найдено установленное ядро"
        exit 1
    fi

    log "Найдено ядро: $new_kernel"

    # Копируем в /etc/linuz для unpackfs
    mkdir -p /etc/linuz
    cp "$new_kernel" "/etc/linuz/vmlinuz-linux"

    # Сохраняем информацию о ядре
    local kernel_version=$(basename $(dirname $(dirname "$new_kernel")))
    echo "$kernel_version" > /tmp/installed-kernel-version
    echo "$kernel_choice" > /tmp/installed-kernel-choice

    log "Ядро скопировано в /etc/linuz/vmlinuz-linux"
    log "Версия ядра: $kernel_version"
}

# Основная функция
main() {
    log "=== Установка альтернативного ядра ==="

    # Проверяем выбор ядра
    local KERNEL_CHOICE=$(check_kernel_choice)
    log "Выбрано альтернативное ядро: $KERNEL_CHOICE"

    # Удаляем стандартное ядро
    remove_linux_kernel

    # Устанавливаем новое ядро
    install_alternative_kernel "$KERNEL_CHOICE"

    # Копируем новое ядро
    copy_new_kernel "$KERNEL_CHOICE"

    log "=== Установка альтернативного ядра завершена ==="
}

main "$@"
