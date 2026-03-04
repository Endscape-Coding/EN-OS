<div align="center">

<img src="https://github.com/Endscape-Coding/EN-OS/blob/main/Images/logofl.png" alt="EN-OS Utils Logo">

# 🖥️ EN-OS-Utils

**Центральный хаб утилит экосистемы EN-OS** <br>
***Central Hub for EN-OS Ecosystem Utilities***

</div>

<div align="center">

![Rust](https://img.shields.io/badge/Rust-orange?logo=rust)
![Python](https://img.shields.io/badge/Python-yellow?logo=python)
![License](https://img.shields.io/badge/License-AGPL%2F%20GPL-blue)
![Status](https://img.shields.io/badge/Status-Active%20Development-green)

</div>

<p align="center">
  <a href="#-русский">Русский</a> • <a href="#-english">English</a>
</p>

---
## 🇷🇺 Русский

<div align="center">

[О проекте](#-о-проекте) • [Каталог утилит](#-каталог-утилит) • [Безопасность](#-безопасность) • [Вклад в проект](#-вклад-в-проект) • [Статус компонентов](#-статус-компонентов) • [Контакты](#-контакты-и-сообщество)

</div>

### 📋 О проекте

**EN-OS-Utils** — это мета-репозиторий, объединяющий все утилиты и инструменты экосистемы **EN-OS**, современного Linux-дистрибутива на базе Arch Linux. Здесь вы найдёте ссылки на все компоненты системы с кратким описанием их назначения, технологий и текущего статуса.

> 💡 **Совет**: Используйте этот README как навигатор по экосистеме. Каждый репозиторий содержит подробную документацию, инструкции по сборке и использованию.

---

### 🗂️ Каталог утилит

#### 🔧 Системные утилиты

| Репозиторий | Описание | Технологии | Статус |
|-------------|----------|-----------|--------|
| **[EN-OS-System-Manager](https://github.com/Endscape-Coding/EN-OS-System-Manager)** | ✅ **Доступен**. Графический центр управления системой: мониторинг, настройки, управление сервисами и пакетами. | `Tauri` + `Python`/`Go`/`Rust` | 🟢 **Готов к использованию** |
| **[EN-OS-Zram-Manager](https://github.com/Endscape-Coding/EN-OS-Zram-Manager)** | Универсальный менеджер ZRam: настройка алгоритмов сжатия, размера swap, мониторинг использования памяти и CPU. Работает на любых systemd-дистрибутивах. | `Rust` | 🟡 В разработке |
| **[EN-OS-Pacman-Key-Manager](https://github.com/Endscape-Coding/EN-OS-Pacman-Key-Manager)** | Утилита для управления ключами pacman: базовые операции с ключами репозиториев. | `Shell`/`Rust` | 🟡 В разработке |

#### 🌐 Удалённое управление и автоматизация

| Репозиторий | Описание | Технологии | Статус |
|-------------|----------|-----------|--------|
| **[EN-OS-Remote-Assistant](https://github.com/Endscape-Coding/EN-OS-Remote-Assistant)** | 🤖 Telegram-бот для удалённого управления ПК: выполнение команд, скриншоты, управление файлами. Поддержка X11/Wayland, эмуляция ввода через ydotool. | `Rust` + `teloxide` | 🟡 В разработке |
| **[EN-OS-Live-Welcome](https://github.com/Endscape-Coding/EN-OS-Live-Welcome)** | Приветственный GUI для Live-сессий EN-OS: быстрый запуск установки, справка, выбор языковых настроек. | `Tauri` + `HTML`/`JS` | 🟡 В разработке |

#### 🛠️ Сборка и дистрибуция

| Репозиторий | Описание | Технологии | Статус |
|-------------|----------|-----------|--------|
| **[EN-OS-Builds](https://github.com/Endscape-Coding/EN-OS-Builds)** | 📦 **Доступен**. Скрипты и конфигурации для сборки ISO-образов EN-OS: профили сборок, автоматизация, управление версиями. | `Shell` + `Bash`/`Python` | ⚪ **Существует / Используется** |
| **[EN-OS-Calamares](https://github.com/Endscape-Coding/EN-OS-Calamares)** | Кастомизированная конфигурация установщика Calamares для EN-OS: разметка, выбор пакетов, брендинг, пост-установочные скрипты. | `C++` + `Python` + `QML` | ⚪ Существует |
| **[EN-Repository](https://github.com/Endscape-Coding/EN-Repository)** | Конфигурация официального репозитория EN-OS: структура пакетов, управление версиями, зеркалирование. | `pacman` + `repo-add` | ⚪ Активный |

#### 🎨 Интерфейс и персонализация

| Репозиторий | Описание | Технологии | Статус |
|-------------|----------|-----------|--------|
| **[en-os-fastfetch](https://github.com/Endscape-Coding/en-os-fastfetch)** | Кастомная конфигурация fastfetch: логотип EN-OS, цветовая схема, отображение системной информации в терминале. | `JSON`/`Shell` | ⚪ Готов к использованию |

#### 📱 Мобильная совместимость

| Репозиторий | Описание | Технологии | Статус |
|-------------|----------|-----------|--------|
| **[EN-OS-termux](https://github.com/Endscape-Coding/EN-OS-termux)** | Адаптация компонентов EN-OS для запуска в Termux на Android: базовые утилиты, окружение, совместимость. | `Shell` + `Rust` | 🧪 Экспериментальный |

---

### 🔐 Безопасность

- Некоторые утилиты требуют `sudo` и явно запрашивают подтверждение.
- Исходный код открыт: вы можете аудитировать любую утилиту перед использованием.
- На текущем этапе репозиторий не использует GPG-подпись пакетов — мы работаем над внедрением системы верификации в будущих релизах.
- При использовании `Remote-Assistant` (в разработке) обязательно настройте `.env` с `TELOXIDE_TOKEN` и `ID` для ограничения доступа.

---

### 🤝 Вклад в проект

EN-OS — проект с открытым исходным кодом, и мы приветствуем участие сообщества:

1. **Сообщите об ошибке**: [Issues](https://github.com/Endscape-Coding/EN-OS-Programs/issues)
2. **Предложите улучшение**: Обсудите идею в Issue перед PR
3. **Напишите код**: Следуйте [CONTRIBUTING.md](./CONTRIBUTING.md) (скоро)
4. **Протестируйте**: Особенно важны тесты на разном железе и в Live-режиме

#### 📌 Правила для PR
- ✅ Код на Rust должен проходить `cargo clippy` и `cargo fmt`
- ✅ Документация на русском и английском
- ✅ Тесты для новых функций (где применимо)
- ✅ Совместимость с systemd и Arch-based системами

---

### 📊 Статус компонентов

| Компонент | Статус | Доступность | Примечание |
|-----------|--------|-------------|------------|
| System-Manager | 🟢 Готов | ✅ В репозитории | Основной инструмент управления |
| EN-OS-Builds | ⚪ Существует | ✅ В репозитории | Используется для сборки пакетов |
| EN-Repository | ⚪ Активен | ✅ Подключён | Основной источник пакетов |
| en-os-fastfetch | ⚪ Готов | ✅ В репозитории | Косметическое улучшение |
| Zram-Manager | 🟡 В разработке | 🔜 Скоро | Оптимизация памяти |
| Remote-Assistant | 🟡 В разработке | 🔜 Скоро | Удалённое управление |
| Live-Welcome | 🟡 В разработке | 🔜 Скоро | Приветствие в Live-режиме |
| Pacman-Key-Manager | 🟡 В разработке | 🔜 Скоро | Управление ключами |
| EN-OS-Calamares | ⚪ Существует | ✅ В репозитории | Конфигурация установщика |
| EN-OS-termux | 🧪 Эксперимент | 🔬 Тестирование | Android-совместимость |

> 🔄 Все репозитории используют **rolling-release** модель: обновления доступны сразу после тестирования.

---

### 🌍 Поддержка языков

| Утилита | 🇷🇺 Русский | 🇬🇧 English | 🌐 Другие |
|---------|-----------|-----------|----------|
| System-Manager | ✅ | ✅ | В разработке |
| Remote-Assistant | ✅ | ✅ | — |
| Live-Welcome | ✅ | ✅ | В разработке |
| Zram-Manager | ✅ | ✅ | — |
| fastfetch | ✅ | ✅ | Через конфиг |

---

### 📬 Контакты и сообщество

- **Telegram-канал**: [@Linux_EN_OS](https://t.me/Linux_EN_OS)
- **GitHub Issues**: [Сообщить об ошибке](https://github.com/Endscape-Coding/EN-OS-Programs/issues)
- **Email**: endscape.coding@gmail.com
- **Документация**: [Wiki (скоро)](https://github.com/Endscape-Coding/EN-OS-Programs/wiki)

---

### 📄 Лицензии

Большинство утилит распространяются под лицензиями:
- **AGPL-3.0** — для сетевых и удалённых компонентов
- **GPL-3.0** — для GUI и системных утилит

Полный текст лицензий находится в файле `LICENSE` каждого репозитория.

<div align="right">

[⬆ Наверх](#-en-os-utils)

</div>

---
## 🇬🇧 English

<div align="center">

[About](#-about-the-project) • [Utilities Catalog](#-utilities-catalog) • [Security](#-security) • [Contributing](#-contributing) • [Component Status](#-component-status) • [Contacts](#-contacts--community)

</div>

### 📋 About the Project

**EN-OS-Utils** is a meta-repository that unites all utilities and tools of the **EN-OS** ecosystem, a modern Linux distribution based on Arch Linux. Here you will find links to all system components with brief descriptions of their purpose, technologies, and current status.

> 💡 **Tip**: Use this README as a navigator through the ecosystem. Each repository contains detailed documentation, build instructions, and usage guides.

---

### 🗂️ Utilities Catalog

#### 🔧 System Utilities

| Repository | Description | Technologies | Status |
|------------|-------------|--------------|--------|
| **[EN-OS-System-Manager](https://github.com/Endscape-Coding/EN-OS-System-Manager)** | ✅ **Available**. Graphical system control center: monitoring, settings, service and package management. | `Tauri` + `Python`/`Go`/`Rust` | 🟢 **Ready for use** |
| **[EN-OS-Zram-Manager](https://github.com/Endscape-Coding/EN-OS-Zram-Manager)** | Universal ZRam manager: configure compression algorithms, swap size, monitor memory and CPU usage. Works on any systemd-based distribution. | `Rust` | 🟡 In development |
| **[EN-OS-Pacman-Key-Manager](https://github.com/Endscape-Coding/EN-OS-Pacman-Key-Manager)** | Utility for managing pacman keys: basic operations with repository keys. | `Shell`/`Rust` | 🟡 In development |

#### 🌐 Remote Control & Automation

| Repository | Description | Technologies | Status |
|------------|-------------|--------------|--------|
| **[EN-OS-Remote-Assistant](https://github.com/Endscape-Coding/EN-OS-Remote-Assistant)** | 🤖 Telegram bot for remote PC control: command execution, screenshots, file management. Supports X11/Wayland, input emulation via ydotool. | `Rust` + `teloxide` | 🟡 In development |
| **[EN-OS-Live-Welcome](https://github.com/Endscape-Coding/EN-OS-Live-Welcome)** | Welcome GUI for EN-OS Live sessions: quick installer launch, help, language settings selection. | `Tauri` + `HTML`/`JS` | 🟡 In development |

#### 🛠️ Build & Distribution

| Repository | Description | Technologies | Status |
|------------|-------------|--------------|--------|
| **[EN-OS-Builds](https://github.com/Endscape-Coding/EN-OS-Builds)** | 📦 **Available**. Scripts and configurations for building EN-OS ISO images: build profiles, automation, version management. | `Shell` + `Bash`/`Python` | ⚪ **Exists / In use** |
| **[EN-OS-Calamares](https://github.com/Endscape-Coding/EN-OS-Calamares)** | Customized Calamares installer configuration for EN-OS: partitioning, package selection, branding, post-install scripts. | `C++` + `Python` + `QML` | ⚪ Exists |
| **[EN-Repository](https://github.com/Endscape-Coding/EN-Repository)** | Official EN-OS repository configuration: package structure, version management, mirroring. | `pacman` + `repo-add` | ⚪ Active |

#### 🎨 Interface & Personalization

| Repository | Description | Technologies | Status |
|------------|-------------|--------------|--------|
| **[en-os-fastfetch](https://github.com/Endscape-Coding/en-os-fastfetch)** | Custom fastfetch configuration: EN-OS logo, color scheme, system information display in terminal. | `JSON`/`Shell` | ⚪ Ready for use |

#### 📱 Mobile Compatibility

| Repository | Description | Technologies | Status |
|------------|-------------|--------------|--------|
| **[EN-OS-termux](https://github.com/Endscape-Coding/EN-OS-termux)** | Adaptation of EN-OS components for running in Termux on Android: basic utilities, environment, compatibility. | `Shell` + `Rust` | 🧪 Experimental |

---

### 🔐 Security

- Some utilities require `sudo` and explicitly request confirmation.
- Source code is open: you can audit any utility before use.
- At this stage, the repository does not use GPG package signing — we are working on implementing a verification system in future releases.
- When using `Remote-Assistant` (in development), be sure to configure `.env` with `TELOXIDE_TOKEN` and `ID` to restrict access.

---

### 🤝 Contributing

EN-OS is an open-source project, and we welcome community participation:

1. **Report a bug**: [Issues](https://github.com/Endscape-Coding/EN-OS-Programs/issues)
2. **Suggest an improvement**: Discuss your idea in an Issue before submitting a PR
3. **Write code**: Follow [CONTRIBUTING.md](./CONTRIBUTING.md) (coming soon)
4. **Test**: Tests on different hardware and in Live mode are especially valuable

#### 📌 PR Guidelines
- ✅ Rust code must pass `cargo clippy` and `cargo fmt`
- ✅ Documentation in both Russian and English
- ✅ Tests for new features (where applicable)
- ✅ Compatibility with systemd and Arch-based systems

---

### 📊 Component Status

| Component | Status | Availability | Notes |
|-----------|--------|--------------|-------|
| System-Manager | 🟢 Ready | ✅ In repository | Main system management tool |
| EN-OS-Builds | ⚪ Exists | ✅ In repository | Used for building packages |
| EN-Repository | ⚪ Active | ✅ Connected | Main package source |
| en-os-fastfetch | ⚪ Ready | ✅ In repository | Cosmetic enhancement |
| Zram-Manager | 🟡 In development | 🔜 Coming soon | Memory optimization |
| Remote-Assistant | 🟡 In development | 🔜 Coming soon | Remote control |
| Live-Welcome | 🟡 In development | 🔜 Coming soon | Live session welcome screen |
| Pacman-Key-Manager | 🟡 In development | 🔜 Coming soon | Key management |
| EN-OS-Calamares | ⚪ Exists | ✅ In repository | Installer configuration |
| EN-OS-termux | 🧪 Experimental | 🔬 Testing | Android compatibility |

> 🔄 All repositories follow a **rolling-release** model: updates are available immediately after testing.

---

### 🌍 Language Support

| Utility | 🇷🇺 Russian | 🇬🇧 English | 🌐 Others |
|---------|-----------|-----------|----------|
| System-Manager | ✅ | ✅ | In development |
| Remote-Assistant | ✅ | ✅ | — |
| Live-Welcome | ✅ | ✅ | In development |
| Zram-Manager | ✅ | ✅ | — |
| fastfetch | ✅ | ✅ | Via config |

---

### 📬 Contacts & Community

- **Telegram channel**: [@Linux_EN_OS](https://t.me/Linux_EN_OS)
- **GitHub Issues**: [Report a bug](https://github.com/Endscape-Coding/EN-OS-Programs/issues)
- **Email**: endscape.coding@gmail.com
- **Documentation**: [Wiki (coming soon)](https://github.com/Endscape-Coding/EN-OS-Programs/wiki)

---

### 📄 Licenses

Most utilities are distributed under the following licenses:
- **AGPL-3.0** — for network and remote components
- **GPL-3.0** — for GUI and system utilities

Full license texts are located in the `LICENSE` file of each repository.

<div align="right">

[⬆ Back to Top](#-en-os-utils)

</div>

---

> 💬 *«EN-OS — это не просто дистрибутив, это экосистема, где каждая утилита продумана для максимальной гибкости, безопасности и простоты. Добро пожаловать в будущее Linux.»*  
> *"EN-OS is not just a distribution — it's an ecosystem where every utility is designed for maximum flexibility, security, and simplicity. Welcome to the future of Linux."*  
> — Команда EN-OS / The EN-OS Team

⭐ **Поставьте звезду / Star the repo**, если проект вам полезен / if you find this project useful!  
🔁 **Форкните / Fork it**, чтобы предложить улучшения или адаптировать под свои нужды / to suggest improvements or adapt it to your needs.

---

*Последнее обновление / Last updated: Март / March 2026*  
*Совместимо с / Compatible with: Arch Linux, EN-OS, Arch-based distributions*
