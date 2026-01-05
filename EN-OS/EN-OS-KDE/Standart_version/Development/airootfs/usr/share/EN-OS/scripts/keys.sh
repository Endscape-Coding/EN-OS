#!/bin/bash

echo "🔧 Обновление службы инициализации ключей pacman..."

sudo tee /usr/local/bin/init-pacman-keys.sh > /dev/null << 'EOF'
#!/bin/bash

PIDFILE="/var/run/init-pacman-keys.pid"
LOG_FILE="/var/log/pacman-keys.log"
CONFIG_FILE="/etc/pacman-keys-init.conf"

if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    chmod 644 "$LOG_FILE"
fi

MIN_KEYS=5
NETWORK_TIMEOUT=240
START_DELAY=5
BACKGROUND_REFRESH=yes
LOG_LEVEL=2
CHECK_URLS=("archlinux.org" "google.com" "8.8.8.8")

if [[ -f "$CONFIG_FILE" ]]; then
    source "$CONFIG_FILE"
fi

log() {
    local level=$1
    local message=$2

    if [[ "$level" -le "$LOG_LEVEL" ]]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$LOG_FILE"
    fi
}

check_internet_connection() {
    log 2 "Проверка интернет соединения..."

    if ! ip link show | grep -q "state UP"; then
        log 1 "Нет активных сетевых интерфейсов"
        return 1
    fi

    if ip neigh show | grep -q "REACHABLE"; then
        log 3 "Локальная сеть доступна"
    fi

    local dns_available=0
    for dns in "8.8.8.8" "1.1.1.1" "9.9.9.9"; do
        if ping -c 1 -W 1 "$dns" >/dev/null 2>&1; then
            log 3 "DNS сервер $dns доступен"
            dns_available=1
            break
        fi
    done

    if [[ "$dns_available" -eq 0 ]]; then
        log 2 "Нет доступных DNS серверов, пробуем прямой ping"
    fi

    local services=(
        "http://archlinux.org"
        "https://google.com"
        "https://1.1.1.1"
    )

    for service in "${services[@]}"; do
        if curl -s --max-time 3 --head "$service" >/dev/null 2>&1; then
            log 2 "Сеть доступна через $service"
            return 0
        fi
    done

    # Последняя попытка через ping
    for host in "${CHECK_URLS[@]}"; do
        if ping -c 1 -W 2 "$host" >/dev/null 2>&1; then
            log 2 "Сеть доступна через ping $host"
            return 0
        fi
    done

    log 1 "Интернет соединение недоступно"
    return 1
}

wait_for_internet() {
    local max_attempts=$((NETWORK_TIMEOUT / 5))
    local attempt=1

    log 2 "Ожидание интернет соединения (таймаут: ${NETWORK_TIMEOUT}с)..."

    # Первая быстрая проверка
    if check_internet_connection; then
        log 2 "Интернет уже доступен"
        return 0
    fi

    sleep 3

    while [ $attempt -le $max_attempts ]; do
        log 3 "Попытка $attempt из $max_attempts..."

        if check_internet_connection; then
            log 2 "Интернет соединение установлено (попытка $attempt)"
            return 0
        fi

        local wait_time=$((5 + attempt))
        if [ $wait_time -gt 15 ]; then
            wait_time=15
        fi

        sleep $wait_time
        attempt=$((attempt + 1))
    done

    log 1 "Таймаут ожидания интернета ($NETWORK_TIMEOUT секунд)"

    log_network_status

    return 1
}

log_network_status() {
    log 2 "=== Статус сети ==="
    ip addr show >> "$LOG_FILE" 2>&1
    ip route show >> "$LOG_FILE" 2>&1

    if systemctl is-active NetworkManager >/dev/null 2>&1; then
        log 2 "NetworkManager активен"
        nmcli -t device status >> "$LOG_FILE" 2>&1
    elif systemctl is-active systemd-networkd >/dev/null 2>&1; then
        log 2 "systemd-networkd активен"
        networkctl status >> "$LOG_FILE" 2>&1
    fi

    cat /etc/resolv.conf >> "$LOG_FILE" 2>&1
}

send_notification() {
    local title="$1"
    local message="$2"

    local lang="${LANG%_*}"
    local translated_title="$title"
    local translated_message="$message"

    if [[ "$lang" == "ru" || "$LANG" == ru* ]]; then
        case "$title" in
            "Pacman Keys Fixed")
                translated_title="Ключи Pacman исправлены"
                ;;
            "Pacman Keys Error")
                translated_title="Ошибка ключей Pacman"
                ;;
            "Network Warning")
                translated_title="Предупреждение сети"
                ;;
        esac
        case "$message" in
            "Pacman keys have been successfully restored")
                translated_message="Ключи Pacman были успешно восстановлены"
                ;;
            "Failed to restore pacman keys")
                translated_message="Не удалось восстановить ключи Pacman"
                ;;
            "No internet connection, skipping keys check")
                translated_message="Нет интернет соединения, проверка ключей пропущена"
                ;;
        esac
    fi

    if [[ -n "$DISPLAY" ]]; then
        if command -v notify-send >/dev/null 2>&1; then
            notify-send -i "dialog-information" "$translated_title" "$translated_message" --app-name="Pacman Keys" 2>/dev/null || true
        fi
    fi
}

check_and_fix_keys() {
    log 1 "Начинаем восстановление ключей pacman..."

    log 2 "Инициализация новой базы ключей..."
    if ! pacman-key --init 2>&1 | tee -a "$LOG_FILE"; then
        log 0 "Ошибка инициализации ключей"
        return 1
    fi

    log 2 "Добавление ключей Arch Linux..."
    if ! pacman-key --populate archlinux 2>&1 | tee -a "$LOG_FILE"; then
        log 0 "Ошибка добавления ключей Arch Linux"
        return 1
    fi

    log 1 "Ключи успешно восстановлены"

    send_notification "Pacman Keys Fixed" "Pacman keys have been successfully restored"
    return 0
}



cleanup() {
    [[ -n "$PIDFILE" ]] && rm -f "$PIDFILE"
    exit
}

main() {
    trap cleanup EXIT INT TERM

    if [[ -f "$PIDFILE" ]]; then
        local old_pid
        old_pid=$(cat "$PIDFILE" 2>/dev/null)
        if [[ -n "$old_pid" ]] && kill -0 "$old_pid" 2>/dev/null; then
            log 1 "Процесс уже запущен (PID: $old_pid)"
            exit 0
        else
            rm -f "$PIDFILE"
        fi
    fi

    echo $$ > "$PIDFILE"

    log 2 "Служба инициализации ключей запущена"

    sleep "$START_DELAY"

    if ! wait_for_internet; then
        log 1 "Нет интернет соединения, проверка ключей невозможна"
        send_notification "Network Warning" "No internet connection, skipping keys check"
        exit 0  # Выходим без ошибки
    fi

    local key_status
    check_and_fix_keys
    key_status=$?

    case $key_status in
        0)
            log 2 "Ключи в порядке, завершаем работу"
            ;;
        1)
            log 1 "Требуется обновление ключей"
            {
                log 2 "Обновляем ключи..."
                pacman-key --init
                pacman-key --populate archlinux
                pacman-key --refresh-keys 2>&1 | tee -a "$LOG_FILE"
                log 2 "Обновление завершено"
            } &
            ;;
        2)
            log 1 "Требуется полное восстановление ключей"
            if ! repair_pacman_keys; then
                log 0 "Не удалось восстановить ключи"
                exit 1
            fi
            ;;
    esac

    rm -f "$PIDFILE"
    log 2 "Служба завершила работу успешно"
}

main &
EOF

sudo chmod +x /usr/local/bin/init-pacman-keys.sh

sudo tee /etc/pacman-keys-init.conf > /dev/null << 'EOF'
MIN_KEYS=5

NETWORK_TIMEOUT=240

START_DELAY=10

BACKGROUND_REFRESH=yes

# Уровень логирования:
# 0 - только ошибки
# 1 - предупреждения и ошибки
# 2 - информационные сообщения (рекомендуется)
# 3 - отладочные сообщения
LOG_LEVEL=2
EOF

sudo tee /etc/systemd/system/pacman-keys-init.service > /dev/null << 'EOF'
[Unit]
Description=Pacman Keys Initialization
Description[ru]=Инициализация ключей Pacman
After=network.target
Before=multi-user.target
ConditionPathExists=/usr/bin/pacman-key

ConditionPathExists=|/etc/pacman.d/gnupg

DefaultDependencies=yes

[Service]
Type=oneshot
ExecStart=/usr/local/bin/init-pacman-keys.sh
RemainAfterExit=yes
TimeoutSec=180
Restart=no
Nice=19
IOSchedulingClass=idle
User=root

NoNewPrivileges=yes
PrivateTmp=yes
ProtectHome=yes
ProtectSystem=full

ReadWriteDirectories=/etc/pacman.d/gnupg
ReadWriteDirectories=/var/log

StandardOutput=journal
StandardError=journal
SyslogIdentifier=pacman-keys-init

[Install]
WantedBy=multi-user.target
EOF

sudo mkdir -p /etc/systemd/system/pacman-keys-init.service.wants
sudo ln -sf /lib/systemd/system/network-online.target /etc/systemd/system/pacman-keys-init.service.wants/network-online.target

sudo systemctl daemon-reload
sudo systemctl enable pacman-keys-init.service

echo "✅ Служба обновлена"
echo ""
echo "📋 Дополнительные действия:"
echo ""
echo "1. Проверьте настройки сети:"
echo "   sudo systemctl status NetworkManager"
echo "   или"
echo "   sudo systemctl status systemd-networkd"
echo ""
echo "2. Тестовый запуск:"
echo "   sudo /usr/local/bin/init-pacman-keys.sh"
echo ""
echo "3. Проверка логов в реальном времени:"
echo "   sudo tail -f /var/log/pacman-keys.log"
echo ""
echo "4. Принудительная проверка сети:"
echo "   curl -I https://archlinux.org"
echo "   ping -c 3 8.8.8.8"
echo ""
echo "5. Если сеть долго поднимается, увеличьте NETWORK_TIMEOUT в /etc/pacman-keys-init.conf"
