<div align="center">

<img src="https://github.com/Endscape-Coding/EN-OS/blob/main/Images/logofl.png" alt="EN-OS Logo">

# EN-OS

**Современный дистрибутив на базе Arch Linux с рабочим столом KDE Plasma 6.** <br>
***A modern Arch Linux-based distribution featuring the KDE Plasma 6 desktop.***

</div>

<div align="center">

[![Status](https://img.shields.io/badge/Status-Release%201.0-success?style=for-the-badge)](https://github.com/Endscape-Coding/EN-OS/releases)
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

**EN-OS** — это современный, удобный и производительный дистрибутив Linux, построенный на надежном фундаменте Arch Linux. Он поставляется с предварительно настроенной новейшей средой рабочего стола **KDE Plasma 6 на Wayland**, созданной для эстетического удовольствия и максимальной продуктивности прямо "из коробки".

Наша философия — предоставить пользователю готовую к работе систему, избавляя от необходимости долгой настройки и ручной установки драйверов. EN-OS идеально подходит для повседневного использования, разработки, мультимедиа и игр.

>  **Текущий статус:** **`Release 1.0 "Leningrad Region"`** — стабильная релизная версия.

---

### ✨ Особенности

*   **🎯 Готовность к работе:** Все необходимое предустановлено. Система работает сразу после загрузки.
*   **⚙️ Автоматическая оптимизация:**
    *   **Z-RAM:** Автоматически настраивается и используется для увеличения эффективной оперативной памяти.
*   **🎨 Красивый интерфейс:**
    *   **KDE Plasma 6 + Wayland:** Используется новейшая версия с современным протоколом Wayland для лучшей производительности и безопасности.
    *   **Единая красивая тема:** Согласованное оформление для всей системы, включая GRUB с красивой темой и сразу включенным `os-prober`.
*   **🛠️ Удобство обслуживания:**
    *   **Собственный репозиторий:** Быстрый доступ к стабильным пакетам и собственным настройкам EN-OS.
    *   **Графический установщик драйверов:** Умный инструмент с GUI для автоматической установки последних драйверов (включая проприетарные NVIDIA), который подбирает оптимальную версию для вашей видеокарты.
    *   **Графический установщик программ:** Модифицированный Pamac для удобного поиска и установки приложений.
    *   **Надежные обновления:** Система обновлений настроена так, чтобы минимизировать риск поломки.
*   **⚡ Производительность и надежность:**
    *   **Поддержка BTRFS:** Работает с современной файловой системой BTRFS, включая предустановленные утилиты для работы с ней.
    *   **Компактность:** Система оптимизирована и занимает мало места.
*   **🔧 Простая установка:** Красивый и интуитивно понятный установщик Calamares.

---

### 🖼️ Скриншоты

<div align="center">

| Рабочий стол | Меню приложений |
| :---: | :---: |
| ![Desktop](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/desktop.png) | ![Applications](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/apps.png) |

| Установщик драйверов | Установщик Calamares |
| :---: | :---: |
| ![Driver Installer](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/driver.png) | ![Calamares](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/calamares.png) |

</div>

---

### 📥 Установка

#### 1. Скачайте образ
Загрузите версию **EN-OS 1.0 "Leningrad Region"** со страницы [Загрузок](https://endscape-coding.github.io/downloads.html).

#### 2. Запишите образ на USB
Используйте любую программу для записи ISO-образов на USB-накопитель.

*   **Windows:** [Rufus](https://rufus.ie/), [Ventoy](https://www.ventoy.net/).
*   **macOS/Linux:** [Balena Etcher](https://www.balena.io/etcher/), [Ventoy](https://www.ventoy.net/).
*   **Командная строка Linux:**
    ```bash
    # ВНИМАНИЕ: Замените /dev/sdX на ваше устройство (например, /dev/sdb).
    sudo dd if=path/to/en-os.iso of=/dev/sdX bs=4M status=progress oflag=sync
    ```

#### 3. Загрузитесь с USB
Перезагрузите компьютер и выберите ваш USB-накопитель в меню загрузки BIOS/UEFI.

---

### 📀 Скачать

| Версия | Статус | Размер | Ссылка |
| :--- | :--- | :--- | :--- |
| **EN-OS 1.0 "Leningrad Region"** | **Релиз** | ~4.6 GB | [Скачать (SourceForge)](https://sourceforge.net/projects/en-os/) [Скачать (Yandex Disk)](https://disk.yandex.ru/d/b_-O61kvX9HOHQ)|
| **Developer Edition** | 🚧 В разработке | - | *Скоро* |
| **Gaming Edition** | 🚧 В разработке | - | *Скоро* |

---

### 🤝 Сообщество

Присоединяйтесь к нам, чтобы быть в курсе новостей, получать помощь и делиться идеями!

*   **💬 Telegram-канал**: [@Linux_EN_OS](https://t.me/Linux_EN_OS) — Новости и анонсы
*   **👥 Telegram-чат**: [@enos_community](https://t.me/enos_community) — Обсуждения и поддержка
*   **🐛 Баг-репорты**: [@enbugreports](https://t.me/enbugreports) или [GitHub Issues](https://github.com/Endscape-Coding/EN-OS/issues) — Сообщения об ошибках

---

### ❤️ Вклад в проект

EN-OS — это проект с открытым исходным кодом, который создается сообществом. Мы будем рады любой помощи!

*   **Тестирование**: Скачивайте релизы и сообщайте об ошибках.
*   **Разработка**: Предлагайте улучшения кода через Pull Requests на [GitHub](https://github.com/Endscape-Coding/EN-OS).
*   **Документация**: Помогайте улучшать этот README и другую документацию.
*   **Распространение**: Расскажите о нашем проекте друзьям!

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

**EN-OS** is a modern, user-friendly, and powerful Linux distribution built on the solid foundation of Arch Linux. It comes with a pre-configured **KDE Plasma 6 on Wayland** desktop environment, meticulously tuned for an aesthetically pleasing and productive experience right out of the box.

Our philosophy is to provide a system that is ready for immediate use, saving you from lengthy setup processes and manual driver installations. EN-OS is ideal for daily use, development, multimedia, and gaming.

> **Current Status:** **`Release 1.0 "Leningrad Region"`** — stable release version.

---

### ✨ Features

*   **🎯 Ready to Go:** Everything essential is pre-installed. The system works immediately after booting.
*   **⚙️ Automatic Optimization:**
    *   **Z-RAM:** Automatically configured and used to increase effective RAM.
*   **🎨 Beautiful Interface:**
    *   **KDE Plasma 6 + Wayland:** The latest version with modern Wayland protocol for better performance and security.
    *   **Unified Beautiful Theme:** Coherent styling for the entire system, including GRUB with a beautiful theme and `os-prober` enabled by default.
*   **🛠️ Maintenance Convenience:**
    *   **Own Repository:** Fast access to stable packages and EN-OS customizations.
    *   **Graphical Driver Installer:** Smart GUI tool for automatic installation of the latest drivers (including proprietary NVIDIA), which selects the optimal version for your graphics card.
    *   **Graphical Software Installer:** Modified Pamac for convenient application search and installation.
    *   **Reliable Updates:** The update system is configured to minimize the risk of breakage.
*   **⚡ Performance & Reliability:**
    *   **BTRFS Support:** Works with the modern BTRFS filesystem, including pre-installed utilities for managing it.
    *   **Compact:** The system is optimized and takes up little space.
*   **🔧 Easy Installation:** Beautiful and intuitive Calamares installer.

---

### 🖼️ Screenshots

<div align="center">

| Desktop | Application Menu |
| :---: | :---: |
| ![Desktop](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/desktop.png) | ![Applications](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/apps.png) |

| Driver Installer | Calamares Installer |
| :---: | :---: |
| ![Driver Installer](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/driver.png) | ![Calamares](https://github.com/Endscape-Coding/EN-OS/blob/main/Images/calamares.png) |

</div>

---

### 📥 Installation

#### 1. Download the ISO
Download the **EN-OS 1.0 "Leningrad Region"** version from the [SourceForge](https://sourceforge.net/projects/en-os/) page.

#### 2. Create a Bootable USB
Use any preferred software to flash the ISO image to a USB drive.

*   **Windows:** [Rufus](https://rufus.ie/), [Ventoy](https://www.ventoy.net/).
*   **macOS/Linux:** [Balena Etcher](https://www.balena.io/etcher/), [Ventoy](https://www.ventoy.net/).
*   **Linux Command Line:**
    ```bash
    # WARNING: Replace /dev/sdX with your actual device (e.g., /dev/sdb).
    sudo dd if=path/to/en-os.iso of=/dev/sdX bs=4M status=progress oflag=sync
    ```

#### 3. Boot from USB
Reboot your computer and select the USB drive from your BIOS/UEFI boot menu.

---

### 📀 Download

| Version | Status | Size | Link |
| :--- | :--- | :--- | :--- |
| **EN-OS 1.0 "Leningrad Region"** | **Release** | ~4.6 GB | [Download (SourceForge)](https://sourceforge.net/projects/en-os/) [Download (Yandex Disk)](https://disk.yandex.ru/d/b_-O61kvX9HOHQ)|
| **Developer Edition** | 🚧 Under Development | - | *Coming Soon* |
| **Gaming Edition** | 🚧 Under Development | - | *Coming Soon* |

---

### 🤝 Community

Join us to stay updated, get help, and share your ideas!

*   **💬 Telegram Channel**: [@Linux_EN_OS](https://t.me/Linux_EN_OS) — News and announcements
*   **👥 Telegram Chat**: [@enos_community](https://t.me/enos_community) — Discussions and support
*   **🐛 Bug Reports**: [@enbugreports](https://t.me/enbugreports) or [GitHub Issues](https://github.com/Endscape-Coding/EN-OS/issues) — Report bugs here

---

### ❤️ Contributing

EN-OS is an open-source project driven by the community. We welcome all contributions!

*   **Testing**: Download releases and report any bugs you find.
*   **Development**: Suggest code improvements via Pull Requests on [GitHub](https://github.com/Endscape-Coding/EN-OS).
*   **Documentation**: Help us improve this README and other documentation.
*   **Spreading the word**: Tell your friends about our project!

---

### 📝 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

<div align="right">

[⬆ Back to Top](#en-os)

</div>
