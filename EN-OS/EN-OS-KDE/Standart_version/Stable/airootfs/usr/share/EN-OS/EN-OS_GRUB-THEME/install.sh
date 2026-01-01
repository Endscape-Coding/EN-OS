#!/bin/bash

# Grub2 Theme

ROOT_UID=0
THEME_DIR="/boot/grub/themes"
THEME_NAME=EN-OS

MAX_DELAY=20                                        # max delay for user to enter root password

#COLORS
CDEF=" \033[0m"                                     # default color
CCIN=" \033[0;36m"                                  # info color
CGSC=" \033[0;32m"                                  # success color
CRER=" \033[0;31m"                                  # error color
CWAR=" \033[0;33m"                                  # waring color
b_CDEF=" \033[1;37m"                                # bold default color
b_CCIN=" \033[1;36m"                                # bold info color
b_CGSC=" \033[1;32m"                                # bold success color
b_CRER=" \033[1;31m"                                # bold error color
b_CWAR=" \033[1;33m"                                # bold warning color

# Function to detect available screen resolutions
detect_resolutions() {
  # Try to get available resolutions from the system
  local resolutions=""

  # Method 1: Using efiboot (for UEFI systems)
  if has_command efibootmgr; then
    resolutions=$(efibootmgr -v 2>/dev/null | grep -oP 'Resolution\s+\K[0-9]+x[0-9]+' | head -1)
  fi

  # Method 2: Using kernel mode setting (KMS)
  if [ -z "$resolutions" ] && [ -d /sys/class/graphics ]; then
    for fb in /sys/class/graphics/fb*/modes; do
      if [ -f "$fb" ]; then
        resolutions=$(head -1 "$fb" | cut -d' ' -f1 | tr -d '\n')
        break
      fi
    done
  fi

  # Method 3: Using hwinfo if available
  if [ -z "$resolutions" ] && has_command hwinfo; then
    resolutions=$(hwinfo --framebuffer | grep -oP 'Mode \K[0-9]+x[0-9]+' | sort -r | head -1)
  fi

  # Method 4: Common resolutions as fallback
  if [ -z "$resolutions" ]; then
    resolutions="1920x1080,1600x900,1366x768,1280x720,1024x768,800x600,auto"
  else
    # Add auto to the detected resolution
    resolutions="${resolutions},auto"
  fi

  echo "$resolutions"
}

# echo like ...  with  flag type  and display message  colors
prompt () {
  case ${1} in
    "-s"|"--success")
      echo -e "${b_CGSC}${@/-s/}${CDEF}";;          # print success message
    "-e"|"--error")
      echo -e "${b_CRER}${@/-e/}${CDEF}";;          # print error message
    "-w"|"--warning")
      echo -e "${b_CWAR}${@/-w/}${CDEF}";;          # print warning message
    "-i"|"--info")
      echo -e "${b_CCIN}${@/-i/}${CDEF}";;          # print info message
    *)
    echo -e "$@"
    ;;
  esac
}

# Check command availability
function has_command() {
  command -v $1 > /dev/null
}

# Welcome message
prompt -s "\n\t*************************\n\t*  ${THEME_NAME} - Grub2 Theme  *\n\t*************************"

# Check command avalibility
function has_command() {
  command -v $1 > /dev/null
}

prompt -w "\nChecking for root access...\n"

# Checking for root access and proceed if it is present
if [ "$UID" -eq "$ROOT_UID" ]; then

  # Create themes directory if not exists
  prompt -i "\nChecking for the existence of themes directory...\n"
  [[ -d ${THEME_DIR}/${THEME_NAME} ]] && rm -rf ${THEME_DIR}/${THEME_NAME}
  mkdir -p "${THEME_DIR}/${THEME_NAME}"

  # Copy theme
  prompt -i "\nInstalling ${THEME_NAME} theme...\n"
  cp -a ${THEME_NAME}/* ${THEME_DIR}/${THEME_NAME}

  # Set theme
  prompt -i "\nSetting ${THEME_NAME} as default...\n"

  # Backup grub config
  cp -an /etc/default/grub /etc/default/grub.bak

  # Detect available resolutions
  prompt -i "Detecting available screen resolutions...\n"
  RESOLUTIONS=$(detect_resolutions)
  prompt -s "Detected resolutions: $RESOLUTIONS\n"

  # Remove existing GRUB_GFXMODE and GRUB_GFXPAYLOAD_LINUX settings
  grep "GRUB_GFXMODE=" /etc/default/grub 2>&1 >/dev/null && sed -i '/GRUB_GFXMODE=/d' /etc/default/grub
  grep "GRUB_GFXPAYLOAD_LINUX=" /etc/default/grub 2>&1 >/dev/null && sed -i '/GRUB_GFXPAYLOAD_LINUX=/d' /etc/default/grub
  grep "GRUB_THEME=" /etc/default/grub 2>&1 >/dev/null && sed -i '/GRUB_THEME=/d' /etc/default/grub

  # Add new settings
  echo "GRUB_GFXMODE=\"1600x900\"" >> /etc/default/grub
  echo "GRUB_GFXPAYLOAD_LINUX=\"keep\"" >> /etc/default/grub
  echo "GRUB_THEME=\"${THEME_DIR}/${THEME_NAME}/theme.txt\"" >> /etc/default/grub

  # Update grub config
  prompt -i "Updating grub config with detected resolutions: $RESOLUTIONS\n"
  if has_command update-grub; then
    update-grub
  elif has_command grub-mkconfig; then
    grub-mkconfig -o /boot/grub/grub.cfg
  elif has_command grub2-mkconfig; then
    if has_command zypper; then
      grub2-mkconfig -o /boot/grub2/grub.cfg
    elif has_command dnf; then
      grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
    fi
  fi

  # Success message
  prompt -s "\n\t          *************************************\n\t          *  All done! Theme installed!  *\n\t          *************************************\n"
  prompt -s "GRUB will use the best available resolution for your monitor: $RESOLUTIONS\n"

else

  # Error message
  prompt -e "\n [ Error! ] -> Run me as root "

  # persisted execution of the script as root
  read -p "[ trusted ] specify the root password : " -t${MAX_DELAY} -s
  [[ -n "$REPLY" ]] && {
    sudo -S <<< $REPLY $0
  } || {
    prompt  "\n Operation canceled  Bye"
    exit 1
  }
fi
