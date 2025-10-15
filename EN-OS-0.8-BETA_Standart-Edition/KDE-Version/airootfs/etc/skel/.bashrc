#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

set_light_purple_prompt() {
    local exit_code=$?

    # Светлая пастельная палитра
    LAVENDER='\[\033[38;5;183m\]'      # #d7afff
    LILAC='\[\033[38;5;189m\]'         # #d7d7ff
    PERIWINKLE='\[\033[38;5;147m\]'    # #afafff
    POWDER_BLUE='\[\033[38;5;153m\]'   # #afd7ff
    LIGHT_CYAN='\[\033[38;5;195m\]'    # #d7ffff
    RESET='\[\033[0m\]'

    # Символы
    TOP_CORNER="╭─"
    BOTTOM_CORNER="╰─"
    LAMBDA="λ"

    # Эмодзи статуса
    local status_emoji="💠"
    [ $exit_code -ne 0 ] && status_emoji="⚡"

    # Время выполнения
    local time_display=""
    if [ -n "${CMD_DURATION}" ] && [ "${CMD_DURATION}" -gt 1000 ]; then
        local seconds=$((CMD_DURATION / 1000))
        time_display="${POWDER_BLUE}took ${seconds}s${RESET}"
    fi

    PS1="${TOP_CORNER}${LAVENDER}\u${LILAC}@${PERIWINKLE}\h${RESET} in ${POWDER_BLUE}\w${RESET} ${status_emoji} ${time_display}\n${BOTTOM_CORNER}${LIGHT_CYAN}${LAMBDA}${RESET} "
}

fastfetch --logo /usr/logos/en-os.txt 2>/dev/null --color magenta


PROMPT_COMMAND=set_light_purple_prompt
