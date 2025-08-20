# Явно подключаем глобальные настройки
source /etc/bash.bashrc

# Специфичные для root настройки
PS1='\[\e[31m\]\u@\h \[\e[33m\]\w\[\e[0m\]# '
alias rm='rm -i'
