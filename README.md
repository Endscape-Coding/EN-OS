<div align="center">

<img src="https://img.icons8.com/?size=100&id=123404&format=png&color=6E48AA" alt="EN-OS Logo">

# EN-OS

**Современный дистрибутив на базе Arch Linux с рабочим столом KDE Plasma.** <br>
***A modern Arch Linux-based distribution featuring the KDE Plasma desktop.***

</div>

<div align="center">

[![Status](https://img.shields.io/badge/Status-Beta%200.4-orange?style=for-the-badge)](https://github.com/Endscape-Coding/EN-OS/releases)
[![Arch Based](https://img.shields.io/badge/Based%20On-Arch%20Linux-1793D1?style=for-the-badge&logo=arch-linux)](https://archlinux.org)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-6e48aa?style=for-the-badge&logo=github)](https://github.com/Endscape-Coding/EN-OS)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/Linux_EN_OS)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge)](LICENSE)

</div>

<p align="center">
  <a href="#-русский">Русский</a> • <a href="#-english">English</a>
</p>

---
## 🇷🇺 Русский

<div align="center">

[Особенности](#-особенности) • [Скриншоты](#-скриншоты) • [Установка](#-установка) • [Скачать](#-скачать) • [Сообщество](#-сообщество) • [Вклад-в-проект](#️-вклад-в-проект)

</div>

### 🚀 Что такое EN-OS?

**EN-OS** — это современный, удобный и производительный дистрибутив Linux, построенный на надежном фундаменте Arch Linux. Он поставляется с предварительно настроенной средой рабочего стола **KDE Plasma**, созданной для эстетического удовольствия и максимальной продуктивности прямо "из коробки".

Наша философия — предоставить пользователю готовую к работе систему, избавляя от необходимости долгой настройки и ручной установки драйверов. EN-OS идеально подходит для повседневного использования, разработки, мультимедиа и игр.

>  **Текущий статус:** `Beta 0.8` 

---

### ✨ Особенности

-   **🎯 Готовность к работе:** Все необходимые драйверы, библиотеки и приложения предустановлены. Система работает сразу после загрузки.
-   **🎨 Прекрасный интерфейс:** Элегантная темная тема для KDE Plasma с плавными анимациями и современным дизайном. Больше тем в разработке!
-   **⚡ Высокая производительность:** Оптимизированное ядро и тщательно подобранный набор ПО обеспечивают быструю и отзывчивую работу системы.
-   **🔒 Безопасность:** Построен на базе Arch Linux, что гарантирует регулярные обновления и высокий уровень безопасности.
-   **📦 Продуманный набор ПО:** Включает приложения для офисной работы, мультимедиа, разработки и общения.
-   **🔧 Простая установка:** Интегрирован интуитивно понятный установщик Calamares.

---

### 🖼️ Скриншоты

<div align="center">

| Рабочий стол | Меню приложений |
| :---: | :---: |
| ![Desktop](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/desktop.png?raw=true) | ![Applications](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/apps.png?raw=true) |

| Терминал Konsole | Параметры системы |
| :---: | :---: |
| ![Terminal](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/terminal.png?raw=true) | ![Settings](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/settings.png?raw=true) |

</div>

---

### 📥 Установка

#### 1. Скачайте образ
Загрузите последнюю версию EN-OS со страницы [sourceforge](https://sourceforge.net/projects/en-os/files/EN-OS-0.8-BETA/EN-OS-EN-OS%200.8%20beta2025.09.28-x86_64.iso/download).

#### 2. Запишите образ на USB
Используйте любую программу для записи ISO-образов на USB-накопитель.

-   **Windows:** [Rufus](https://rufus.ie/), [Ventoy](https://www.ventoy.net/).
-   **macOS/Linux:** [Balena Etcher](https://www.balena.io/etcher/), [Ventoy](https://www.ventoy.net/).
-   **Командная строка Linux (продвинутый способ):**
    ```bash
    # ВНИМАНИЕ: Замените /dev/sdX на ваше устройство.
    # Неправильное имя устройства приведет к потере данных!
    # Проверьте имя командой lsblk.
    sudo dd if=path/to/en-os.iso of=/dev/sdX bs=4M status=progress oflag=sync
    ```

#### 3. Загрузитесь с USB
Перезагрузите компьютер и выберите ваш USB-накопитель в меню загрузки BIOS/UEFI.

---

### 📀 Скачать

| Версия                | Статус              | Размер  | Ссылка                                                                                              |
| :-------------------- | :------------------ | :------ | :-------------------------------------------------------------------------------------------------- |
| **Live EN-OS Beta 0.8** | Beta                | ~4.6 GB | [Скачать](https://sourceforge.net/projects/en-os/files/EN-OS-0.8-BETA/EN-OS-EN-OS%200.8%20beta2025.09.28-x86_64.iso/download)           |
| **Developer Edition** | 🚧 В разработке      | -       | *Скоро* |
| **Gaming Edition** | 🚧 В разработке      | -       | *Скоро* |

---

### 🤝 Сообщество

Присоединяйтесь к нам, чтобы быть в курсе новостей, получать помощь и делиться идеями!

-   **💬 Telegram-канал**: [@Linux_EN_OS](https://t.me/Linux_EN_OS) — Новости и анонсы
-   **👥 Telegram-чат**: [@enos_community](https://t.me/enos_community) — Обсуждения и поддержка
-   **🐛 Баг-репорты**: [@enbugreports](https://t.me/enbugreports) или [GitHub Issues](https://github.com/Endscape-Coding/EN-OS/issues) — Сообщения об ошибках

---

### ❤️ Вклад в проект

EN-OS — это проект с открытым исходным кодом, который создается сообществом. Мы будем рады любой помощи!

-   **Тестирование**: Скачивайте бета-версии и сообщайте об ошибках.
-   **Разработка**: Предлагайте улучшения кода через Pull Requests на [GitHub](https://github.com/Endscape-Coding/EN-OS).
-   **Документация**: Помогайте улучшать этот README и другую документацию.
-   **Распространение**: Расскажите о нашем проекте друзьям!

---

### 📝 Лицензия

Этот проект распространяется под лицензией **GNU General Public License v3.0**. Подробнее см. в файле [LICENSE](LICENSE).

<div align="right">

[⬆ Наверх](#en-os)

</div>

---
## 🇬🇧 English

<div align="center">

[Features](#-features-1) • [Screenshots](#-screenshots-1) • [Installation](#-installation-1) • [Download](#-download-1) • [Community](#-community-1) • [Contributing](#️-contributing)

</div>

### 🚀 What is EN-OS?

**EN-OS** is a modern, user-friendly, and powerful Linux distribution built on the solid foundation of Arch Linux. It comes with a pre-configured **KDE Plasma** desktop environment, meticulously tuned for an aesthetically pleasing and productive experience right out of the box.

Our philosophy is to provide a system that is ready for immediate use, saving you from lengthy setup processes and manual driver installations. EN-OS is ideal for daily use, development, multimedia, and gaming.

> **Current Status:** `Beta 0.8`.

---

### ✨ Features

-   **🎯 Ready to Go:** All essential drivers, libraries, and applications are pre-installed. The system works immediately after booting.
-   **🎨 Beautiful Interface:** An elegant dark theme for KDE Plasma with smooth animations and a modern design. More themes are on the way!
-   **⚡ High Performance:** A tuned kernel and a carefully selected software suite ensure a fast and responsive system.
-   **🔒 Secure:** Built on Arch Linux, guaranteeing timely updates and a high level of security.
-   **📦 Curated Software:** Includes a suite of applications for office tasks, multimedia, development, and communication.
-   **🔧 Easy Installation:** Intuitive Calamares installer.

---

### 🖼️ Screenshots

<div align="center">

| Desktop | Application Menu |
| :---: | :---: |
| ![Desktop](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/desktop.png?raw=true) | ![Applications](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/apps.png?raw=true) |

| Konsole Terminal | System Settings |
| :---: | :---: |
| ![Terminal](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/terminal.png?raw=true) | ![Settings](https://github.com/Endscape-Coding/Endscape-Coding.github.io/blob/main/images/settings.png?raw=true) |

</div>

---

### 📥 Installation

#### 1. Download the ISO
Download the latest version of EN-OS from the [Sourceforge](https://sourceforge.net/projects/en-os/files/EN-OS-0.8-BETA/EN-OS-EN-OS%200.8%20beta2025.09.28-x86_64.iso/download) page.

#### 2. Create a Bootable USB
Use any preferred software to flash the ISO image to a USB drive.

-   **Windows:** [Rufus](https://rufus.ie/), [Ventoy](https://www.ventoy.net/).
-   **macOS/Linux:** [Balena Etcher](https://www.balena.io/etcher/), [Ventoy](https://www.ventoy.net/).
-   **Linux Command Line (Advanced):**
    ```bash
    # WARNING: Replace /dev/sdX with your actual device.
    # Using the wrong device name will result in data loss!
    # Double-check with the 'lsblk' command.
    sudo dd if=path/to/en-os.iso of=/dev/sdX bs=4M status=progress oflag=sync
    ```

#### 3. Boot from USB
Reboot your computer and select the USB drive from your BIOS/UEFI boot menu.

---

### 📀 Download

| Version               | Status              | Size    | Link                                                                                                |
| :-------------------- | :------------------ | :------ | :-------------------------------------------------------------------------------------------------- |
| **Live EN-OS Beta 0.8** | Beta                | ~4.6 GB | [Download]([https://drive.google.com/uc?export=download&id=1FuauymjLwglj8ojJOP7AIzIFxinbgnqJ](https://sourceforge.net/projects/en-os/files/EN-OS-0.8-BETA/EN-OS-EN-OS%200.8%20beta2025.09.28-x86_64.iso/download))         |
| **Developer Edition** | 🚧 Under Development | -       | *Coming Soon* |
| **Gaming Edition** | 🚧 Under Development | -       | *Coming Soon* |

---

### 🤝 Community

Join us to stay updated, get help, and share your ideas!

-   **💬 Telegram Channel**: [@Linux_EN_OS](https://t.me/Linux_EN_OS) — News and announcements
-   **👥 Telegram Chat**: [@enos_community](https://t.me/enos_community) — Discussions and support
-   **🐛 Bug Reports**: [@enbugreports](https://t.me/enbugreports) or [GitHub Issues](https://github.com/Endscape-Coding/EN-OS/issues) — Report bugs here

---

### ❤️ Contributing

EN-OS is an open-source project driven by the community. We welcome all contributions!

-   **Testing**: Download beta releases and report any bugs you find.
-   **Development**: Suggest code improvements via Pull Requests on [GitHub](https://github.com/Endscape-Coding/EN-OS).
-   **Documentation**: Help us improve this README and other documentation.
-   **Spreading the word**: Tell your friends about our project!

---

### 📝 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

<div align="right">

[⬆ Back to Top](#en-os)

</div>
