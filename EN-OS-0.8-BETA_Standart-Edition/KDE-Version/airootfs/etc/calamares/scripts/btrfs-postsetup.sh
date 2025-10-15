#!/bin/bash

set -e

if mount | grep -q "btrfs.*subvol=@"; then
    echo "Настройка Btrfs..."

    if [ -f /etc/mkinitcpio.conf ]; then
        sed -i 's/^HOOKS=.*/HOOKS=(base udev autodetect modconf block filesystems keyboard fsck)/' /etc/mkinitcpio.conf
        mkinitcpio -P
    fi

    if [ -f /etc/fstab ]; then
        cp /etc/fstab /etc/fstab.backup

        sed -i 's|btrfs.*/|btrfs defaults,noatime,compress=zstd,subvol=@ /|' /etc/fstab
    fi
fi
