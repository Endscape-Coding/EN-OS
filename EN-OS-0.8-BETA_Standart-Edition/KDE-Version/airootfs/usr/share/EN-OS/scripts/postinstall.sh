#!/bin/bash

# EN-OS Postinstall Script
# Универсальный скрипт постустановочной настройки с максимальной обработкой ошибок

# Настройка логирования
LOG_FILE="/var/log/en-os-postinstall.log"
exec > >(tee -a "$LOG_FILE") 2>&1
exec 2> >(tee -a "$LOG_FILE" >&2)

# Функция для логирования
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Функция для отправки уведомлений в KDE с максимальной надежностью
send_notification() {
    local title="$1"
    local message="$2"
    local urgency="${3:-normal}"
    local timeout="${4:-5000}"

    # Несколько попыток определения пользователя
    for attempt in {1..5}; do
        # Разные методы определения пользователя X-сессии
        local xuser=$(who | grep -E '(:0|tty7|tty1)' | awk '{print $1}' | head -n1)
        [ -z "$xuser" ] && xuser=$(ps aux | grep -E '[X]org|[k]win' | awk '{print $1}' | head -n1)
        [ -z "$xuser" ] && xuser=$(ls -l /dev/console | awk '{print $3}')

        if [ -n "$xuser" ]; then
            # Пробуем разные пути к Xauthority
            local xauth_paths=(
                "/home/$xuser/.Xauthority"
                "/run/user/$(id -u "$xuser" 2>/dev/null)/gdm/Xauthority"
                "/var/run/gdm/auth-for-$xuser-*/database"
            )

            for xauth in "${xauth_paths[@]}"; do
                if [ -f "$xauth" ]; then
                    export XAUTHORITY="$xauth"
                    export DISPLAY=:0

                    # Пробуем разные методы отправки уведомлений
                    if command -v kdialog >/dev/null 2>&1; then
                        sudo -u "$xuser" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u "$xuser")/bus" \
                        kdialog --title "$title" --passivepopup "$message" "$timeout" 2>/dev/null && return 0
                    fi

                    if command -v notify-send >/dev/null 2>&1; then
                        sudo -u "$xuser" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u "$xuser")/bus" \
                        notify-send -u "$urgency" -t "$timeout" "$title" "$message" 2>/dev/null && return 0
                    fi
                fi
            done
        fi

        sleep 2
    done

    # Если не удалось отправить через GUI, пишем в лог
    log "Не удалось отправить уведомление: $title - $message"
    return 1
}

# Функция проверки интернета с повторными попытками
check_internet() {
    local max_attempts=3
    log "Проверяем подключение к интернету (попыток: $max_attempts)..."

    for attempt in {1..$max_attempts}; do
        if ping -c 1 -W 5 archlinux.org >/dev/null 2>&1 || \
           ping -c 1 -W 5 google.com >/dev/null 2>&1 || \
           curl -s --connect-timeout 5 ifconfig.me >/dev/null 2>&1; then
            log "Интернет подключение доступно"
            return 0
        fi
        sleep 2
    done

    log "Нет подключения к интернету после $max_attempts попыток"
    send_notification "EN-OS Postinstall" "Отсутствует интернет соединение. Некоторые операции пропущены." "critical" 5000
    return 1
}

# Функция инициализации pacman-key с обработкой ошибок
init_pacman_key() {
    log "Проверяем состояние pacman keyring..."

    # Проверяем, нужно ли инициализировать ключи
    if ! pacman-key --list-keys >/dev/null 2>&1; then
        log "Инициализируем pacman-key..."

        if pacman-key --init 2>> "$LOG_FILE"; then
            log "Pacman-key успешно инициализирован"
        else
            log "Ошибка при инициализации pacman-key"
            return 1
        fi

        log "Добавляем ключи Arch Linux..."
        if pacman-key --populate archlinux 2>> "$LOG_FILE"; then
            log "Ключи Arch Linux успешно добавлены"
        else
            log "Ошибка при добавлении ключей Arch Linux"
            return 1
        fi
    else
        log "Pacman-key уже инициализирован"
    fi

    return 0
}

# Функция добавления репозитория с проверкой
add_en_repository() {
    log "Добавляем EN Repository..."

    # Проверяем, не добавлен ли уже репозиторий
    if grep -q "\[enrepo\]" /etc/pacman.conf; then
        log "Репозиторий enrepo уже существует в pacman.conf"
        return 0
    fi

    # Добавляем репозиторий
    echo -e '\n[enrepo]\nSigLevel = Optional TrustAll\nServer = https://github.com/Endscape-Coding/EN-Repository/raw/main/repo/' >> /etc/pacman.conf

    if grep -q "\[enrepo\]" /etc/pacman.conf; then
        log "Репозиторий enrepo успешно добавлен в pacman.conf"

        # Обновляем базы pacman
        if check_internet; then
            log "Обновляем базы pacman..."
            if pacman -Syy 2>> "$LOG_FILE"; then
                log "Базы pacman успешно обновлены"
            else
                log "Ошибка при обновлении баз pacman"
                return 1
            fi
        fi
    else
        log "Ошибка при добавлении репозитория enrepo"
        return 1
    fi

    return 0
}

# Функция установки GRUB темы с максимальной обработкой ошибок
install_grub_theme() {
    local theme_script="/usr/share/EN-OS/EN-OS_GRUB-THEME/install.sh"
    local max_attempts=3

    log "Проверяем наличие GRUB темы..."

    for attempt in {1..$max_attempts}; do
        if [ -f "$theme_script" ]; then
            log "Найден скрипт установки GRUB темы, attempt $attempt"
            chmod +x "$theme_script"

            if "$theme_script" 2>> "$LOG_FILE"; then
                log "GRUB тема успешно установлена"
                send_notification "EN-OS Postinstall" "GRUB тема успешно установлена" "normal" 3000
                return 0
            else
                log "Ошибка при установке GRUB темы (attempt $attempt)"
                sleep 2
            fi
        else
            log "GRUB тема не найдена: $theme_script (attempt $attempt)"
            sleep 2
        fi
    done

    log "Не удалось установить GRUB тему после $max_attempts попыток"
    send_notification "EN-OS Postinstall" "Ошибка при установке GRUB темы" "critical" 3000
    return 1
}



# Основная функция с обработкой ошибок
main() {
    local error_count=0
    local start_time=$(date +%s)

    log "=== НАЧАЛО ПОСТУСТАНОВОЧНОГО СКРИПТА EN-OS ==="
    send_notification "EN-OS Postinstall" "Запуск постустановочных задач..." "normal" 2000

    # Ждем полной загрузки системы
    log "Ожидаем загрузку системы..."
    sleep 10

    # Выполняем задачи с обработкой ошибок
    tasks=(
        "init_pacman_key"
        "add_en_repository"
        "install_grub_theme"
    )

    for task in "${tasks[@]}"; do
        if ! $task; then
            log "Ошибка в задаче: $task"
            ((error_count++))
        fi
        sleep 1
    done

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))

    log "=== ЗАВЕРШЕНИЕ ПОСТУСТАНОВОЧНЫХ ЗАДАЧ ==="
    log "Выполнено за $duration секунд с $error_count ошибками"

    if [ $error_count -eq 0 ]; then
        send_notification "EN-OS Postinstall" "Постустановочные задачи завершены успешно! Система готова к использованию." "normal" 5000
    else
        send_notification "EN-OS Postinstall" "Постустановочные задачи завершены с $error_count ошибками. Проверьте лог: $LOG_FILE" "critical" 8000
    fi

    # Отключаем службу после выполнения
    log "Отключаем службу postinstall..."
    systemctl disable postinstall.service 2>> "$LOG_FILE"

    echo "Постустановочные задачи завершены. Лог: $LOG_FILE"
    return $error_count
}

# Обработка прерываний и ошибок
trap 'log "Скрипт прерван пользователем"; send_notification "EN-OS Postinstall" "Постустановочные задачи прерваны!" "critical" 5000; exit 1' INT TERM
trap 'log "Ошибка в строке $LINENO"; send_notification "EN-OS Postinstall" "Ошибка в постустановочных задачах!" "critical" 5000' ERR

# Запуск основной функции
main "$@"
exit $?
