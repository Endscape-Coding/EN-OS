#!/bin/bash

# Grub2 Theme with os-prober support

ROOT_UID=0
THEME_DIR="/boot/grub/themes"
THEME_NAME="EN-OS"
CONFIG_FILE="/etc/default/grub"
BACKUP_FILE="${CONFIG_FILE}.bak.$(date +%Y%m%d_%H%M%S)"

MAX_DELAY=20                                        # max delay for user to enter root password

# COLORS
CDEF=" \033[0m"                                     # default color
CCIN=" \033[0;36m"                                  # info color
CGSC=" \033[0;32m"                                  # success color
CRER=" \033[0;31m"                                  # error color
CWAR=" \033[0;33m"                                  # warning color
b_CDEF=" \033[1;37m"                                # bold default color
b_CCIN=" \033[1;36m"                                # bold info color
b_CGSC=" \033[1;32m"                                # bold success color
b_CRER=" \033[1;31m"                                # bold error color
b_CWAR=" \033[1;33m"                                # bold warning color

# Function to print messages with colors
prompt() {
  case ${1} in
    "-s"|"--success")
      echo -e "${b_CGSC}${@/-s/}${CDEF}";;
    "-e"|"--error")
      echo -e "${b_CRER}${@/-e/}${CDEF}";;
    "-w"|"--warning")
      echo -e "${b_CWAR}${@/-w/}${CDEF}";;
    "-i"|"--info")
      echo -e "${b_CCIN}${@/-i/}${CDEF}";;
    *)
      echo -e "$@"
    ;;
  esac
}

# Check command availability
has_command() {
  command -v "$1" > /dev/null 2>&1
}

# Detect available screen resolutions
detect_resolutions() {
  local resolutions=""
  local detected_resolutions=()

  # Method 1: Using efiboot (for UEFI systems)
  if has_command efibootmgr; then
    detected_resolutions+=($(efibootmgr -v 2>/dev/null | grep -oP 'Resolution\s+\K[0-9]+x[0-9]+' | head -1))
  fi

  # Method 2: Using kernel mode setting (KMS)
  if [ -d /sys/class/graphics ]; then
    for fb in /sys/class/graphics/fb*/modes; do
      if [ -f "$fb" ]; then
        detected_resolutions+=($(head -1 "$fb" | cut -d' ' -f1 | tr -d '\n'))
      fi
    done
  fi

  # Method 3: Using hwinfo if available
  if has_command hwinfo; then
    detected_resolutions+=($(hwinfo --framebuffer 2>/dev/null | grep -oP 'Mode \K[0-9]+x[0-9]+' | sort -r | head -1))
  fi

  # Remove duplicates and empty entries
  if [ ${#detected_resolutions[@]} -gt 0 ]; then
    resolutions=$(printf "%s\n" "${detected_resolutions[@]}" | sort -u | tr '\n' ',')
    resolutions="${resolutions%,}" # Remove trailing comma
  fi

  # Common resolutions as fallback
  if [ -z "$resolutions" ]; then
    resolutions="1920x1080,1600x900,1366x768,1280x720,1024x768,800x600"
  fi

  # Add auto option
  resolutions="${resolutions},auto"

  echo "$resolutions"
}

# Backup configuration file
backup_config() {
  prompt -i "Creating backup of ${CONFIG_FILE}...\n"
  cp -an "${CONFIG_FILE}" "${BACKUP_FILE}"
  prompt -s "Backup created: ${BACKUP_FILE}\n"
}

# Enable os-prober
enable_os_prober() {
  prompt -i "Configuring os-prober...\n"

  # Check if os-prober is installed
  if ! has_command os-prober; then
    prompt -w "os-prober not found. Installing...\n"
    if has_command pacman; then
      pacman -S --noconfirm os-prober
    elif has_command apt; then
      apt install -y os-prober
    elif has_command dnf; then
      dnf install -y os-prober
    elif has_command yum; then
      yum install -y os-prober
    fi
  fi

  # Enable os-prober in grub config
  if grep -q "GRUB_DISABLE_OS_PROBER=" "${CONFIG_FILE}"; then
    sed -i 's/GRUB_DISABLE_OS_PROBER=.*/GRUB_DISABLE_OS_PROBER=false/' "${CONFIG_FILE}"
  else
    echo "GRUB_DISABLE_OS_PROBER=false" >> "${CONFIG_FILE}"
  fi

  # Run os-prober to detect other OS
  prompt -i "Running os-prober to detect other operating systems...\n"
  if os_prober_output=$(os-prober 2>/dev/null); then
    if [ -n "$os_prober_output" ]; then
      prompt -s "Detected operating systems:\n"
      echo "$os_prober_output"
    else
      prompt -w "No other operating systems detected.\n"
    fi
  else
    prompt -w "os-prober encountered issues (may be normal if no other OS found).\n"
  fi
}

# Update grub configuration
update_grub_config() {
  prompt -i "Updating GRUB configuration...\n"

  local update_success=false

  if has_command update-grub; then
    if update-grub; then
      update_success=true
    fi
  elif has_command grub-mkconfig; then
    if grub-mkconfig -o /boot/grub/grub.cfg; then
      update_success=true
    fi
  elif has_command grub2-mkconfig; then
    if has_command zypper; then
      if grub2-mkconfig -o /boot/grub2/grub.cfg; then
        update_success=true
      fi
    elif has_command dnf; then
      if grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg; then
        update_success=true
      fi
    fi
  fi

  if [ "$update_success" = true ]; then
    prompt -s "GRUB configuration updated successfully!\n"
  else
    prompt -e "Failed to update GRUB configuration. Please check manually.\n"
    return 1
  fi
}

# Main installation function
install_theme() {
  prompt -s "\n\t*************************\n\t*  ${THEME_NAME} - Grub2 Theme  *\n\t*************************\n"

  # Create themes directory if not exists
  prompt -i "Checking for the existence of themes directory...\n"
  if [ -d "${THEME_DIR}/${THEME_NAME}" ]; then
    prompt -w "Removing existing theme directory...\n"
    rm -rf "${THEME_DIR}/${THEME_NAME}"
  fi
  mkdir -p "${THEME_DIR}/${THEME_NAME}"

  # Copy theme
  prompt -i "Installing ${THEME_NAME} theme...\n"
  if ! cp -a "${THEME_NAME}"/* "${THEME_DIR}/${THEME_NAME}"/; then
    prompt -e "Failed to copy theme files!\n"
    return 1
  fi

  # Backup config
  backup_config

  # Detect available resolutions
  prompt -i "Detecting available screen resolutions...\n"
  local resolutions
  resolutions=$(detect_resolutions)
  prompt -s "Available resolutions: $resolutions\n"

  # Remove existing settings
  sed -i '/^GRUB_GFXMODE=/d' "${CONFIG_FILE}"
  sed -i '/^GRUB_GFXPAYLOAD_LINUX=/d' "${CONFIG_FILE}"
  sed -i '/^GRUB_THEME=/d' "${CONFIG_FILE}"
  sed -i '/^GRUB_DISABLE_OS_PROBER=/d' "${CONFIG_FILE}"

  # Add new settings
  echo "GRUB_GFXMODE=\"auto\"" >> "${CONFIG_FILE}"
  echo "GRUB_GFXPAYLOAD_LINUX=\"keep\"" >> "${CONFIG_FILE}"
  echo "GRUB_THEME=\"${THEME_DIR}/${THEME_NAME}/theme.txt\"" >> "${CONFIG_FILE}"

  # Enable os-prober
  enable_os_prober

  # Update grub config
  if ! update_grub_config; then
    return 1
  fi

  prompt -s "\n\t          ********************************************\n\t          *  Theme installed successfully!  *\n\t          ********************************************\n"
  prompt -s "GRUB will use the best available resolution for your monitor\n"
  prompt -s "os-prober has been enabled to detect other operating systems\n"
  prompt -s "Backup of original config: ${BACKUP_FILE}\n"
}

# Check for root access
check_root() {
  prompt -w "\nChecking for root access...\n"
  if [ "$UID" -eq "$ROOT_UID" ]; then
    install_theme
  else
    prompt -e "\n[ Error! ] -> Run me as root\n"
    read -p "[ trusted ] specify the root password : " -t${MAX_DELAY} -s
    if [[ -n "$REPLY" ]]; then
      if ! sudo -S <<< "$REPLY" "$0"; then
        prompt -e "Authentication failed or command execution error\n"
        exit 1
      fi
    else
      prompt -w "\nOperation canceled. Bye!\n"
      exit 1
    fi
  fi
}

# Main execution
check_root

exit 0
