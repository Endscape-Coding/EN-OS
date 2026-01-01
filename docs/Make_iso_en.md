# How to Build a Custom System?

> [!TIP]
> Language: 🇷🇺 [Русский](Make_iso_ru.md) | 🇺🇸 **English**

#### Before You Begin:
- **Recommended base system:** Arch Linux or derivatives (Manjaro, EndeavourOS, etc.)
- **On Debian, NixOS, or other distros:** Build may fail or produce incorrect results
- **Storage requirements:** Minimum 15 GB free disk space
- **Internet connection:** Stable, high-speed connection recommended
- **System requirements:** Multi-core CPU, 8+ GB RAM for optimal performance
- **Time estimate:** 30-90 minutes depending on your system and internet speed

#### Let's Get Started!

**Step 1: Install Required Packages**
```bash
# On Arch-based systems:
sudo pacman -S archiso git

# Optional but recommended for faster builds:
sudo pacman -S pigz zstd  # Parallel compression tools
```

**Step 2: Clone the Repository**
```bash
git clone https://github.com/Endscape-Coding/EN-OS.git
cd EN-OS
```

**Step 3: Navigate to Your Desired Edition**
```bash
# Choose your interface and edition:
cd build-profiles/EN-OS-KDE-Standard/       # KDE Standard
# OR
cd build-profiles/EN-OS-KDE-Gaming/         # KDE Gaming Edition
# OR
cd build-profiles/EN-OS-XFCE-Standard/      # XFCE Edition (Beta)
```

**Step 4: Customize (Optional)**
Edit configuration files according to your needs:
- `packages.x86_64` – Package list
- `airootfs/` – Root filesystem modifications
- `profiledef.sh` – Build profile settings
- `pacman.conf` – Package manager configuration

> 💡 **Tip:** Use the included `customize_airootfs.sh` script for post-install automation.

**Step 5: Build the ISO**
```bash
# Basic build (outputs to work/out/ in current directory)
sudo mkarchiso -v .

# Custom output directory (recommended for SSD users)
sudo mkarchiso -v -o /path/to/output/directory .

# Advanced: Clean build with parallel compression
sudo rm -rf work/ 2>/dev/null || true
sudo mkarchiso -v -w work -o /path/to/output .
```

**Step 6: Verify and Test**
```bash
# Check ISO integrity
sha256sum EN-OS-*.iso

# Optional: Test in QEMU (install qemu first)
sudo pacman -S qemu-base
qemu-system-x86_64 -cdrom EN-OS-*.iso -m 4G -enable-kvm
```

#### Additional Options:
- **Minimal build** (faster but larger ISO):
  ```bash
  sudo mkarchiso -v -r .
  ```
- **Skip validation** (for testing only):
  ```bash
  sudo mkarchiso -v -s .
  ```

#### Where's My ISO?
- Default location: `work/out/` within your build directory
- Custom location: The path you specified with `-o` flag
- Output naming: `EN-OS-<edition>-<date>-x86_64.iso`

#### Next Steps:
1. **Test** the ISO in a virtual machine (VirtualBox, VMware, QEMU)
2. **Flash** to USB: `sudo dd if=EN-OS.iso of=/dev/sdX bs=4M status=progress`
3. **Report issues** on our [GitHub Issues page](https://github.com/Endscape-Coding/EN-OS/issues)
4. **Contribute** improvements via Pull Requests

#### Troubleshooting:
- **Build fails:** Check internet connection and disk space
- **Missing packages:** Ensure `archiso` is up-to-date
- **Permission errors:** Run with `sudo` and verify user permissions
- **Slow download:** Edit `pacman.conf` to use faster mirrors

> 📚 **For detailed archiso options**, consult the [official Arch Linux documentation](https://wiki.archlinux.org/title/Archiso).

---
**Good luck with your build!** 🚀

> 💬 **Need help?** Join our [Telegram community](https://t.me/Linux_EN_OS) or create a GitHub Issue.
