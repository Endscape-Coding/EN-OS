#!/bin/bash

LOG_FILE="/tmp/en-os-postinstall.log"
exec > >(tee -a "$LOG_FILE") 2>&1
exec 2> >(tee -a "$LOG_FILE" >&2)

detect_language() {
    if [ -n "$LANG" ]; then
        case "$LANG" in
            *ru*|*RU*|*rus*)
                echo "ru"
                ;;
            *)
                echo "en"
                ;;
        esac
    else
        echo "en"
    fi
}

LANG_CODE=$(detect_language)

declare -A messages
messages=(
    ["log_start"]="=== STARTING EN-OS POSTINSTALL SCRIPT ==="
    ["log_start_ru"]="=== НАЧАЛО ПОСТУСТАНОВОЧНОГО СКРИПТА EN-OS ==="

    ["log_wait_system"]="Waiting for system to load..."
    ["log_wait_system_ru"]="Ожидаем загрузку системы..."

    ["log_completion"]="=== COMPLETION OF POSTINSTALLATION TASKS ==="
    ["log_completion_ru"]="=== ЗАВЕРШЕНИЕ ПОСТУСТАНОВОЧНЫХ ЗАДАЧ ==="

    ["log_duration"]="Completed in %d seconds with %d errors"
    ["log_duration_ru"]="Выполнено за %d секунд с %d ошибками"

    ["log_interrupted"]="Script interrupted by user"
    ["log_interrupted_ru"]="Скрипт прерван пользователем"

    ["log_line_error"]="Error on line %s"
    ["log_line_error_ru"]="Ошибка в строке %s"

    ["log_check_internet"]="Checking internet connection..."
    ["log_check_internet_ru"]="Проверяем подключение к интернету..."

    ["log_internet_available"]="Internet connection available"
    ["log_internet_available_ru"]="Интернет подключение доступно"

    ["log_internet_failed"]="No internet connection after %d attempts"
    ["log_internet_failed_ru"]="Нет подключения к интернету после %d попыток"

    ["log_check_pacman_key"]="Checking pacman keyring status..."
    ["log_check_pacman_key_ru"]="Проверяем состояние pacman keyring..."

    ["log_init_pacman_key"]="Initializing pacman-key..."
    ["log_init_pacman_key_ru"]="Инициализируем pacman-key..."

    ["log_pacman_key_success"]="Pacman-key successfully initialized"
    ["log_pacman_key_success_ru"]="Pacman-key успешно инициализирован"

    ["log_pacman_key_error"]="Error initializing pacman-key"
    ["log_pacman_key_error_ru"]="Ошибка при инициализации pacman-key"

    ["log_add_arch_keys"]="Adding Arch Linux keys..."
    ["log_add_arch_keys_ru"]="Добавляем ключи Arch Linux..."

    ["log_arch_keys_success"]="Arch Linux keys successfully added"
    ["log_arch_keys_success_ru"]="Ключи Arch Linux успешно добавлены"

    ["log_arch_keys_error"]="Error adding Arch Linux keys"
    ["log_arch_keys_error_ru"]="Ошибка при добавлении ключей Arch Linux"

    ["log_pacman_key_exists"]="Pacman-key already initialized"
    ["log_pacman_key_exists_ru"]="Pacman-key уже инициализирован"

    ["log_add_en_repo"]="Adding EN Repository..."
    ["log_add_en_repo_ru"]="Добавляем EN Repository..."

    ["log_repo_exists"]="Repository enrepo already exists in pacman.conf"
    ["log_repo_exists_ru"]="Репозиторий enrepo уже существует в pacman.conf"

    ["log_repo_success"]="Repository enrepo successfully added to pacman.conf"
    ["log_repo_success_ru"]="Репозиторий enrepo успешно добавлен в pacman.conf"

    ["log_update_pacman"]="Updating pacman databases..."
    ["log_update_pacman_ru"]="Обновляем базы pacman..."

    ["log_update_success"]="Pacman databases successfully updated"
    ["log_update_success_ru"]="Базы pacman успешно обновлены"

    ["log_update_error"]="Error updating pacman databases"
    ["log_update_error_ru"]="Ошибка при обновлении баз pacman"

    ["log_repo_error"]="Error adding enrepo repository"
    ["log_repo_error_ru"]="Ошибка при добавлении репозитория enrepo"

    ["log_find_grub_theme"]="Searching for GRUB theme..."
    ["log_find_grub_theme_ru"]="Поиск GRUB темы..."

    ["log_grub_script_found"]="Found GRUB theme installation script: %s"
    ["log_grub_script_found_ru"]="Найден скрипт установки GRUB темы: %s"

    ["log_grub_success"]="GRUB theme successfully installed"
    ["log_grub_success_ru"]="GRUB тема успешно установлена"

    ["log_grub_script_error"]="Error executing GRUB theme installation script"
    ["log_grub_script_error_ru"]="Ошибка при выполнении скрипта установки GRUB темы"

    ["log_grub_not_found"]="GRUB theme not found in system"
    ["log_grub_not_found_ru"]="GRUB тема не найдена в системе"

    ["log_detect_de"]="Detected desktop environment: %s"
    ["log_detect_de_ru"]="Обнаружена среда рабочего стола: %s"

    ["log_skip_packages"]="Skipping additional packages installation - no internet"
    ["log_skip_packages_ru"]="Пропускаем установку дополнительных пакетов - нет интернета"

    ["log_install_packages"]="Installing additional packages for %s"
    ["log_install_packages_ru"]="Устанавливаем дополнительные пакеты для %s"

    ["log_package_installed"]="Package %s already installed"
    ["log_package_installed_ru"]="Пакет %s уже установлен"

    ["log_installing_package"]="Installing %s..."
    ["log_installing_package_ru"]="Устанавливаем %s..."

    ["log_package_success"]="Package %s successfully installed"
    ["log_package_success_ru"]="Пакет %s успешно установлен"

    ["log_package_error"]="Error installing %s"
    ["log_package_error_ru"]="Ошибка при установке %s"

    ["log_config_system"]="Configuring system parameters..."
    ["log_config_system_ru"]="Настраиваем системные параметры..."

    ["log_update_desktop_db"]="Updating .desktop file database..."
    ["log_update_desktop_db_ru"]="Обновляем базу данных .desktop файлов..."

    ["log_desktop_db_success"]="Desktop file database updated"
    ["log_desktop_db_success_ru"]="База данных .desktop файлов обновлена"

    ["log_update_icon_cache"]="Updating GTK icon cache..."
    ["log_update_icon_cache_ru"]="Обновляем кеш иконок GTK..."

    ["log_icon_cache_success"]="GTK icon cache updated"
    ["log_icon_cache_success_ru"]="Кеш иконок GTK обновлен"

    ["log_set_permissions"]="Setting correct permissions on home directories..."
    ["log_set_permissions_ru"]="Устанавливаем корректные права на домашние каталоги..."

    ["log_permissions_set"]="Permissions set for %s"
    ["log_permissions_set_ru"]="Права установлены для %s"

    ["log_disable_service"]="Disabling postinstall service..."
    ["log_disable_service_ru"]="Отключаем службу postinstall..."

    ["log_request_root"]="Requesting root privileges via pkexec..."
    ["log_request_root_ru"]="Запрашиваем права root через pkexec..."

    ["log_pkexec_error"]="Error: pkexec not found. Run script with root privileges."
    ["log_pkexec_error_ru"]="Ошибка: pkexec не найден. Запустите скрипт с правами root."

    ["log_notification_failed"]="Failed to send notification: %s - %s"
    ["log_notification_failed_ru"]="Не удалось отправить уведомление: %s - %s"

    ["log_task_error"]="Error in task: %s"
    ["log_task_error_ru"]="Ошибка в задаче: %s"

    ["notify_start"]="Starting postinstallation tasks..."
    ["notify_start_ru"]="Запуск постустановочных задач..."

    ["notify_no_internet"]="No internet connection. Some operations skipped."
    ["notify_no_internet_ru"]="Отсутствует интернет соединение. Некоторые операции пропущены."

    ["notify_grub_success"]="GRUB theme successfully installed"
    ["notify_grub_success_ru"]="GRUB тема успешно установлена"

    ["notify_grub_error"]="Error installing GRUB theme"
    ["notify_grub_error_ru"]="Ошибка при установке GRUB темы"

    ["notify_success"]="Postinstallation tasks completed successfully! System is ready to use."
    ["notify_success_ru"]="Постустановочные задачи завершены успешно! Система готова к использованию."

    ["notify_with_errors"]="Postinstallation tasks completed with %d errors. Check log: %s"
    ["notify_with_errors_ru"]="Постустановочные задачи завершены с %d ошибками. Проверьте лог: %s"

    ["notify_interrupted"]="Postinstallation tasks interrupted!"
    ["notify_interrupted_ru"]="Постустановочные задачи прерваны!"

    ["notify_script_error"]="Error in postinstallation tasks!"
    ["notify_script_error_ru"]="Ошибка в постустановочных задачах!"

    ["notify_root_error"]="EN-OS Postinstall"
    ["notify_root_error_ru"]="EN-OS Postinstall"
)

get_message() {
    local key="$1"
    shift
    local message

    if [ "$LANG_CODE" = "ru" ]; then
        message="${messages[${key}_ru]}"
        [ -z "$message" ] && message="${messages[$key]}"
    else
        message="${messages[$key]}"
    fi

    if [ $# -gt 0 ]; then
        printf "$message" "$@"
    else
        echo "$message"
    fi
}

log() {
    local message
    if [ $# -eq 1 ]; then
        message=$(get_message "$1")
    else
        message=$(get_message "$1" "${@:2}")
    fi
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" | tee -a "$LOG_FILE"
}

get_display_user() {
    local user=""

    user=$(loginctl list-sessions 2>/dev/null | awk '/tty/ || /seat/ {print $3}' | head -n1)
    [ -n "$user" ] && echo "$user" && return 0

    user=$(who | grep -E '(tty[0-9]+|pts)' | awk '{print $1}' | head -n1)
    [ -n "$user" ] && echo "$user" && return 0

    user=$(ps aux | grep -E '[k]win_wayland|[p]lasma' | grep -v root | awk '{print $1}' | head -n1)
    [ -n "$user" ] && echo "$user" && return 0

    [ -n "$USER" ] && echo "$USER" && return 0

    user=$(logname 2>/dev/null)
    [ -n "$user" ] && echo "$user" && return 0

    return 1
}

send_notification() {
    local title=$(get_message "notify_root_error")
    local message_key="$1"
    local urgency="${2:-normal}"
    local timeout="${3:-5000}"
    shift 3

    local message=$(get_message "$message_key" "$@")

    local xuser=$(get_display_user)

    if [ -z "$xuser" ]; then
        log "log_notification_failed" "$title" "$message"
        return 1
    fi

    local user_id=$(id -u "$xuser" 2>/dev/null)
    if [ -z "$user_id" ]; then
        log "log_notification_failed" "$title" "$message"
        return 1
    fi

    local dbus_addr="unix:path=/run/user/$user_id/bus"

    # Проверяем доступность D-Bus
    if [ ! -S "/run/user/$user_id/bus" ]; then
        log "log_notification_failed" "$title" "D-Bus socket not found"
        return 1
    fi

    for attempt in {1..3}; do
        log "Notification attempt $attempt for user $xuser (UID: $user_id)"

        if sudo -u "$xuser" env DBUS_SESSION_BUS_ADDRESS="$dbus_addr" XDG_RUNTIME_DIR="/run/user/$user_id" \
           dbus-send --session --dest=org.freedesktop.Notifications \
           --type=method_call /org/freedesktop/Notifications org.freedesktop.Notifications.Notify \
           "string:$title" "uint32:0" "string:" "string:$message" "array:string:" "dict:string:" "int32:$timeout" 2>> "$LOG_FILE"; then
            log "Notification sent successfully via dbus-send"
            return 0
        fi

        if command -v kdialog >/dev/null 2>&1; then
            if sudo -u "$xuser" env DBUS_SESSION_BUS_ADDRESS="$dbus_addr" XDG_RUNTIME_DIR="/run/user/$user_id" \
               kdialog --title "$title" --passivepopup "$message" "$((timeout/1000))" 2>> "$LOG_FILE"; then
                log "Notification sent successfully via kdialog"
                return 0
            fi
        fi

        if command -v notify-send >/dev/null 2>&1; then
            if sudo -u "$xuser" env DBUS_SESSION_BUS_ADDRESS="$dbus_addr" XDG_RUNTIME_DIR="/run/user/$user_id" \
               notify-send -u "$urgency" -t "$timeout" "$title" "$message" 2>> "$LOG_FILE"; then
                log "Notification sent successfully via notify-send"
                return 0
            fi
        fi

        sleep 2
    done

    log "log_notification_failed" "$title" "$message"
    return 1
}

check_wayland_session() {
    local user="$1"
    local user_id=$(id -u "$user" 2>/dev/null)

    log "Wayland debug - User: $user, UID: $user_id"

    if [ -S "/run/user/$user_id/bus" ]; then
        log "D-Bus socket exists"
    else
        log "D-Bus socket NOT found"
    fi

    log "Active sessions:"
    loginctl list-sessions 2>> "$LOG_FILE" | tee -a "$LOG_FILE"
}

check_internet() {
    local max_attempts=3
    log "log_check_internet"

    for attempt in {1..3}; do
        if ping -c 1 -W 5 archlinux.org >/dev/null 2>&1 || \
           ping -c 1 -W 5 google.com >/dev/null 2>&1 || \
           curl -s --connect-timeout 5 ifconfig.me >/dev/null 2>&1 || \
           wget -q --timeout=5 --spider http://github.com >/dev/null 2>&1; then
            log "log_internet_available"
            return 0
        fi
        sleep 2
    done

    log "log_internet_failed" "$max_attempts"
    send_notification "notify_no_internet" "critical" 5000
    return 1
}

check_root() {
    if [ "$(id -u)" -ne 0 ]; then
        if command -v pkexec >/dev/null 2>&1; then
            log "log_request_root"
            exec pkexec "$0" "$@"
        else
            send_notification "notify_root_error" "critical" 5000
            exit 1
        fi
    fi
}

init_pacman_key() {
    log "log_check_pacman_key"


    log "log_init_pacman_key"

    if pacman-key --init 2>> "$LOG_FILE"; then
        log "log_pacman_key_success"
    else
        log "log_pacman_key_error"
        return 1
    fi

    log "log_add_arch_keys"
    if pacman-key --populate archlinux 2>> "$LOG_FILE"; then
        log "log_arch_keys_success"
    else
        log "log_arch_keys_error"
        return 1
    fi

    systemctl enable NetworkManager

    return 0
}

add_en_repository() {
    log "log_add_en_repo"

    if grep -q "\[enrepo\]" /etc/pacman.conf; then
        log "log_repo_exists"
    else
        echo -e '\n[enrepo]\nSigLevel = Optional TrustAll\nServer = https://github.com/Endscape-Coding/EN-Repository/raw/main/repo/' >> /etc/pacman.conf

        if grep -q "\[enrepo\]" /etc/pacman.conf; then
            log "log_repo_success"
        else
            log "log_repo_error"
            return 1
        fi
    fi


    log "log_enable_multilib"
    sed -i '/^#\[multilib\]/,/^#Include = \/etc\/pacman.d\/mirrorlist/ s/^#//' /etc/pacman.conf 2>> "$LOG_FILE"

    if grep -q "\[multilib\]" /etc/pacman.conf && ! grep -q "^#\[multilib\]" /etc/pacman.conf; then
        log "log_multilib_success"
    else
            log "log_multilib_manual"
        echo -e '\n[multilib]\nInclude = /etc/pacman.d/mirrorlist' >> /etc/pacman.conf
        log "log_multilib_added"
    fi

    if check_internet; then
        log "log_update_pacman"
        if pacman -Syy 2>> "$LOG_FILE"; then
            log "log_update_success"
        else
            log "log_update_error"
            return 1
        fi
    fi

    return 0
}

find_grub_theme() {
    local search_paths=(
        "/etc/Grub2-theme/install.sh"
        "/usr/share/en-os-grub-theme/install.sh"
        "/opt/EN-OS/GRUB-THEME/install.sh"
        "/usr/share/EN-OS/EN-OS_GRUB-THEME/install.sh"
        "/home/*/EN-OS_GRUB-THEME/install.sh"
        "/usr/share/grub/themes/EN-OS/install.sh"
    )

    for path in "${search_paths[@]}"; do
        if [ -f "$path" ]; then
            echo "$path"
            return 0
        fi
    done

    return 1
}

install_grub_theme() {
    log "log_find_grub_theme"

    local theme_script=$(find_grub_theme)

    if [ -n "$theme_script" ]; then
        log "log_grub_script_found" "$theme_script"

        local script_dir=$(dirname "$theme_script")
        local script_name=$(basename "$theme_script")

        if cd "$script_dir" && chmod +x "$script_name"; then
            log "Запуск скрипта установки GRUB темы из директории: $script_dir"

            if ./"$script_name"; then
                log "log_grub_success"
                send_notification "notify_grub_success" "normal" 3000
                cd - > /dev/null
                return 0
            else
                log "log_grub_script_error"
                cd - > /dev/null
            fi
        else
            log "Ошибка при переходе в директорию скрипта: $script_dir"
        fi
    else
        log "log_grub_not_found"
    fi

    send_notification "notify_grub_error" "critical" 3000
    return 1
}

detect_desktop_environment() {
    local de=""

    if [ -n "$XDG_CURRENT_DESKTOP" ]; then
        de="$XDG_CURRENT_DESKTOP"
    elif [ -n "$DESKTOP_SESSION" ]; then
        de="$DESKTOP_SESSION"
    elif ps aux | grep -q "[k]win"; then
        de="KDE"
    elif ps aux | grep -q "[x]fce"; then
        de="XFCE"
    elif ps aux | grep -q "[g]nome-shell"; then
        de="GNOME"
    elif ps aux | grep -q "[c]innamon"; then
        de="CINNAMON"
    elif ps aux | grep -q "[m]ate"; then
        de="MATE"
    fi

    echo "$de" | tr '[:upper:]' '[:lower:]'
}

configure_system() {
    log "log_config_system"

    if command -v update-desktop-database >/dev/null 2>&1; then
        log "log_update_desktop_db"
        update-desktop-database 2>> "$LOG_FILE" && log "log_desktop_db_success"
    fi

    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
        log "log_update_icon_cache"
        gtk-update-icon-cache -t /usr/share/icons/hicolor 2>> "$LOG_FILE" && log "log_icon_cache_success"
    fi

    log "log_set_permissions"
    for user_dir in /home/*; do
        if [ -d "$user_dir" ]; then
            local user=$(basename "$user_dir")
            chown -R "$user:$user" "$user_dir" 2>> "$LOG_FILE" && log "log_permissions_set" "$user"
        fi
    done

    return 0
}

main() {
    local error_count=0
    local start_time=$(date +%s)

    touch "$LOG_FILE"
    chmod 644 "$LOG_FILE"

    check_root "$@"

    sleep 3

    log "log_start"

    local current_user=$(get_display_user)
    log "Detected user: $current_user"

    if [ -n "$current_user" ]; then
        check_wayland_session "$current_user"
    else
        log "Could not detect current user"
    fi

    send_notification "notify_start" "normal" 2000

    sleep 5

    tasks=(
        "add_en_repository"
        "install_grub_theme"
        "configure_system"
    )

    for task in "${tasks[@]}"; do
        if ! $task; then
            log "log_task_error" "$task"
            ((error_count++))
        fi
        sleep 1
    done

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))

    log "log_completion"
    log "log_duration" "$duration" "$error_count"

    if [ $error_count -eq 0 ]; then
        send_notification "notify_success" "normal" 5000
    else
        send_notification "notify_with_errors" "critical" 8000 "$error_count" "$LOG_FILE"
    fi

    if systemctl is-enabled postinstall.service >/dev/null 2>&1; then
        log "log_disable_service"
        systemctl disable postinstall.service 2>> "$LOG_FILE"
    fi

    rm -f /etc/xdg/autostart/postinstall.desktop

    echo "Postinstallation tasks completed. Log: $LOG_FILE"
    return $error_count
}

trap 'log "log_interrupted"; send_notification "notify_interrupted" "critical" 5000; exit 1' INT TERM

main "$@"
exit $?
