#!/bin/bash

set -e

if [ -d "/usr/lib/modules" ] && [ -n "$(ls -A /usr/lib/modules 2>/dev/null)" ]; then
    LATEST_KERNEL=$(find /usr/lib/modules -name "vmlinuz" -type f 2>/dev/null | sort -V | tail -n1)
    KERNEL_SOURCE="установленное в системе"
else
    LATEST_KERNEL=$(find /run/archiso/bootmnt/arch/boot/x86_64 -name "vmlinuz-*" -type f 2>/dev/null | sort -V | tail -n1)
    if [ -z "$LATEST_KERNEL" ]; then
        LATEST_KERNEL=$(find /run/archiso/bootmnt -name "vmlinuz-linux" -type f 2>/dev/null | head -n1)
    fi
    KERNEL_SOURCE="из ISO образа"
fi

if [ -z "$LATEST_KERNEL" ]; then
    echo "Ошибка: ядро не найдено" >&2
    exit 1
fi

mkdir -p /etc/linuz
cp "$LATEST_KERNEL" "/boot/vmlinuz-linux"

echo "Скопировано: $LATEST_KERNEL -> /boot/vmlinuz-linux ($KERNEL_SOURCE)"
