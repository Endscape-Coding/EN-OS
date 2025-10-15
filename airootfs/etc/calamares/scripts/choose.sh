#!/bin/bash

# 1. Получаем ID ядра из аргумента, переданного Calamares
SELECTED_KERNEL_ID="$1"

# 2. Файл, куда нужно записать название ядра
OUTPUT_FILE="/tmp/selected_kernel_name.txt"

# 3. Проверка и запись в файл
if [ -z "$SELECTED_KERNEL_ID" ]; then
    echo "ERROR: Kernel ID is empty. Skipping file write."
    exit 1
fi

echo "$SELECTED_KERNEL_ID" > "$OUTPUT_FILE"

# Для отладки (появится в логах Calamares)
echo "Custom Script: Saved kernel ID '$SELECTED_KERNEL_ID' to $OUTPUT_FILE"

# Убедитесь, что скрипт исполняемый:
# chmod +x /usr/local/bin/save-kernel-to-file.sh
