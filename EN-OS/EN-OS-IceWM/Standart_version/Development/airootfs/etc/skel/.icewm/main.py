#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import traceback
import locale
import time
from pathlib import Path
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QFrame,
                             QMessageBox, QComboBox, QDialog, QGridLayout,
                             QLineEdit, QSpinBox, QCheckBox, QFileDialog,
                             QListWidget, QListWidgetItem, QSplitter, QGroupBox)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, pyqtProperty, QTimer, QMimeData
from PyQt6.QtGui import (QIcon, QFont, QPalette, QColor, QLinearGradient,
                         QPainter, QPixmap, QFontDatabase, QImage, QImageReader,
                         QDragEnterEvent, QDropEvent)
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QListWidget, QListWidgetItem,
    QGroupBox, QGridLayout, QCheckBox, QMessageBox, QDialog,
    QSlider
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from datetime import datetime, timedelta
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from datetime import datetime, timedelta

from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from PyQt6.QtWidgets import QSlider, QDialog, QLineEdit, QDialogButtonBox
from PyQt6.QtGui import QIntValidator

from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from PyQt6.QtWidgets import QSlider, QDialog, QLineEdit, QDialogButtonBox
from PyQt6.QtGui import QIntValidator

from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from PyQt6.QtWidgets import QSlider, QDialog, QLineEdit, QDialogButtonBox
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from datetime import datetime, timedelta


os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-root'

LOCALES = {
    'en': {
        'app_title': 'EN-OS Settings',
        'header': 'EN-OS Settings',
        'display_settings': 'Display Settings',
        'display_desc': 'Adjust screen resolution and manage multiple monitors',
        'wallpaper_settings': 'Wallpaper',
        'wallpaper_desc': 'Choose and set your favorite desktop background',
        'mouse_touchpad': 'Mouse & Touchpad',
        'mouse_touchpad_desc': 'Customize cursor speed and touchpad gestures',
        'theme_settings': 'Themes',
        'theme_desc': 'Pick a beautiful theme for IceWM',
        'footer': 'EN-OS · Made with care ❤️',
        'language': 'Language',
        'error_title': 'Error',
        'error_launch': 'Failed to execute command: {}',
        'error_file_not_found': 'File not found: {}',
        'error_permission': 'Permission denied: {}',
        'error_unknown': 'Unknown error: {}',
        'close': 'Close',
        'apply': 'Apply',
        'cancel': 'Cancel',
        'ok': 'OK',
        'select_wallpaper': 'Select Wallpaper',
        'wallpaper_applied': 'Wallpaper applied successfully',
        'error_wallpaper': 'Failed to apply wallpaper',
        'mouse_speed': 'Cursor Speed',
        'mouse_accel': 'Mouse Acceleration',
        'tap_to_click': 'Tap to Click',
        'no_touchpad': 'No touchpad detected',
        'touchpad_detected': 'Touchpad detected',
        'resolution': 'Resolution',
        'refresh_rate': 'Refresh Rate',
        'primary_display': 'Make primary display',
        'detect_displays': 'Detect Displays',
        'theme_select': 'Select Theme',
        'theme_applied': 'Theme applied successfully',
        'error_theme': 'Failed to apply theme',
        'current_settings': 'Current Settings',
        'set_new_wallpaper': 'Set New Wallpaper',
        'wallpaper_path': 'Wallpaper File',
        'select_wallpaper_placeholder': 'Select wallpaper file…',
        'wallpaper_mode': 'Display Mode',
        'browse': 'Browse…',
        'preview': 'Preview',
        'current_wallpaper': 'Current Wallpaper',
        'no_wallpaper_set': 'No wallpaper set',
        'remove_wallpaper': 'Remove Wallpaper',
        'invalid_path': 'Invalid file path',
        'preview_applied': 'Preview applied',
        'error_preview': 'Error applying preview',
        'select_wallpaper_first': 'Please select a wallpaper first',
        'file_not_found': 'File not found',
        'confirm_remove_wallpaper': 'Are you sure you want to remove the wallpaper?',
        'wallpaper_removed': 'Wallpaper removed successfully',
        'error_remove_wallpaper': 'Failed to remove wallpaper',
        'wallpaper_settings_adjust': 'Current Wallpaper Settings',
        'update_settings': 'Update Settings',
        'wallpaper_preview': 'Wallpaper Preview',
        'preview_wallpaper_placeholder': 'Drag & drop or select an image',
        'selected_wallpaper': 'Selected Wallpaper',
        'path': 'Path',
        'size': 'Size',
        'mode': 'Mode',
        'preview_note': 'This is just a preview — click "Apply" to set the wallpaper',
        'no_wallpaper_preview': 'No wallpaper selected',
        'invalid_image': 'Unsupported image format',
        'load_error': 'Failed to load image',
        'settings_updated': 'Settings updated successfully',
        'settings_applied': 'Settings applied successfully',
        'confirm': 'Confirm',
        'error_apply': 'Error applying settings',
        'drag_drop_here': 'Drag & drop image here',
        'or_click_browse': 'or click Browse',
        'drag_drop_hint': 'You can drag and drop image files from your file manager',
        'browse_tooltip': 'Browse for image files',
        'file_dropped': 'File dropped',
        'file_dropped_success': 'Image file dropped successfully',
        'overclock_mode': 'Overclock Mode',
        'custom_rate': 'Custom Refresh Rate',
        'auto_detect': 'Auto Detect',
        'display_info': 'Display Information',
        'confirm_settings': 'Confirm Settings',
        'revert_timer': 'Revert Countdown',
        'redshift_settings': 'Night Light Settings',
        'enable_redshift': 'Enable Night Light',
        'color_temperature': 'Color Temperature',
        'temperature_presets': 'Temperature Presets',
        'auto_mode': 'Automatic Mode',
        'enable_auto_mode': 'Enable automatic adjustment',
        'location': 'Location',
        'latitude_placeholder': 'Latitude',
        'longitude_placeholder': 'Longitude',
        'detect_location': 'Detect Location',
        'stop_redshift': 'Stop Night Light',
        'redshift_running': 'Night Light is active',
        'redshift_stopped': 'Night Light is stopped',
        'redshift_disabled': 'Night Light disabled',
        'redshift_applied': 'Night Light settings applied successfully',
        'error_redshift': 'Failed to apply Night Light settings',
        'redshift_not_installed': 'Redshift is not installed',
        'keyboard_settings': 'Keyboard Settings',
        'keyboard_layouts': 'Keyboard Layouts',
        'primary_layout': 'Primary Layout',
        'additional_layouts': 'Additional Layouts',
        'add_layout': 'Add Layout',
        'remove_layout': 'Remove',
        'switch_shortcut': 'Switch Layout Shortcut',
        'keybindings': 'Keybindings',
        'shortcut': 'Shortcut',
        'command': 'Command',
        'add': 'Add',
        'edit': 'Edit',
        'remove': 'Remove',
        'apply_layouts': 'Apply Layouts',
        'apply_keybindings': 'Apply Keybindings',
    },

    'ru': {
        'app_title': 'Настройки EN-OS',
        'header': 'Настройки EN-OS',
        'display_settings': 'Настройки дисплея',
        'display_desc': 'Изменение разрешения экрана и работа с несколькими мониторами',
        'wallpaper_settings': 'Обои рабочего стола',
        'wallpaper_desc': 'Выбор и установка красивых обоев',
        'mouse_touchpad': 'Мышь и тачпад',
        'mouse_touchpad_desc': 'Настройка скорости курсора и жестов тачпада',
        'theme_settings': 'Темы оформления',
        'theme_desc': 'Выбор и применение стильных тем IceWM',
        'footer': 'EN-OS · Создано с заботой о вас ❤️',
        'language': 'Язык',
        'error_title': 'Ошибка',
        'error_launch': 'Не удалось запустить команду: {}',
        'error_file_not_found': 'Файл не найден: {}',
        'error_permission': 'Нет прав доступа: {}',
        'error_unknown': 'Неизвестная ошибка: {}',
        'close': 'Закрыть',
        'apply': 'Применить',
        'cancel': 'Отмена',
        'ok': 'ОК',
        'select_wallpaper': 'Выбрать обои',
        'wallpaper_applied': 'Обои успешно установлены',
        'error_wallpaper': 'Не удалось установить обои',
        'mouse_speed': 'Скорость курсора',
        'mouse_accel': 'Ускорение мыши',
        'tap_to_click': 'Нажатие касанием (Tap-to-click)',
        'no_touchpad': 'Тачпад не обнаружен',
        'touchpad_detected': 'Тачпад обнаружен',
        'resolution': 'Разрешение',
        'refresh_rate': 'Частота обновления',
        'primary_display': 'Сделать основным',
        'detect_displays': 'Обнаружить дисплеи',
        'theme_select': 'Выберите тему',
        'theme_applied': 'Тема успешно применена',
        'error_theme': 'Не удалось применить тему',
        'current_settings': 'Текущие настройки',
        'set_new_wallpaper': 'Установить новые обои',
        'wallpaper_path': 'Путь к файлу',
        'select_wallpaper_placeholder': 'Выберите файл обоев…',
        'wallpaper_mode': 'Режим отображения',
        'browse': 'Обзор…',
        'preview': 'Предпросмотр',
        'current_wallpaper': 'Текущие обои',
        'no_wallpaper_set': 'Обои не установлены',
        'remove_wallpaper': 'Удалить обои',
        'invalid_path': 'Неверный путь к файлу',
        'preview_applied': 'Предпросмотр применён',
        'error_preview': 'Ошибка при предпросмотре',
        'select_wallpaper_first': 'Сначала выберите обои',
        'file_not_found': 'Файл не найден',
        'confirm_remove_wallpaper': 'Вы действительно хотите удалить обои?',
        'wallpaper_removed': 'Обои успешно удалены',
        'error_remove_wallpaper': 'Не удалось удалить обои',
        'wallpaper_settings_adjust': 'Настройки текущих обоев',
        'update_settings': 'Обновить настройки',
        'wallpaper_preview': 'Предпросмотр обоев',
        'preview_wallpaper_placeholder': 'Перетащите или выберите изображение',
        'selected_wallpaper': 'Выбранные обои',
        'path': 'Путь',
        'size': 'Размер',
        'mode': 'Режим',
        'preview_note': 'Это только предпросмотр — для применения нажмите «Применить»',
        'no_wallpaper_preview': 'Обои не выбраны',
        'invalid_image': 'Неподдерживаемый формат изображения',
        'load_error': 'Не удалось загрузить изображение',
        'settings_updated': 'Настройки успешно обновлены',
        'settings_applied': 'Настройки успешно применены',
        'confirm': 'Подтвердить',
        'error_apply': 'Ошибка при применении настроек',
        'drag_drop_here': 'Перетащите изображение сюда',
        'or_click_browse': 'или нажмите «Обзор»',
        'drag_drop_hint': 'Можно просто перетащить файл изображения из файлового менеджера',
        'browse_tooltip': 'Выбрать файл изображения',
        'file_dropped': 'Файл перетащен',
        'file_dropped_success': 'Изображение успешно добавлено',
        'overclock_mode': 'Режим разгона',
        'custom_rate': 'Ручная частота',
        'auto_detect': 'Автоопределение',
        'display_info': 'Информация о дисплее',
        'confirm_settings': 'Подтверждение настроек',
        'revert_timer': 'Обратный отсчёт',
        'redshift_settings': 'Настройки ночного света',
        'enable_redshift': 'Включить ночной свет',
        'color_temperature': 'Цветовая температура',
        'temperature_presets': 'Предустановки температуры',
        'auto_mode': 'Автоматический режим',
        'enable_auto_mode': 'Включить автоматическую регулировку',
        'location': 'Местоположение',
        'latitude_placeholder': 'Широта',
        'longitude_placeholder': 'Долгота',
        'detect_location': 'Определить местоположение',
        'stop_redshift': 'Остановить ночной свет',
        'redshift_running': 'Ночной свет активен',
        'redshift_stopped': 'Ночной свет остановлен',
        'redshift_disabled': 'Ночной свет отключён',
        'redshift_applied': 'Настройки ночного света успешно применены',
        'error_redshift': 'Не удалось применить настройки ночного света',
        'redshift_not_installed': 'Redshift не установлен',
        'keyboard_settings': 'Настройки клавиатуры',
        'keyboard_layouts': 'Раскладки клавиатуры',
        'primary_layout': 'Основная раскладка',
        'additional_layouts': 'Дополнительные раскладки',
        'add_layout': 'Добавить',
        'remove_layout': 'Удалить',
        'switch_shortcut': 'Сочетание для переключения',
        'keybindings': 'Горячие клавиши',
        'shortcut': 'Сочетание клавиш',
        'command': 'Команда',
        'add': 'Добавить',
        'edit': 'Изменить',
        'remove': 'Удалить',
        'apply_layouts': 'Применить раскладки',
        'apply_keybindings': 'Применить горячие клавиши',
    },

    'es': {
        'app_title': 'Ajustes de EN-OS',
        'header': 'Ajustes de EN-OS',
        'display_settings': 'Configuración de pantalla',
        'display_desc': 'Ajusta la resolución y gestiona varios monitores',
        'wallpaper_settings': 'Fondo de escritorio',
        'wallpaper_desc': 'Elige y establece tu fondo de pantalla favorito',
        'mouse_touchpad': 'Ratón y touchpad',
        'mouse_touchpad_desc': 'Personaliza la velocidad del cursor y gestos del touchpad',
        'theme_settings': 'Temas',
        'theme_desc': 'Selecciona un tema elegante para IceWM',
        'footer': 'EN-OS · Hecho con cariño ❤️',
        'language': 'Idioma',
        'error_title': 'Error',
        'error_launch': 'No se pudo ejecutar el comando: {}',
        'error_file_not_found': 'Archivo no encontrado: {}',
        'error_permission': 'Permiso denegado: {}',
        'error_unknown': 'Error desconocido: {}',
        'close': 'Cerrar',
        'apply': 'Aplicar',
        'cancel': 'Cancelar',
        'ok': 'Aceptar',
        'select_wallpaper': 'Seleccionar fondo',
        'wallpaper_applied': 'Fondo aplicado correctamente',
        'error_wallpaper': 'No se pudo aplicar el fondo',
        'mouse_speed': 'Velocidad del cursor',
        'mouse_accel': 'Aceleración del ratón',
        'tap_to_click': 'Tocar para hacer clic',
        'no_touchpad': 'No se detectó touchpad',
        'touchpad_detected': 'Touchpad detectado',
        'resolution': 'Resolución',
        'refresh_rate': 'Tasa de refresco',
        'primary_display': 'Hacer pantalla principal',
        'detect_displays': 'Detectar pantallas',
        'theme_select': 'Seleccionar tema',
        'theme_applied': 'Tema aplicado correctamente',
        'error_theme': 'No se pudo aplicar el tema',
        'current_settings': 'Configuración actual',
        'set_new_wallpaper': 'Establecer nuevo fondo',
        'wallpaper_path': 'Archivo de fondo',
        'select_wallpaper_placeholder': 'Selecciona archivo de fondo…',
        'wallpaper_mode': 'Modo de visualización',
        'browse': 'Examinar…',
        'preview': 'Vista previa',
        'current_wallpaper': 'Fondo actual',
        'no_wallpaper_set': 'No hay fondo establecido',
        'remove_wallpaper': 'Eliminar fondo',
        'invalid_path': 'Ruta de archivo inválida',
        'preview_applied': 'Vista previa aplicada',
        'error_preview': 'Error al aplicar vista previa',
        'select_wallpaper_first': 'Primero selecciona un fondo',
        'file_not_found': 'Archivo no encontrado',
        'confirm_remove_wallpaper': '¿Realmente quieres eliminar el fondo?',
        'wallpaper_removed': 'Fondo eliminado correctamente',
        'error_remove_wallpaper': 'No se pudo eliminar el fondo',
        'wallpaper_settings_adjust': 'Ajustes del fondo actual',
        'update_settings': 'Actualizar ajustes',
        'wallpaper_preview': 'Vista previa del fondo',
        'preview_wallpaper_placeholder': 'Arrastra o selecciona una imagen',
        'selected_wallpaper': 'Fondo seleccionado',
        'path': 'Ruta',
        'size': 'Tamaño',
        'mode': 'Modo',
        'preview_note': 'Esto es solo una vista previa — pulsa "Aplicar" para establecer el fondo',
        'no_wallpaper_preview': 'No hay fondo seleccionado',
        'invalid_image': 'Formato de imagen no compatible',
        'load_error': 'No se pudo cargar la imagen',
        'settings_updated': 'Ajustes actualizados correctamente',
        'settings_applied': 'Ajustes aplicados correctamente',
        'confirm': 'Confirmar',
        'error_apply': 'Error al aplicar ajustes',
        'drag_drop_here': 'Arrastra la imagen aquí',
        'or_click_browse': 'o pulsa Examinar',
        'drag_drop_hint': 'Puedes arrastrar archivos de imagen desde el explorador de archivos',
        'browse_tooltip': 'Buscar archivos de imagen',
        'file_dropped': 'Archivo soltado',
        'file_dropped_success': 'Imagen añadida correctamente',
        'overclock_mode': 'Modo overclock',
        'custom_rate': 'Frecuencia personalizada',
        'auto_detect': 'Detección automática',
        'display_info': 'Información de pantalla',
        'confirm_settings': 'Confirmar ajustes',
        'revert_timer': 'Cuenta regresiva de reversión',
        'redshift_settings': 'Ajustes de Luz Nocturna',
        'enable_redshift': 'Activar Luz Nocturna',
        'color_temperature': 'Temperatura de color',
        'temperature_presets': 'Preajustes de temperatura',
        'auto_mode': 'Modo automático',
        'enable_auto_mode': 'Activar ajuste automático',
        'location': 'Ubicación',
        'latitude_placeholder': 'Latitud',
        'longitude_placeholder': 'Longitud',
        'detect_location': 'Detectar ubicación',
        'stop_redshift': 'Detener Luz Nocturna',
        'redshift_running': 'Luz Nocturna activa',
        'redshift_stopped': 'Luz Nocturna detenida',
        'redshift_disabled': 'Luz Nocturna desactivada',
        'redshift_applied': 'Ajustes de Luz Nocturna aplicados correctamente',
        'error_redshift': 'No se pudieron aplicar los ajustes de Luz Nocturna',
        'redshift_not_installed': 'Redshift no está instalado'
    },

    'fr': {
        'app_title': 'Paramètres EN-OS',
        'header': 'Paramètres EN-OS',
        'display_settings': 'Paramètres d\'affichage',
        'display_desc': 'Réglage de la résolution et gestion de plusieurs écrans',
        'wallpaper_settings': 'Fond d\'écran',
        'wallpaper_desc': 'Choisissez et appliquez votre fond d\'écran préféré',
        'mouse_touchpad': 'Souris et pavé tactile',
        'mouse_touchpad_desc': 'Personnalisez la vitesse du curseur et les gestes du pavé tactile',
        'theme_settings': 'Thèmes',
        'theme_desc': 'Sélectionnez un beau thème pour IceWM',
        'footer': 'EN-OS · Créé avec soin ❤️',
        'language': 'Langue',
        'error_title': 'Erreur',
        'error_launch': 'Impossible d\'exécuter la commande : {}',
        'error_file_not_found': 'Fichier non trouvé : {}',
        'error_permission': 'Permission refusée : {}',
        'error_unknown': 'Erreur inconnue : {}',
        'close': 'Fermer',
        'apply': 'Appliquer',
        'cancel': 'Annuler',
        'ok': 'OK',
        'select_wallpaper': 'Sélectionner un fond d\'écran',
        'wallpaper_applied': 'Fond d\'écran appliqué avec succès',
        'error_wallpaper': 'Échec de l\'application du fond d\'écran',
        'mouse_speed': 'Vitesse du curseur',
        'mouse_accel': 'Accélération de la souris',
        'tap_to_click': 'Tactile pour cliquer',
        'no_touchpad': 'Aucun pavé tactile détecté',
        'touchpad_detected': 'Pavé tactile détecté',
        'resolution': 'Résolution',
        'refresh_rate': 'Taux de rafraîchissement',
        'primary_display': 'Définir comme écran principal',
        'detect_displays': 'Détecter les écrans',
        'theme_select': 'Sélectionner un thème',
        'theme_applied': 'Thème appliqué avec succès',
        'error_theme': 'Échec de l\'application du thème',
        'current_settings': 'Paramètres actuels',
        'set_new_wallpaper': 'Définir un nouveau fond',
        'wallpaper_path': 'Fichier du fond',
        'select_wallpaper_placeholder': 'Sélectionner le fichier du fond…',
        'wallpaper_mode': 'Mode d\'affichage',
        'browse': 'Parcourir…',
        'preview': 'Aperçu',
        'current_wallpaper': 'Fond actuel',
        'no_wallpaper_set': 'Aucun fond défini',
        'remove_wallpaper': 'Supprimer le fond',
        'invalid_path': 'Chemin de fichier invalide',
        'preview_applied': 'Aperçu appliqué',
        'error_preview': 'Erreur lors de l\'application de l\'aperçu',
        'select_wallpaper_first': 'Veuillez d\'abord sélectionner un fond',
        'file_not_found': 'Fichier non trouvé',
        'confirm_remove_wallpaper': 'Voulez-vous vraiment supprimer le fond d\'écran ?',
        'wallpaper_removed': 'Fond supprimé avec succès',
        'error_remove_wallpaper': 'Échec de la suppression du fond',
        'wallpaper_settings_adjust': 'Paramètres du fond actuel',
        'update_settings': 'Mettre à jour les paramètres',
        'wallpaper_preview': 'Aperçu du fond',
        'preview_wallpaper_placeholder': 'Glissez-déposez ou sélectionnez une image',
        'selected_wallpaper': 'Fond sélectionné',
        'path': 'Chemin',
        'size': 'Taille',
        'mode': 'Mode',
        'preview_note': 'Ceci est un simple aperçu — cliquez sur "Appliquer" pour définir le fond',
        'no_wallpaper_preview': 'Aucun fond sélectionné',
        'invalid_image': 'Format d\'image non pris en charge',
        'load_error': 'Impossible de charger l\'image',
        'settings_updated': 'Paramètres mis à jour avec succès',
        'settings_applied': 'Paramètres appliqués avec succès',
        'confirm': 'Confirmer',
        'error_apply': 'Erreur lors de l\'application des paramètres',
        'drag_drop_here': 'Glissez-déposez l\'image ici',
        'or_click_browse': 'ou cliquez sur Parcourir',
        'drag_drop_hint': 'Vous pouvez glisser-déposer des fichiers image depuis votre gestionnaire de fichiers',
        'browse_tooltip': 'Parcourir les fichiers image',
        'file_dropped': 'Fichier déposé',
        'file_dropped_success': 'Image déposée avec succès',
        'overclock_mode': 'Mode overclocking',
        'custom_rate': 'Fréquence personnalisée',
        'auto_detect': 'Détection automatique',
        'display_info': 'Informations sur l\'écran',
        'confirm_settings': 'Confirmation des paramètres',
        'revert_timer': 'Compte à rebours de retour',
        'redshift_settings': 'Paramètres de Lumière Nocturne',
        'enable_redshift': 'Activer la Lumière Nocturne',
        'color_temperature': 'Température de couleur',
        'temperature_presets': 'Préréglages de température',
        'auto_mode': 'Mode automatique',
        'enable_auto_mode': 'Activer l\'ajustement automatique',
        'location': 'Emplacement',
        'latitude_placeholder': 'Latitude',
        'longitude_placeholder': 'Longitude',
        'detect_location': 'Détecter l\'emplacement',
        'stop_redshift': 'Arrêter la Lumière Nocturne',
        'redshift_running': 'Lumière Nocturne active',
        'redshift_stopped': 'Lumière Nocturne arrêtée',
        'redshift_disabled': 'Lumière Nocturne désactivée',
        'redshift_applied': 'Paramètres de Lumière Nocturne appliqués avec succès',
        'error_redshift': 'Échec de l\'application des paramètres de Lumière Nocturne',
        'redshift_not_installed': 'Redshift n\'est pas installé'
    },

    'de': {
        'app_title': 'EN-OS Einstellungen',
        'header': 'EN-OS Einstellungen',
        'display_settings': 'Bildschirmeinstellungen',
        'display_desc': 'Auflösung anpassen und mehrere Monitore verwalten',
        'wallpaper_settings': 'Hintergrundbild',
        'wallpaper_desc': 'Wählen und setzen Sie Ihr Lieblings-Hintergrundbild',
        'mouse_touchpad': 'Maus & Touchpad',
        'mouse_touchpad_desc': 'Passen Sie Cursor-Geschwindigkeit und Touchpad-Gesten an',
        'theme_settings': 'Themen',
        'theme_desc': 'Wählen Sie ein schönes Theme für IceWM',
        'footer': 'EN-OS · Mit Liebe gemacht ❤️',
        'language': 'Sprache',
        'error_title': 'Fehler',
        'error_launch': 'Befehl konnte nicht ausgeführt werden: {}',
        'error_file_not_found': 'Datei nicht gefunden: {}',
        'error_permission': 'Zugriff verweigert: {}',
        'error_unknown': 'Unbekannter Fehler: {}',
        'close': 'Schließen',
        'apply': 'Anwenden',
        'cancel': 'Abbrechen',
        'ok': 'OK',
        'select_wallpaper': 'Hintergrund auswählen',
        'wallpaper_applied': 'Hintergrund erfolgreich angewendet',
        'error_wallpaper': 'Hintergrund konnte nicht angewendet werden',
        'mouse_speed': 'Cursor-Geschwindigkeit',
        'mouse_accel': 'Mausbeschleunigung',
        'tap_to_click': 'Tippen zum Klicken',
        'no_touchpad': 'Kein Touchpad erkannt',
        'touchpad_detected': 'Touchpad erkannt',
        'resolution': 'Auflösung',
        'refresh_rate': 'Bildwiederholrate',
        'primary_display': 'Als Hauptbildschirm festlegen',
        'detect_displays': 'Bildschirme erkennen',
        'theme_select': 'Theme auswählen',
        'theme_applied': 'Theme erfolgreich angewendet',
        'error_theme': 'Theme konnte nicht angewendet werden',
        'current_settings': 'Aktuelle Einstellungen',
        'set_new_wallpaper': 'Neuen Hintergrund setzen',
        'wallpaper_path': 'Hintergrunddatei',
        'select_wallpaper_placeholder': 'Hintergrunddatei auswählen…',
        'wallpaper_mode': 'Anzeigemodus',
        'browse': 'Durchsuchen…',
        'preview': 'Vorschau',
        'current_wallpaper': 'Aktueller Hintergrund',
        'no_wallpaper_set': 'Kein Hintergrund festgelegt',
        'remove_wallpaper': 'Hintergrund entfernen',
        'invalid_path': 'Ungültiger Dateipfad',
        'preview_applied': 'Vorschau angewendet',
        'error_preview': 'Fehler beim Anwenden der Vorschau',
        'select_wallpaper_first': 'Bitte zuerst einen Hintergrund auswählen',
        'file_not_found': 'Datei nicht gefunden',
        'confirm_remove_wallpaper': 'Möchten Sie den Hintergrund wirklich entfernen?',
        'wallpaper_removed': 'Hintergrund erfolgreich entfernt',
        'error_remove_wallpaper': 'Hintergrund konnte nicht entfernt werden',
        'wallpaper_settings_adjust': 'Einstellungen des aktuellen Hintergrunds',
        'update_settings': 'Einstellungen aktualisieren',
        'wallpaper_preview': 'Hintergrund-Vorschau',
        'preview_wallpaper_placeholder': 'Ziehen & ablegen oder Bild auswählen',
        'selected_wallpaper': 'Ausgewählter Hintergrund',
        'path': 'Pfad',
        'size': 'Größe',
        'mode': 'Modus',
        'preview_note': 'Dies ist nur eine Vorschau — klicken Sie auf "Anwenden" um den Hintergrund zu setzen',
        'no_wallpaper_preview': 'Kein Hintergrund ausgewählt',
        'invalid_image': 'Nicht unterstütztes Bildformat',
        'load_error': 'Bild konnte nicht geladen werden',
        'settings_updated': 'Einstellungen erfolgreich aktualisiert',
        'settings_applied': 'Einstellungen erfolgreich angewendet',
        'confirm': 'Bestätigen',
        'error_apply': 'Fehler beim Anwenden der Einstellungen',
        'drag_drop_here': 'Bild hierher ziehen',
        'or_click_browse': 'oder auf Durchsuchen klicken',
        'drag_drop_hint': 'Sie können Bilddateien aus Ihrem Dateimanager ziehen und ablegen',
        'browse_tooltip': 'Nach Bilddateien suchen',
        'file_dropped': 'Datei abgelegt',
        'file_dropped_success': 'Bilddatei erfolgreich abgelegt',
        'overclock_mode': 'Overclock-Modus',
        'custom_rate': 'Benutzerdefinierte Bildwiederholrate',
        'auto_detect': 'Automatische Erkennung',
        'display_info': 'Bildschirminformationen',
        'confirm_settings': 'Einstellungen bestätigen',
        'revert_timer': 'Rücksetz-Countdown',
        'redshift_settings': 'Nachtlicht-Einstellungen',
        'enable_redshift': 'Nachtlicht aktivieren',
        'color_temperature': 'Farbtemperatur',
        'temperature_presets': 'Temperatur-Voreinstellungen',
        'auto_mode': 'Automatischer Modus',
        'enable_auto_mode': 'Automatische Anpassung aktivieren',
        'location': 'Standort',
        'latitude_placeholder': 'Breitengrad',
        'longitude_placeholder': 'Längengrad',
        'detect_location': 'Standort erkennen',
        'stop_redshift': 'Nachtlicht stoppen',
        'redshift_running': 'Nachtlicht ist aktiv',
        'redshift_stopped': 'Nachtlicht gestoppt',
        'redshift_disabled': 'Nachtlicht deaktiviert',
        'redshift_applied': 'Nachtlicht-Einstellungen erfolgreich angewendet',
        'error_redshift': 'Nachtlicht-Einstellungen konnten nicht angewendet werden',
        'redshift_not_installed': 'Redshift ist nicht installiert'
    },

    'zh_CN': {
        'app_title': 'EN-OS 设置',
        'header': 'EN-OS 设置',
        'display_settings': '显示设置',
        'display_desc': '调整屏幕分辨率和管理多显示器',
        'wallpaper_settings': '桌面壁纸',
        'wallpaper_desc': '选择并设置您喜爱的桌面背景',
        'mouse_touchpad': '鼠标与触控板',
        'mouse_touchpad_desc': '自定义光标速度和触控板手势',
        'theme_settings': '主题',
        'theme_desc': '为 IceWM 挑选漂亮的主题',
        'footer': 'EN-OS · 用心制作 ❤️',
        'language': '语言',
        'error_title': '错误',
        'error_launch': '无法执行命令：{}',
        'error_file_not_found': '文件未找到：{}',
        'error_permission': '权限被拒绝：{}',
        'error_unknown': '未知错误：{}',
        'close': '关闭',
        'apply': '应用',
        'cancel': '取消',
        'ok': '确定',
        'select_wallpaper': '选择壁纸',
        'wallpaper_applied': '壁纸设置成功',
        'error_wallpaper': '无法应用壁纸',
        'mouse_speed': '光标速度',
        'mouse_accel': '鼠标加速',
        'tap_to_click': '轻触即点',
        'no_touchpad': '未检测到触控板',
        'touchpad_detected': '触控板已检测到',
        'resolution': '分辨率',
        'refresh_rate': '刷新率',
        'primary_display': '设为主显示器',
        'detect_displays': '检测显示器',
        'theme_select': '选择主题',
        'theme_applied': '主题应用成功',
        'error_theme': '无法应用主题',
        'current_settings': '当前设置',
        'set_new_wallpaper': '设置新壁纸',
        'wallpaper_path': '壁纸文件',
        'select_wallpaper_placeholder': '选择壁纸文件…',
        'wallpaper_mode': '显示模式',
        'browse': '浏览…',
        'preview': '预览',
        'current_wallpaper': '当前壁纸',
        'no_wallpaper_set': '未设置壁纸',
        'remove_wallpaper': '移除壁纸',
        'invalid_path': '无效的文件路径',
        'preview_applied': '预览已应用',
        'error_preview': '应用预览时出错',
        'select_wallpaper_first': '请先选择壁纸',
        'file_not_found': '文件未找到',
        'confirm_remove_wallpaper': '确定要移除壁纸吗？',
        'wallpaper_removed': '壁纸已成功移除',
        'error_remove_wallpaper': '无法移除壁纸',
        'wallpaper_settings_adjust': '当前壁纸设置',
        'update_settings': '更新设置',
        'wallpaper_preview': '壁纸预览',
        'preview_wallpaper_placeholder': '拖放或选择图片',
        'selected_wallpaper': '已选择的壁纸',
        'path': '路径',
        'size': '大小',
        'mode': '模式',
        'preview_note': '这只是预览 — 点击「应用」来设置壁纸',
        'no_wallpaper_preview': '未选择壁纸',
        'invalid_image': '不支持的图片格式',
        'load_error': '无法加载图片',
        'settings_updated': '设置更新成功',
        'settings_applied': '设置应用成功',
        'confirm': '确认',
        'error_apply': '应用设置时出错',
        'drag_drop_here': '将图片拖放到此处',
        'or_click_browse': '或点击浏览',
        'drag_drop_hint': '您可以直接从文件管理器拖放图片文件',
        'browse_tooltip': '浏览图片文件',
        'file_dropped': '文件已拖放',
        'file_dropped_success': '图片文件成功添加',
        'overclock_mode': '超频模式',
        'custom_rate': '自定义刷新率',
        'auto_detect': '自动检测',
        'display_info': '显示器信息',
        'confirm_settings': '确认设置',
        'revert_timer': '恢复倒计时',
        'redshift_settings': '夜灯设置',
        'enable_redshift': '启用夜灯模式',
        'color_temperature': '色温',
        'temperature_presets': '色温预设',
        'auto_mode': '自动模式',
        'enable_auto_mode': '启用自动调节',
        'location': '位置',
        'latitude_placeholder': '纬度',
        'longitude_placeholder': '经度',
        'detect_location': '检测位置',
        'stop_redshift': '停止夜灯',
        'redshift_running': '夜灯正在运行',
        'redshift_stopped': '夜灯已停止',
        'redshift_disabled': '夜灯已禁用',
        'redshift_applied': '夜灯设置已成功应用',
        'error_redshift': '无法应用夜灯设置',
        'redshift_not_installed': '未安装 Redshift'
    },

    'ja': {
        'app_title': 'EN-OS 設定',
        'header': 'EN-OS 設定',
        'display_settings': 'ディスプレイ設定',
        'display_desc': '画面解像度の調整と複数モニターの管理',
        'wallpaper_settings': '壁紙',
        'wallpaper_desc': 'お気に入りのデスクトップ壁紙を選択・設定',
        'mouse_touchpad': 'マウス＆タッチパッド',
        'mouse_touchpad_desc': 'カーソル速度とタッチパッドジェスチャーをカスタマイズ',
        'theme_settings': 'テーマ',
        'theme_desc': 'IceWM に素敵なテーマを選ぶ',
        'footer': 'EN-OS · 心を込めて作りました ❤️',
        'language': '言語',
        'error_title': 'エラー',
        'error_launch': 'コマンドを実行できませんでした：{}',
        'error_file_not_found': 'ファイルが見つかりません：{}',
        'error_permission': '権限が拒否されました：{}',
        'error_unknown': '不明なエラー：{}',
        'close': '閉じる',
        'apply': '適用',
        'cancel': 'キャンセル',
        'ok': 'OK',
        'select_wallpaper': '壁紙を選択',
        'wallpaper_applied': '壁紙を適用しました',
        'error_wallpaper': '壁紙の適用に失敗しました',
        'mouse_speed': 'カーソル速度',
        'mouse_accel': 'マウス加速',
        'tap_to_click': 'タップでクリック',
        'no_touchpad': 'タッチパッドが検出されません',
        'touchpad_detected': 'タッチパッドを検出しました',
        'resolution': '解像度',
        'refresh_rate': 'リフレッシュレート',
        'primary_display': 'メインディスプレイに設定',
        'detect_displays': 'ディスプレイを検出',
        'theme_select': 'テーマを選択',
        'theme_applied': 'テーマを適用しました',
        'error_theme': 'テーマの適用に失敗しました',
        'current_settings': '現在の設定',
        'set_new_wallpaper': '新しい壁紙を設定',
        'wallpaper_path': '壁紙ファイル',
        'select_wallpaper_placeholder': '壁紙ファイルを選択…',
        'wallpaper_mode': '表示モード',
        'browse': '参照…',
        'preview': 'プレビュー',
        'current_wallpaper': '現在の壁紙',
        'no_wallpaper_set': '壁紙が設定されていません',
        'remove_wallpaper': '壁紙を削除',
        'invalid_path': '無効なファイルパス',
        'preview_applied': 'プレビューを適用しました',
        'error_preview': 'プレビューの適用に失敗',
        'select_wallpaper_first': '先に壁紙を選択してください',
        'file_not_found': 'ファイルが見つかりません',
        'confirm_remove_wallpaper': '本当に壁紙を削除しますか？',
        'wallpaper_removed': '壁紙を削除しました',
        'error_remove_wallpaper': '壁紙の削除に失敗しました',
        'wallpaper_settings_adjust': '現在の壁紙設定',
        'update_settings': '設定を更新',
        'wallpaper_preview': '壁紙プレビュー',
        'preview_wallpaper_placeholder': 'ドラッグ＆ドロップまたは画像を選択',
        'selected_wallpaper': '選択した壁紙',
        'path': 'パス',
        'size': 'サイズ',
        'mode': 'モード',
        'preview_note': 'これはプレビューのみです — 「適用」を押して壁紙を設定してください',
        'no_wallpaper_preview': '壁紙が選択されていません',
        'invalid_image': '対応していない画像形式です',
        'load_error': '画像を読み込めませんでした',
        'settings_updated': '設定を更新しました',
        'settings_applied': '設定を適用しました',
        'confirm': '確認',
        'error_apply': '設定の適用中にエラー',
        'drag_drop_here': 'ここに画像をドラッグ＆ドロップ',
        'or_click_browse': 'または「参照」をクリック',
        'drag_drop_hint': 'ファイルマネージャーから画像ファイルをドラッグ＆ドロップできます',
        'browse_tooltip': '画像ファイルを参照',
        'file_dropped': 'ファイルがドロップされました',
        'file_dropped_success': '画像ファイルを正常に追加しました',
        'overclock_mode': 'オーバークロックモード',
        'custom_rate': 'カスタムリフレッシュレート',
        'auto_detect': '自動検出',
        'display_info': 'ディスプレイ情報',
        'confirm_settings': '設定の確認',
        'revert_timer': '元に戻すカウントダウン',
        'redshift_settings': 'ナイトライト設定',
        'enable_redshift': 'ナイトライトを有効にする',
        'color_temperature': '色温度',
        'temperature_presets': '温度プリセット',
        'auto_mode': '自動モード',
        'enable_auto_mode': '自動調整を有効にする',
        'location': '位置',
        'latitude_placeholder': '緯度',
        'longitude_placeholder': '経度',
        'detect_location': '位置を検出',
        'stop_redshift': 'ナイトライトを停止',
        'redshift_running': 'ナイトライトが動作中',
        'redshift_stopped': 'ナイトライト停止中',
        'redshift_disabled': 'ナイトライトが無効',
        'redshift_applied': 'ナイトライト設定を適用しました',
        'error_redshift': 'ナイトライト設定の適用に失敗しました',
        'redshift_not_installed': 'Redshift がインストールされていません'
    },

    'ko': {
        'app_title': 'EN-OS 설정',
        'header': 'EN-OS 설정',
        'display_settings': '디스플레이 설정',
        'display_desc': '화면 해상도 조정 및 다중 모니터 관리',
        'wallpaper_settings': '배경화면',
        'wallpaper_desc': '좋아하는 데스크톱 배경화면 선택 및 설정',
        'mouse_touchpad': '마우스 & 터치패드',
        'mouse_touchpad_desc': '커서 속도와 터치패드 제스처 사용자 지정',
        'theme_settings': '테마',
        'theme_desc': 'IceWM에 멋진 테마 선택하기',
        'footer': 'EN-OS · 정성껏 만들었습니다 ❤️',
        'language': '언어',
        'error_title': '오류',
        'error_launch': '명령 실행 실패: {}',
        'error_file_not_found': '파일을 찾을 수 없음: {}',
        'error_permission': '권한 거부됨: {}',
        'error_unknown': '알 수 없는 오류: {}',
        'close': '닫기',
        'apply': '적용',
        'cancel': '취소',
        'ok': '확인',
        'select_wallpaper': '배경화면 선택',
        'wallpaper_applied': '배경화면이 성공적으로 적용되었습니다',
        'error_wallpaper': '배경화면 적용 실패',
        'mouse_speed': '커서 속도',
        'mouse_accel': '마우스 가속',
        'tap_to_click': '탭하여 클릭',
        'no_touchpad': '터치패드가 감지되지 않음',
        'touchpad_detected': '터치패드 감지됨',
        'resolution': '해상도',
        'refresh_rate': '주사율',
        'primary_display': '기본 디스플레이로 설정',
        'detect_displays': '디스플레이 감지',
        'theme_select': '테마 선택',
        'theme_applied': '테마가 성공적으로 적용되었습니다',
        'error_theme': '테마 적용 실패',
        'current_settings': '현재 설정',
        'set_new_wallpaper': '새 배경화면 설정',
        'wallpaper_path': '배경화면 파일',
        'select_wallpaper_placeholder': '배경화면 파일 선택…',
        'wallpaper_mode': '표시 모드',
        'browse': '찾아보기…',
        'preview': '미리보기',
        'current_wallpaper': '현재 배경화면',
        'no_wallpaper_set': '배경화면이 설정되지 않음',
        'remove_wallpaper': '배경화면 제거',
        'invalid_path': '잘못된 파일 경로',
        'preview_applied': '미리보기 적용됨',
        'error_preview': '미리보기 적용 오류',
        'select_wallpaper_first': '먼저 배경화면을 선택해주세요',
        'file_not_found': '파일을 찾을 수 없음',
        'confirm_remove_wallpaper': '정말 배경화면을 제거하시겠습니까?',
        'wallpaper_removed': '배경화면이 성공적으로 제거되었습니다',
        'error_remove_wallpaper': '배경화면 제거 실패',
        'wallpaper_settings_adjust': '현재 배경화면 설정',
        'update_settings': '설정 업데이트',
        'wallpaper_preview': '배경화면 미리보기',
        'preview_wallpaper_placeholder': '드래그 앤 드롭 또는 이미지 선택',
        'selected_wallpaper': '선택한 배경화면',
        'path': '경로',
        'size': '크기',
        'mode': '모드',
        'preview_note': '이것은 미리보기일 뿐입니다 — 「적용」을 눌러 배경화면을 설정하세요',
        'no_wallpaper_preview': '배경화면이 선택되지 않음',
        'invalid_image': '지원되지 않는 이미지 형식',
        'load_error': '이미지를 불러올 수 없음',
        'settings_updated': '설정이 성공적으로 업데이트되었습니다',
        'settings_applied': '설정이 성공적으로 적용되었습니다',
        'confirm': '확인',
        'error_apply': '설정 적용 중 오류',
        'drag_drop_here': '여기에 이미지를 드래그 앤 드롭',
        'or_click_browse': '또는 찾아보기를 클릭',
        'drag_drop_hint': '파일 관리자에서 이미지 파일을 드래그 앤 드롭할 수 있습니다',
        'browse_tooltip': '이미지 파일 찾아보기',
        'file_dropped': '파일이 드롭됨',
        'file_dropped_success': '이미지 파일이 성공적으로 추가되었습니다',
        'overclock_mode': '오버클럭 모드',
        'custom_rate': '사용자 지정 주사율',
        'auto_detect': '자동 감지',
        'display_info': '디스플레이 정보',
        'confirm_settings': '설정 확인',
        'revert_timer': '복구 카운트다운',
        'redshift_settings': '야간 조명 설정',
        'enable_redshift': '야간 조명 활성화',
        'color_temperature': '색온도',
        'temperature_presets': '색온도 프리셋',
        'auto_mode': '자동 모드',
        'enable_auto_mode': '자동 조정 활성화',
        'location': '위치',
        'latitude_placeholder': '위도',
        'longitude_placeholder': '경도',
        'detect_location': '위치 감지',
        'stop_redshift': '야간 조명 중지',
        'redshift_running': '야간 조명이 실행 중',
        'redshift_stopped': '야간 조명 중지됨',
        'redshift_disabled': '야간 조명 비활성화됨',
        'redshift_applied': '야간 조명 설정이 성공적으로 적용되었습니다',
        'error_redshift': '야간 조명 설정 적용 실패',
        'redshift_not_installed': 'Redshift가 설치되지 않았습니다'
    }
}

COLORS = {
    'primary': {
        'dark': '#0f0f23',
        'medium': '#1a1a2e',
        'light': '#16213e'
    },
    'accent': {
        'blue': '#4fc4cf',
        'purple': '#9d4edd',
        'cyan': '#00bbf9',
        'dark_blue': '#4361ee'
    },
    'text': {
        'primary': '#ffffff',
        'secondary': '#b8b8d1',
        'muted': '#8b8ba7'
    },
    'misc': {
        'border': '#2d2d4d',
        'success': '#4cd964',
        'error': '#ff4757'
    }
}

class LanguageManager:
    def __init__(self):
        self.current_language = self.detect_system_language()
        self.load_language_setting()

    def detect_system_language(self):
        lang_map = {
            'en': 'en',
            'ru': 'ru',
            'uk': 'ru',
            'es': 'es',
            'fr': 'fr',
            'de': 'de',
            'zh': 'zh_CN',
            'ja': 'ja',
            'ko': 'ko',
        }
        default = 'en'

        try:
            lang_env = os.environ.get('LANG', '') or os.environ.get('LANGUAGE', '')
            if lang_env:
                lang_code = lang_env.split('_')[0].lower()
                return lang_map.get(lang_code, default)

            system_locale = locale.getdefaultlocale()[0]
            if system_locale:
                lang_code = system_locale.split('_')[0].lower()
                return lang_map.get(lang_code, default)

            result = subprocess.run(['locale'], capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('LANG=') or line.startswith('LANGUAGE='):
                        lang_code = line.split('=')[1].split('_')[0].lower().replace('"', '')
                        return lang_map.get(lang_code, default)
        except Exception as e:
            print(f"Language detection error: {e}")

        return default

    def load_language_setting(self):
        try:
            config_dir = Path.home() / '.config' / 'enos_manager'
            config_dir.mkdir(parents=True, exist_ok=True)
            config_file = config_dir / 'settings.json'

            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    saved_language = settings.get('language')
                    if saved_language in LOCALES:
                        self.current_language = saved_language
        except Exception as e:
            print(f"Error loading language settings: {e}")

    def save_language_setting(self):
        try:
            config_dir = Path.home() / '.config' / 'enos_manager'
            config_dir.mkdir(parents=True, exist_ok=True)

            config_file = config_dir / 'settings.json'
            settings = {'language': self.current_language}

            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving language settings: {e}")

    def get_text(self, key):
        return LOCALES[self.current_language].get(key, key)

    def set_language(self, language):
        if language in LOCALES:
            self.current_language = language
            self.save_language_setting()
            return True
        return False

class StyledDialog(QDialog):
    def __init__(self, title, language_manager, parent=None):
        super().__init__(parent)
        self.language_manager = language_manager
        self.setWindowTitle(title)
        self.setModal(True)
        self.set_modern_style()

    def set_modern_style(self):
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 12px;
            }}
            QLabel {{
                color: {COLORS['text']['primary']};
                font-size: 13px;
            }}
            QLabel[title="true"] {{
                font-size: 15px;
                font-weight: bold;
                color: {COLORS['accent']['blue']};
                padding: 5px;
            }}
            QLineEdit, QComboBox, QSpinBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus {{
                border: 2px solid {COLORS['accent']['blue']};
            }}
            QPushButton {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: medium;
            }}
            QPushButton:hover {{
                background-color: {COLORS['primary']['light']};
                border: 1px solid {COLORS['accent']['blue']};
            }}
            QPushButton:pressed {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
            QPushButton[primary="true"] {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
                font-weight: bold;
            }}
            QPushButton[primary="true"]:hover {{
                background-color: {COLORS['accent']['cyan']};
            }}
            QCheckBox {{
                color: {COLORS['text']['primary']};
                font-size: 13px;
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 16px;
                height: 16px;
            }}
            QCheckBox::indicator:unchecked {{
                background-color: {COLORS['primary']['medium']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 3px;
            }}
            QCheckBox::indicator:checked {{
                background-color: {COLORS['accent']['blue']};
                border: 1px solid {COLORS['accent']['blue']};
                border-radius: 3px;
                image: url(checkbox-checked.png);
            }}
            QGroupBox {{
                color: {COLORS['accent']['blue']};
                font-weight: bold;
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 10px;
                font-size: 14px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 8px 0 8px;
            }}
            QListWidget {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 4px;
                font-size: 13px;
                outline: none;
            }}
            QListWidget::item {{
                padding: 8px;
                border-radius: 4px;
            }}
            QListWidget::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
            QListWidget::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QScrollBar:vertical {{
                background-color: {COLORS['primary']['medium']};
                width: 8px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical {{
                background-color: {COLORS['accent']['blue']};
                border-radius: 4px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {COLORS['accent']['cyan']};
            }}
        """)

class MinimalButton(QPushButton):
    def __init__(self, text, icon=None, color_scheme='blue', parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(70)

        try:
            self.setFont(QFont("DejaVu Sans", 44))
        except:
            self.setFont(QFont("Arial", 44))

        self._opacity = 1.0
        self._scale = 1.0
        self.color_scheme = color_scheme

        if icon:
            self.setIcon(icon)
            self.setIconSize(QSize(24, 24))

        self.update_style()

        self.hover_animation = QPropertyAnimation(self, b"scale")
        self.hover_animation.setDuration(200)
        self.hover_animation.setEasingCurve(QEasingCurve.Type.OutBack)

        self.click_animation = QPropertyAnimation(self, b"opacity")
        self.click_animation.setDuration(100)
        self.click_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def update_style(self):
        colors = {
            'blue': {'bg': '#2a2a4a', 'hover': '#3a3a5a', 'text': COLORS['accent']['blue']},
            'purple': {'bg': '#2a2a4a', 'hover': '#3a3a5a', 'text': COLORS['accent']['purple']},
            'cyan': {'bg': '#2a2a4a', 'hover': '#3a3a5a', 'text': COLORS['accent']['cyan']},
            'green': {'bg': '#2a2a4a', 'hover': '#3a3a5a', 'text': '#4cd964'}
        }

        color = colors.get(self.color_scheme, colors['blue'])

        self.setStyleSheet(f"""
            MinimalButton {{
                background-color: {color['bg']};
                color: {color['text']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
                padding: 15px 20px;
                text-align: center;
                font-weight: normal;
                font-size: 20px;
            }}
            MinimalButton:hover {{
                background-color: {color['hover']};
                border: 1px solid {color['text']};
            }}
            MinimalButton:pressed {{
                background-color: {color['bg']};
                border: 1px solid {color['text']};
            }}
        """)

    def get_opacity(self):
        return self._opacity

    def set_opacity(self, opacity):
        self._opacity = opacity
        self.update()

    def get_scale(self):
        return self._scale

    def set_scale(self, scale):
        self._scale = scale
        self.update()

    opacity = pyqtProperty(float, get_opacity, set_opacity)
    scale = pyqtProperty(float, get_scale, set_scale)

    def enterEvent(self, event):
        self.hover_animation.stop()
        self.hover_animation.setStartValue(self.scale)
        self.hover_animation.setEndValue(1.02)
        self.hover_animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hover_animation.stop()
        self.hover_animation.setStartValue(self.scale)
        self.hover_animation.setEndValue(1.0)
        self.hover_animation.start()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.click_animation.stop()
        self.click_animation.setStartValue(self.opacity)
        self.click_animation.setEndValue(0.95)
        self.click_animation.start()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.click_animation.stop()
        self.click_animation.setStartValue(self.opacity)
        self.click_animation.setEndValue(1.0)
        self.click_animation.start()
        super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self._opacity)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.translate(self.rect().center())
        painter.scale(self._scale, self._scale)
        painter.translate(-self.rect().center())

        super().paintEvent(event)

class ModernCard(QFrame):
    def __init__(self, title, description, icon=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            ModernCard {{
                background-color: {COLORS['primary']['medium']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 12px;
                padding: 0px;
            }}
        """)
        self.setMinimumHeight(100)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(12)

        if icon:
            icon_label = QLabel()
            icon_label.setPixmap(icon.pixmap(32, 32))
            icon_label.setStyleSheet("padding: 3px;")
            layout.addWidget(icon_label)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(4)

        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {COLORS['text']['primary']};
                font-size: 14px;
                font-weight: bold;
            }}
        """)

        desc_label = QLabel(description)
        desc_label.setStyleSheet(f"""
            QLabel {{
                color: {COLORS['text']['secondary']};
                font-size: 12px;
            }}
        """)
        desc_label.setWordWrap(True)
        desc_label.setFixedHeight(70)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        layout.addLayout(text_layout)


class DisplaySettingsDialog(StyledDialog):
    timer_updated = pyqtSignal(str)

    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('display_settings'), language_manager, parent)
        self.setFixedSize(700, 600)

        self.current_wallpaper = None
        self.load_current_wallpaper()

        self.display_data = {}

        self.revert_timer = QTimer()
        self.revert_timer.timeout.connect(self.on_timer_tick)
        self.revert_time_left = 0
        self.original_settings = {}
        self.last_applied_settings = None

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(12)

        display_group = QGroupBox(language_manager.get_text('detect_displays'))
        display_layout = QVBoxLayout()
        self.displays_list = QListWidget()
        self.displays_list.setFixedHeight(120)
        display_layout.addWidget(self.displays_list)
        display_group.setLayout(display_layout)
        content_layout.addWidget(display_group)

        settings_group = QGroupBox(language_manager.get_text('resolution'))
        settings_layout = QGridLayout()
        settings_layout.setSpacing(10)

        settings_layout.addWidget(QLabel(language_manager.get_text('resolution') + ":"), 0, 0)
        self.resolution_combo = QComboBox()
        self.resolution_combo.currentTextChanged.connect(self.update_refresh_rates)
        settings_layout.addWidget(self.resolution_combo, 0, 1)

        settings_layout.addWidget(QLabel(language_manager.get_text('refresh_rate') + ":"), 1, 0)
        self.refresh_combo = QComboBox()
        settings_layout.addWidget(self.refresh_combo, 1, 1)

        self.overclock_check = QCheckBox(language_manager.get_text('overclock_mode') or "Режим разгона")
        settings_layout.addWidget(self.overclock_check, 2, 0, 1, 2)
        self.overclock_check.stateChanged.connect(self.on_overclock_changed)

        self.custom_rate_layout = QHBoxLayout()
        self.custom_rate_layout.addWidget(QLabel(self.language_manager.get_text('custom_rate') or "Ручная настройка:"))
        self.custom_rate_slider = QSlider(Qt.Orientation.Horizontal)
        self.custom_rate_slider.setRange(10, 240)
        self.custom_rate_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.custom_rate_slider.setTickInterval(10)
        self.custom_rate_slider.setEnabled(False)
        self.custom_rate_label = QLabel("60 Hz")
        self.custom_rate_slider.valueChanged.connect(self.update_custom_rate_label)
        self.custom_rate_layout.addWidget(self.custom_rate_slider)
        self.custom_rate_layout.addWidget(self.custom_rate_label)
        settings_layout.addLayout(self.custom_rate_layout, 3, 0, 1, 2)

        self.primary_check = QCheckBox(language_manager.get_text('primary_display'))
        settings_layout.addWidget(self.primary_check, 4, 0, 1, 2)

        settings_group.setLayout(settings_layout)
        content_layout.addWidget(settings_group)

        info_group = QGroupBox(self.language_manager.get_text('display_info') or "Информация о дисплее")
        info_layout = QVBoxLayout()
        self.info_label = QLabel("")
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("color: #666; font-size: 12px;")
        info_layout.addWidget(self.info_label)
        info_group.setLayout(info_layout)
        content_layout.addWidget(info_group)

        main_layout.addWidget(content_widget)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        detect_btn = QPushButton(language_manager.get_text('detect_displays'))
        detect_btn.clicked.connect(self.detect_displays)
        detect_btn.setProperty("primary", "true")
        button_layout.addWidget(detect_btn)

        auto_detect_btn = QPushButton(self.language_manager.get_text('auto_detect') or "Автоопределение")
        auto_detect_btn.clicked.connect(self.auto_detect_max_refresh)
        auto_detect_btn.setProperty("secondary", "true")
        button_layout.addWidget(auto_detect_btn)

        button_layout.addStretch()

        apply_btn = QPushButton(language_manager.get_text('apply'))
        apply_btn.clicked.connect(self.apply_display_settings)
        apply_btn.setProperty("primary", "true")
        button_layout.addWidget(apply_btn)

        close_btn = QPushButton(language_manager.get_text('close'))
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

        self.detect_displays()

    def load_current_wallpaper(self):
        startup_path = Path.home() / '.icewm' / 'startup'

        if not startup_path.exists():
            self.current_wallpaper = None
            return

        try:
            for line in startup_path.read_text().split('\n'):
                if 'feh' in line and '--bg-' in line:
                    parts = line.strip().split()
                    for i, part in enumerate(parts):
                        if '--bg-' in part and i + 1 < len(parts):
                            wallpaper_path = parts[i + 1]
                            if Path(wallpaper_path).exists():
                                self.current_wallpaper = {
                                    'path': wallpaper_path,
                                    'mode': part.replace('--bg-', '')
                                }
                            return
        except Exception as e:
            print(f"Error loading wallpaper: {e}")
            self.current_wallpaper = None

    def reapply_wallpaper(self):
        if self.current_wallpaper:
            try:
                subprocess.run(['feh', f'--bg-{self.current_wallpaper["mode"]}',
                              self.current_wallpaper['path']])
                print(f"Wallpaper restored: {self.current_wallpaper['path']}")
            except Exception as e:
                print(f"Error restoring wallpaper: {e}")

    def detect_displays(self):
        try:
            result = subprocess.run(['xrandr'], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            displays = []
            current_display = None

            self.display_data.clear()

            for line in lines:
                if ' connected' in line:
                    current_display = line.split()[0]
                    displays.append(current_display)
                    self.display_data[current_display] = {
                        'modes': [],
                        'current_mode': None,
                        'max_refresh': {}
                    }

                    if '*' in line and 'current' in line:
                        for part in line.split():
                            if 'x' in part and '+' in part:
                                self.display_data[current_display]['current_mode'] = part.split('+')[0]

                elif current_display and line.startswith('   '):
                    parts = line.strip().split()
                    if parts:
                        mode = parts[0]
                        if mode not in self.display_data[current_display]['modes']:
                            self.display_data[current_display]['modes'].append(mode)

                        if len(parts) > 1:
                            for part in parts[1:]:
                                if 'Hz' in part:
                                    try:
                                        rate = float(part.replace('Hz', '').replace('*', '').replace('+', ''))
                                        if mode not in self.display_data[current_display]['max_refresh']:
                                            self.display_data[current_display]['max_refresh'][mode] = rate
                                        elif rate > self.display_data[current_display]['max_refresh'][mode]:
                                            self.display_data[current_display]['max_refresh'][mode] = rate
                                    except:
                                        pass

            self.displays_list.clear()
            for disp in displays:
                item = QListWidgetItem(disp)
                self.displays_list.addItem(item)

            self.displays_list.itemSelectionChanged.connect(self.load_display_options)

            if displays:
                self.displays_list.setCurrentRow(0)
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'), str(e))

    def load_display_options(self):
        if not self.displays_list.currentItem():
            return

        selected = self.displays_list.currentItem().text()

        if selected not in self.display_data:
            return

        self.resolution_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)

        self.resolution_combo.clear()
        if self.display_data[selected]['modes']:
            self.resolution_combo.addItems(self.display_data[selected]['modes'])

            current_mode = self.display_data[selected]['current_mode']
            if current_mode and current_mode in self.display_data[selected]['modes']:
                index = self.display_data[selected]['modes'].index(current_mode)
                self.resolution_combo.setCurrentIndex(index)

        self.update_refresh_rates()

        self.update_display_info()

    def update_refresh_rates(self):
        if not self.displays_list.currentItem():
            return

        selected = self.displays_list.currentItem().text()
        current_res = self.resolution_combo.currentText()

        self.refresh_combo.clear()

        self.refresh_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)

        if current_res in self.display_data[selected]['max_refresh']:
            max_rate = self.display_data[selected]['max_refresh'][current_res]

            standard_rates = [60.00, 75.00, 90.00, 100, 120, 144, 165, 240]
            available_rates = []

            for rate in standard_rates:
                if rate <= max_rate:
                    available_rates.append(str(rate))

            if int(max_rate) not in standard_rates:
                available_rates.append(str(int(max_rate)))

            self.refresh_combo.addItems(available_rates)

            self.refresh_combo.setCurrentText(str(int(max_rate)))

            self.custom_rate_slider.setRange(10, min(240, int(max_rate * 1.2)))
            self.custom_rate_slider.setValue(int(max_rate))
        else:
            self.refresh_combo.addItems(['60.00', '75.00', '120', '144'])
            self.custom_rate_slider.setRange(10, 240)
            self.custom_rate_slider.setValue(60)

    def on_overclock_changed(self, state):
        is_overclock = state == Qt.CheckState.Checked.value
        self.custom_rate_slider.setEnabled(is_overclock)

        if is_overclock:
            self.refresh_combo.setEnabled(False)
        else:
            self.refresh_combo.setEnabled(True)

    def update_custom_rate_label(self, value):
        self.custom_rate_label.setText(f"{value} Hz")
        self.update_display_info()

    def update_display_info(self):
        if not self.displays_list.currentItem():
            return

        selected = self.displays_list.currentItem().text()
        current_res = self.resolution_combo.currentText()

        info_text = ""

        if current_res in self.display_data[selected]['max_refresh']:
            max_rate = self.display_data[selected]['max_refresh'][current_res]
            info_text = f"Максимальная поддерживаемая частота для {current_res}: {max_rate} Hz"

            if self.overclock_check.isChecked():
                custom_rate = self.custom_rate_slider.value()
                if custom_rate > max_rate:
                    info_text += f"\n⚠️ Внимание: выбранная частота {custom_rate} Hz превышает официально поддерживаемую!"

        self.info_label.setText(info_text)

    def auto_detect_max_refresh(self):
        if not self.displays_list.currentItem():
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              "Please select a display first")
            return

        selected = self.displays_list.currentItem().text()
        current_res = self.resolution_combo.currentText()

        if current_res in self.display_data[selected]['max_refresh']:
            max_rate = int(self.display_data[selected]['max_refresh'][current_res])

            self.overclock_check.setChecked(False)

            self.refresh_combo.setCurrentText(str(max_rate))

            QMessageBox.information(self,
                                  self.language_manager.get_text('ok') or "Успех",
                                  f"Автоматически определена максимальная частота: {max_rate} Hz")
        else:
            QMessageBox.warning(self,
                              self.language_manager.get_text('error_title'),
                              "Не удалось определить максимальную частоту для выбранного разрешения")

    def save_original_settings(self):
        if not self.displays_list.currentItem():
            print("Нет выбранного дисплея")
            return

        selected = self.displays_list.currentItem().text()
        try:
            result = subprocess.run(['xrandr'], capture_output=True, text=True)
            lines = result.stdout.splitlines()

            for line in lines:
                if selected in line and ' connected' in line:
                    is_primary = 'primary' in line
                    parts = line.split()

                    current_mode = None
                    for part in parts:
                        if 'x' in part and '+' in part:
                            current_mode = part.split('+')[0]
                            break

                    if not current_mode:
                        print(f"Не нашли разрешение в строке connected для {selected}")
                        return

                    current_rate = "60.00"
                    for part in parts:
                        if 'Hz' in part:
                            rate_str = part.replace('*', '').replace('+', '').replace('Hz', '').strip()
                            if rate_str.replace('.', '').isdigit():
                                current_rate = rate_str
                                break

                    self.original_settings[selected] = {
                        'mode': current_mode,
                        'rate': current_rate,
                        'primary': is_primary
                    }
                    print(f"ОРИГИНАЛ СОХРАНЁН (из connected): {selected} → {current_mode} @ {current_rate} Hz, primary={is_primary}")
                    return

            print(f"Не нашли строку connected для {selected}")

        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def revert_to_original_settings(self):
        if not self.last_applied_settings:
            print("Нет применённых настроек для отката")
            return

        selected = self.last_applied_settings['display']
        if selected not in self.original_settings:
            print(f"Не найдены оригинальные настройки для {selected}")
            print("Текущий original_settings:", self.original_settings)
            return

        original = self.original_settings[selected]
        try:
            cmd = ['xrandr', '--output', selected, '--mode', original['mode'], '--rate', original['rate']]
            if original['primary']:
                cmd.append('--primary')

            print(f"Выполняем откат: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
            self.reapply_wallpaper()
            QMessageBox.information(self, "Успех",
                                    f"Настройки восстановлены: {original['mode']} @ {original['rate']} Hz")
        except Exception as e:
            print(f"Ошибка отката: {e}")
            QMessageBox.critical(self, "Ошибка", f"Не удалось восстановить: {str(e)}")

    def on_timer_tick(self):
        self.revert_time_left -= 1

        if self.revert_time_left <= 0:
            self.revert_timer.stop()
            self.revert_to_original_settings()

    def apply_display_settings(self):
        if not self.displays_list.currentItem():
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              "Please select a display first")
            return

        selected = self.displays_list.currentItem().text()
        res = self.resolution_combo.currentText()

        if self.overclock_check.isChecked():
            rate = str(self.custom_rate_slider.value())
        else:
            rate = self.refresh_combo.currentText()

        self.save_original_settings()

        self.last_applied_settings = {
            'display': selected,
            'mode': res,
            'rate': rate
        }

        cmd = ['xrandr', '--output', selected, '--mode', res, '--rate', rate]

        if self.primary_check.isChecked():
            cmd.extend(['--primary'])

        try:
            if self.overclock_check.isChecked():
                custom_rate = int(rate)
                if selected in self.display_data and res in self.display_data[selected]['max_refresh']:
                    max_rate = self.display_data[selected]['max_refresh'][res]
                    if custom_rate > max_rate:
                        reply = QMessageBox.warning(self,
                                                  "Предупреждение о разгоне",
                                                  f"Выбранная частота {custom_rate} Hz превышает официально поддерживаемую {max_rate} Hz.\n\n"
                                                  "Разгон монитора может привести к:\n"
                                                  "• Артефактам изображения\n"
                                                  "• Повреждению оборудования\n"
                                                  "• Потере гарантии\n\n"
                                                  "Продолжить?",
                                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        if reply == QMessageBox.StandardButton.No:
                            return

            print(f"Applying display settings: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
            self.reapply_wallpaper()

            self.show_confirmation_dialog()

        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"Ошибка применения настроек: {e}\n\n"
                               "Возможно, выбранная частота не поддерживается монитором.")
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'), str(e))

    def show_confirmation_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Подтверждение настроек")
        dialog.setFixedSize(400, 200)
        dialog.setModal(True)
        layout = QVBoxLayout(dialog)

        self.confirmation_timer_label = QLabel("")
        self.confirmation_timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmation_timer_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.confirmation_timer_label)

        info_label = QLabel("Если изображение пропало или появились артефакты,\n"
                            "настройки автоматически вернутся через 15 секунд.\n\n"
                            "Если всё в порядке, нажмите 'Сохранить настройки'.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setWordWrap(True)
        layout.addWidget(info_label)

        button_layout = QHBoxLayout()

        save_btn = QPushButton("Сохранить настройки")
        save_btn.clicked.connect(lambda checked=False: self.on_settings_confirmed(dialog))
        save_btn.setProperty("primary", "true")

        revert_btn = QPushButton("Отменить (Enter)")
        revert_btn.clicked.connect(lambda checked=False: self.on_settings_reverted(dialog))

        revert_btn.setDefault(True)
        revert_btn.setAutoDefault(True)

        button_layout.addWidget(save_btn)
        button_layout.addWidget(revert_btn)
        layout.addLayout(button_layout)

        self.revert_time_left = 15
        self.confirmation_timer = QTimer()
        self.confirmation_timer.timeout.connect(lambda: self.update_confirmation_timer(dialog))
        self.confirmation_timer.start(1000)
        self.update_confirmation_timer(dialog)

        dialog.exec()

    def update_confirmation_timer(self, dialog):
        if self.revert_time_left > 0:
            time_text = f"Обратный отсчёт: {self.revert_time_left} секунд"

            if self.revert_time_left <= 5:
                self.confirmation_timer_label.setStyleSheet(
                    "font-size: 14px; font-weight: bold; color: red;"
                )
            elif self.revert_time_left <= 10:
                self.confirmation_timer_label.setStyleSheet(
                    "font-size: 14px; font-weight: bold; color: orange;"
                )
            else:
                self.confirmation_timer_label.setStyleSheet(
                    "font-size: 14px; font-weight: bold; color: green;"
                )

            self.confirmation_timer_label.setText(time_text)
            self.revert_time_left -= 1
        else:
            self.confirmation_timer.stop()
            self.on_settings_reverted(dialog)

    def on_settings_confirmed(self, dialog):
        self.confirmation_timer.stop()
        dialog.accept()

        QMessageBox.information(self, self.language_manager.get_text('ok'),
                              self.language_manager.get_text('settings_applied'))

    def on_settings_reverted(self, dialog):
        self.confirmation_timer.stop()
        dialog.reject()

        self.revert_to_original_settings()

    def closeEvent(self, event):
        if hasattr(self, 'confirmation_timer'):
            self.confirmation_timer.stop()
        if self.revert_timer.isActive():
            self.revert_timer.stop()
        event.accept()


import os
import subprocess
from pathlib import Path

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class WallpaperSettingsDialog(StyledDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('wallpaper_settings'), language_manager, parent)
        self.setFixedSize(820, 700)
        self.current_wallpaper_info = {}

        self.init_ui()
        self.load_current_wallpaper()
        self.setAcceptDrops(True)

    def init_ui(self):
        lm = self.language_manager
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        #title_label = QLabel(lm.get_text('wallpaper_settings'))
        #title_label.setProperty("title", "true")
        #title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #main_layout.addWidget(title_label)

        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setSpacing(10)

        current_group = QGroupBox(lm.get_text('current_settings'))
        current_layout = QVBoxLayout()
        current_layout.setSpacing(10)

        self.current_wallpaper_preview = QLabel()
        self.current_wallpaper_preview.setFixedSize(350, 200)
        self.current_wallpaper_preview.setStyleSheet("""
            QLabel {
                border: 2px solid #4fc4cf;
                border-radius: 8px;
                background-color: #1a1a2e;
            }
        """)
        self.current_wallpaper_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_wallpaper_preview.setAcceptDrops(True)
        current_layout.addWidget(self.current_wallpaper_preview)

        self.current_wallpaper_label = QLabel()
        self.current_wallpaper_label.setWordWrap(True)
        self.current_wallpaper_label.setStyleSheet("""
            QLabel {
                padding: 12px;
                background-color: #1a1a2e;
                border-radius: 6px;
                border: 1px solid #2d2d4d;
                font-size: 12px;
            }
        """)
        current_layout.addWidget(self.current_wallpaper_label)

        current_group.setLayout(current_layout)
        left_layout.addWidget(current_group)

        adjust_group = QGroupBox(lm.get_text('wallpaper_settings_adjust'))
        adjust_layout = QGridLayout()
        adjust_layout.setSpacing(10)

        adjust_layout.addWidget(QLabel(lm.get_text('wallpaper_mode') + ":"), 0, 0)
        self.current_mode_combo = QComboBox()
        self.current_mode_combo.addItems(['fill', 'center', 'scale', 'max', 'tile'])
        self.current_mode_combo.currentTextChanged.connect(self.update_current_wallpaper_mode)
        self.current_mode_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)
        adjust_layout.addWidget(self.current_mode_combo, 0, 1)

        update_btn = QPushButton(lm.get_text('update_settings'))
        update_btn.clicked.connect(self.apply_current_settings)
        update_btn.setProperty("primary", "true")
        adjust_layout.addWidget(update_btn, 1, 0, 1, 2)

        adjust_group.setLayout(adjust_layout)
        left_layout.addWidget(adjust_group)

        left_layout.addStretch()

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setSpacing(10)

        preview_group = QGroupBox(lm.get_text('wallpaper_preview'))
        preview_layout = QVBoxLayout()
        preview_layout.setSpacing(10)

        self.preview_image = QLabel()
        self.preview_image.setFixedSize(350, 200)
        self.preview_image.setStyleSheet("""
            QLabel {
                border: 2px dashed #4fc4cf;
                border-radius: 8px;
                background-color: #1a1a2e;
                color: #8b8ba7;
                font-size: 14px;
            }
        """)
        self.preview_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_image.setText(lm.get_text('drag_drop_here') + "\n" +
                                  lm.get_text('or_click_browse'))
        self.preview_image.setAcceptDrops(True)
        preview_layout.addWidget(self.preview_image)

        self.preview_label = QLabel()
        self.preview_label.setWordWrap(True)
        self.preview_label.setStyleSheet("""
            QLabel {
                padding: 8px;
                background-color: #1a1a2e;
                border-radius: 6px;
                border: 1px solid #2d2d4d;
                font-size: 12px;
            }
        """)
        preview_layout.addWidget(self.preview_label)

        preview_group.setLayout(preview_layout)
        right_layout.addWidget(preview_group)

        selection_group = QGroupBox(lm.get_text('set_new_wallpaper'))
        selection_layout = QGridLayout()
        selection_layout.setSpacing(10)

        selection_layout.addWidget(QLabel(lm.get_text('wallpaper_path') + ":"), 0, 0)
        self.wallpaper_path = QLineEdit()
        self.wallpaper_path.setPlaceholderText(lm.get_text('select_wallpaper_placeholder'))
        self.wallpaper_path.textChanged.connect(self.update_preview)
        self.wallpaper_path.setAcceptDrops(True)
        selection_layout.addWidget(self.wallpaper_path, 0, 1, 1, 2)

        browse_btn = QPushButton(lm.get_text('browse'))
        browse_btn.clicked.connect(self.browse_wallpaper)
        selection_layout.addWidget(browse_btn, 0, 3)

        selection_layout.addWidget(QLabel(lm.get_text('wallpaper_mode') + ":"), 1, 0)
        self.wallpaper_mode = QComboBox()
        self.wallpaper_mode.addItems(['fill', 'center', 'scale', 'max', 'tile'])
        self.wallpaper_mode.setCurrentText('fill')
        self.wallpaper_mode.currentTextChanged.connect(self.update_preview_info)
        self.wallpaper_mode.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)
        selection_layout.addWidget(self.wallpaper_mode, 1, 1, 1, 3)

        selection_group.setLayout(selection_layout)
        right_layout.addWidget(selection_group)

        hint_label = QLabel(lm.get_text('drag_drop_hint'))
        hint_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                background-color: rgba(79, 196, 207, 0.1);
                border: 1px solid rgba(79, 196, 207, 0.3);
                border-radius: 6px;
                color: #4fc4cf;
                font-size: 12px;
            }
        """)
        hint_label.setWordWrap(True)
        right_layout.addWidget(hint_label)

        right_layout.addStretch()

        main_splitter.addWidget(left_widget)
        main_splitter.addWidget(right_widget)
        main_splitter.setSizes([400, 400])
        main_layout.addWidget(main_splitter)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        preview_btn = QPushButton(lm.get_text('preview'))
        preview_btn.clicked.connect(self.preview_wallpaper)
        button_layout.addWidget(preview_btn)

        button_layout.addStretch()

        apply_btn = QPushButton(lm.get_text('apply'))
        apply_btn.clicked.connect(lambda: self.apply_wallpaper(self.wallpaper_path.text()))
        apply_btn.setProperty("primary", "true")
        button_layout.addWidget(apply_btn)

        remove_btn = QPushButton(lm.get_text('remove_wallpaper'))
        remove_btn.clicked.connect(self.remove_wallpaper)
        button_layout.addWidget(remove_btn)

        close_btn = QPushButton(lm.get_text('close'))
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                file_path = url.toLocalFile()
                if self.is_image_file(file_path):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            image_files = []

            for url in urls:
                file_path = url.toLocalFile()
                if self.is_image_file(file_path):
                    image_files.append(file_path)

            if image_files:
                event.acceptProposedAction()
                file_path = image_files[0]
                self.wallpaper_path.setText(file_path)
                self.update_preview()

                QMessageBox.information(self,
                                      self.language_manager.get_text('file_dropped'),
                                      self.language_manager.get_text('file_dropped_success'))

    def is_image_file(self, file_path):
        if not os.path.exists(file_path):
            return False

        valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.svg']
        ext = os.path.splitext(file_path)[1].lower()

        if ext in valid_extensions:
            return True

        try:
            reader = QImageReader(file_path)
            return reader.canRead()
        except:
            return False

    def browse_wallpaper(self):
        file, _ = QFileDialog.getOpenFileName(
            self, self.language_manager.get_text('select_wallpaper'),
            str(Path.home() / 'Pictures'),
            'Images (*.png *.jpg *.jpeg *.bmp *.gif *.webp);;All Files (*)'
        )
        if file:
            self.wallpaper_path.setText(file)

    def preview_wallpaper(self):
        path = self.wallpaper_path.text()
        mode = self.wallpaper_mode.currentText()

        if not path or not os.path.exists(path):
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              self.language_manager.get_text('invalid_path'))
            return

        try:
            subprocess.Popen(['feh', f'--bg-{mode}', path])
            QMessageBox.information(self, self.language_manager.get_text('preview'),
                                   self.language_manager.get_text('preview_applied'))
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"{self.language_manager.get_text('error_preview')}: {str(e)}")

    def update_current_wallpaper_mode(self, mode):
        pass

    def update_preview(self):
        path = self.wallpaper_path.text()
        if path and os.path.exists(path):
            self.load_preview_image(path, self.preview_image)
            self.update_preview_info()
        else:
            self.preview_image.setText(self.language_manager.get_text('preview_wallpaper_placeholder'))
            self.preview_label.setText("")

    def update_preview_info(self):
        path = self.wallpaper_path.text()
        if path and os.path.exists(path):
            try:
                mode = self.wallpaper_mode.currentText()
                wallpaper_name = Path(path).name
                file_size = os.path.getsize(path) / 1024

                info_text = f"""
                <b>{self.language_manager.get_text('selected_wallpaper')}:</b> {wallpaper_name}<br>
                <b>{self.language_manager.get_text('mode')}:</b> {mode}<br>
                <b>{self.language_manager.get_text('size')}:</b> {file_size:.1f} KB<br>
                <i>{self.language_manager.get_text('preview_note')}</i>
                """
                self.preview_label.setText(info_text)
            except Exception as e:
                print(f"Error getting info: {e}")

    def load_current_wallpaper(self):
        startup_path = Path.home() / '.icewm' / 'startup'

        if not startup_path.exists():
            self.current_wallpaper_label.setText(self.language_manager.get_text('no_wallpaper_set'))
            self.current_wallpaper_preview.setText(self.language_manager.get_text('no_wallpaper_preview'))
            self.current_mode_combo.setEnabled(False)
            return

        try:
            wallpaper_found = False
            for line in startup_path.read_text().split('\n'):
                if 'feh' in line and '--bg-' in line:
                    parts = line.strip().split()
                    for i, part in enumerate(parts):
                        if '--bg-' in part:
                            mode = part.replace('--bg-', '')
                            if i + 1 < len(parts):
                                wallpaper_path = parts[i + 1]
                                if os.path.exists(wallpaper_path):
                                    self.current_wallpaper_info = {
                                        'path': wallpaper_path,
                                        'mode': mode,
                                        'full_command': line.strip()
                                    }

                                    wallpaper_name = Path(wallpaper_path).name
                                    file_size = os.path.getsize(wallpaper_path) / 1024
                                    info_text = f"""
                                    <b>{self.language_manager.get_text('current_wallpaper')}:</b> {wallpaper_name}<br>
                                    <b>{self.language_manager.get_text('path')}:</b> {wallpaper_path}<br>
                                    <b>{self.language_manager.get_text('size')}:</b> {file_size:.1f} KB<br>
                                    <b>{self.language_manager.get_text('mode')}:</b> {mode}
                                    """
                                    self.current_wallpaper_label.setText(info_text)

                                    self.load_preview_image(wallpaper_path, self.current_wallpaper_preview)

                                    self.current_mode_combo.setCurrentText(mode)
                                    self.current_mode_combo.setEnabled(True)

                                    wallpaper_found = True
                                    break

                    if wallpaper_found:
                        break

            if not wallpaper_found:
                self.current_wallpaper_label.setText(self.language_manager.get_text('no_wallpaper_set'))
                self.current_wallpaper_preview.setText(self.language_manager.get_text('no_wallpaper_preview'))
                self.current_mode_combo.setEnabled(False)

        except Exception as e:
            print(f"Error reading startup file: {e}")
            self.current_wallpaper_label.setText(self.language_manager.get_text('no_wallpaper_set'))
            self.current_wallpaper_preview.setText(self.language_manager.get_text('no_wallpaper_preview'))
            self.current_mode_combo.setEnabled(False)

    def load_preview_image(self, image_path, label):
        try:
            reader = QImageReader(image_path)
            reader.setAutoTransform(True)

            size = reader.size()
            if not size.isValid():
                label.setText(self.language_manager.get_text('invalid_image'))
                return

            label_size = label.size()
            size.scale(label_size, Qt.AspectRatioMode.KeepAspectRatio)
            reader.setScaledSize(size)

            image = reader.read()
            if image.isNull():
                label.setText(self.language_manager.get_text('load_error'))
                return

            pixmap = QPixmap.fromImage(image)
            label.setPixmap(pixmap)
            label.setText("")

        except Exception as e:
            print(f"Error loading image: {e}")
            label.setText(self.language_manager.get_text('load_error'))

    def apply_current_settings(self):
        if not self.current_wallpaper_info:
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              self.language_manager.get_text('no_wallpaper_set'))
            return

        try:
            new_mode = self.current_mode_combo.currentText()
            wallpaper_path = self.current_wallpaper_info['path']

            subprocess.run(['feh', f'--bg-{new_mode}', wallpaper_path])

            startup_path = Path.home() / '.icewm' / 'startup'
            if startup_path.exists():
                new_lines = []
                for line in startup_path.read_text().split('\n'):
                    if 'feh' in line and '--bg-' in line and self.current_wallpaper_info['full_command'] in line:
                        new_lines.append(f'feh --bg-{new_mode} {wallpaper_path}')
                    elif line.strip():
                        new_lines.append(line)

                startup_path.write_text('\n'.join(new_lines))

            self.current_wallpaper_info['mode'] = new_mode
            self.current_wallpaper_info['full_command'] = f'feh --bg-{new_mode} {wallpaper_path}'

            QMessageBox.information(self, self.language_manager.get_text('ok'),
                                  self.language_manager.get_text('settings_updated'))

            self.load_current_wallpaper()

        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"{self.language_manager.get_text('error_apply')}: {str(e)}")

    def apply_wallpaper(self, wallpaper_path):
        if not wallpaper_path or not os.path.exists(wallpaper_path):
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              self.language_manager.get_text('invalid_path'))
            return

        mode = self.wallpaper_mode.currentText()
        startup_path = Path.home() / '.icewm' / 'startup'

        subprocess.run(['feh', f'--bg-{mode}', wallpaper_path])

        try:
            new_lines = []
            if startup_path.exists():
                for line in startup_path.read_text().split('\n'):
                    if 'feh' not in line or '--bg-' not in line:
                        new_lines.append(line)

            new_lines.append(f'feh --bg-{mode} {wallpaper_path}')
            startup_path.parent.mkdir(parents=True, exist_ok=True)
            startup_path.write_text('\n'.join(new_lines))

            QMessageBox.information(self, self.language_manager.get_text('ok'),
                                  self.language_manager.get_text('wallpaper_applied'))

            self.wallpaper_path.clear()
            self.preview_image.setText(self.language_manager.get_text('preview_wallpaper_placeholder'))
            self.preview_label.setText("")
            self.load_current_wallpaper()

        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"{self.language_manager.get_text('error_apply')}: {str(e)}")

    def remove_wallpaper(self):
        reply = QMessageBox.question(
            self, self.language_manager.get_text('confirm'),
            self.language_manager.get_text('confirm_remove_wallpaper'),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            startup_path = Path.home() / '.icewm' / 'startup'
            if startup_path.exists():
                lines = [line for line in startup_path.read_text().splitlines()
                        if 'feh' not in line or '--bg-' not in line]
                startup_path.write_text('\n'.join(lines))

            subprocess.run(['feh', '--bg-fill', '#000000'])

            self.current_wallpaper_label.setText(self.language_manager.get_text('no_wallpaper_set'))
            self.current_wallpaper_preview.setText(self.language_manager.get_text('no_wallpaper_preview'))
            self.current_mode_combo.setEnabled(False)
            self.wallpaper_path.clear()
            self.preview_image.setText(self.language_manager.get_text('preview_wallpaper_placeholder'))
            self.preview_label.setText("")

            self.current_wallpaper_info = {}

            QMessageBox.information(self, self.language_manager.get_text('ok'),
                                  self.language_manager.get_text('wallpaper_removed'))

        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"{self.language_manager.get_text('error_remove_wallpaper')}: {str(e)}")

class MouseTouchpadDialog(StyledDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('mouse_touchpad'), language_manager, parent)
        self.setFixedSize(600, 400)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel(language_manager.get_text('mouse_touchpad'))
        title_label.setProperty("title", "true")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        mouse_group = QGroupBox("Mouse Settings")
        mouse_layout = QGridLayout()
        mouse_layout.setSpacing(15)

        mouse_layout.addWidget(QLabel(language_manager.get_text('mouse_speed') + ":"), 0, 0)
        self.mouse_speed = QSpinBox()
        self.mouse_speed.setRange(1, 20)
        self.mouse_speed.setValue(10)
        mouse_layout.addWidget(self.mouse_speed, 0, 1)

        mouse_layout.addWidget(QLabel(language_manager.get_text('mouse_accel') + ":"), 1, 0)
        self.mouse_accel = QSpinBox()
        self.mouse_accel.setRange(1, 10)
        self.mouse_accel.setValue(3)
        mouse_layout.addWidget(self.mouse_accel, 1, 1)

        mouse_group.setLayout(mouse_layout)
        content_layout.addWidget(mouse_group)

        touchpad_group = QGroupBox("Touchpad Settings")
        touchpad_layout = QVBoxLayout()
        touchpad_layout.setSpacing(10)

        self.tap_check = QCheckBox(language_manager.get_text('tap_to_click'))
        touchpad_layout.addWidget(self.tap_check)

        self.touchpad_status = QLabel()
        self.touchpad_status.setStyleSheet("""
            QLabel {
                padding: 10px;
                background-color: rgba(79, 196, 207, 0.1);
                border-radius: 6px;
                border: 1px solid rgba(79, 196, 207, 0.3);
            }
        """)
        touchpad_layout.addWidget(self.touchpad_status)

        touchpad_group.setLayout(touchpad_layout)
        content_layout.addWidget(touchpad_group)

        main_layout.addWidget(content_widget)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        button_layout.addStretch()

        apply_btn = QPushButton(language_manager.get_text('apply'))
        apply_btn.clicked.connect(self.apply_mouse_settings)
        apply_btn.setProperty("primary", "true")
        button_layout.addWidget(apply_btn)

        close_btn = QPushButton(language_manager.get_text('close'))
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

        self.detect_touchpad()

    def detect_touchpad(self):
        try:
            result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
            if 'touchpad' in result.stdout.lower():
                self.touchpad_status.setText(
                    self.language_manager.get_text('touchpad_detected')
                )
                self.tap_check.setEnabled(True)
            else:
                self.touchpad_status.setText(
                    self.language_manager.get_text('no_touchpad')
                )
                self.tap_check.setEnabled(False)
        except Exception as e:
            self.touchpad_status.setText(
                self.language_manager.get_text('error_unknown') + f": {e}"
            )


    def apply_mouse_settings(self):
        speed = self.mouse_speed.value()
        accel = self.mouse_accel.value()
        try:
            subprocess.run(['xset', 'm', f'{accel}/1', str(speed)], check=True)
            if self.tap_check.isEnabled() and self.tap_check.isChecked():
                touchpad_id = self.get_touchpad_id()
                if touchpad_id:
                    subprocess.run(['xinput', 'set-prop', touchpad_id, 'libinput Tapping Enabled', '1'], check=True)
            QMessageBox.information(self, self.language_manager.get_text('ok'),
                                  self.language_manager.get_text('settings_applied'))
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'), str(e))

    def get_touchpad_id(self):
        result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if 'touchpad' in line.lower():
                return line.split('id=')[1].split()[0]
        return None

class ThemeSettingsDialog(StyledDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('theme_settings'), language_manager, parent)
        self.setFixedSize(700, 500)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel(language_manager.get_text('theme_settings'))
        title_label.setProperty("title", "true")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        themes_group = QGroupBox(language_manager.get_text('theme_select'))
        themes_layout = QVBoxLayout()

        self.themes_list = QListWidget()
        self.themes_list.setFixedHeight(300)
        themes_layout.addWidget(self.themes_list)

        themes_group.setLayout(themes_layout)
        main_layout.addWidget(themes_group)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        button_layout.addStretch()

        apply_btn = QPushButton(language_manager.get_text('apply'))
        apply_btn.clicked.connect(self.apply_theme)
        apply_btn.setProperty("primary", "true")
        button_layout.addWidget(apply_btn)

        close_btn = QPushButton(language_manager.get_text('close'))
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

        self.load_themes()

    def load_themes(self):
        theme_dirs = [Path('/usr/share/icewm/themes'), Path.home() / '.icewm' / 'themes']
        for dir_path in theme_dirs:
            if dir_path.exists():
                for theme in dir_path.iterdir():
                    if theme.is_dir():
                        self.themes_list.addItem(theme.name)

    def apply_theme(self):
        selected = self.themes_list.currentItem()
        if not selected:
            QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                              "Please select a theme first")
            return

        theme_name = selected.text()
        theme_file = Path.home() / '.icewm' / 'theme'
        theme_file.parent.mkdir(exist_ok=True)
        theme_file.write_text(f'Theme="{theme_name}/default.theme"\n')

        try:
            subprocess.run(['icewm', '--restart'], check=True)
            QMessageBox.information(self, self.language_manager.get_text('ok'),
                                  self.language_manager.get_text('theme_applied'))
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"{self.language_manager.get_text('error_theme')}: {str(e)}")

class RedshiftSettingsDialog(StyledDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('redshift_settings'), language_manager, parent)
        self.setFixedSize(600, 450)
        self.redshift_process = None
        self.current_temperature = 6500
        self.is_enabled = False

        self.redshift_available = self.check_redshift_available()

        self.init_ui()
        self.load_current_settings()

    def check_redshift_available(self):
        try:
            result = subprocess.run(['which', 'redshift'], capture_output=True, text=True)
            return result.returncode == 0
        except:
            return False

    def init_ui(self):
        lm = self.language_manager

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        #title_label = QLabel(lm.get_text('redshift_settings'))
        #title_label.setProperty("title", "true")
        #title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #main_layout.addWidget(title_label)

        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)
        status_layout.setContentsMargins(10, 10, 10, 10)

        self.status_indicator = QLabel("●")
        self.status_indicator.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 5px;
            }
        """)
        status_layout.addWidget(self.status_indicator)

        self.status_label = QLabel()
        self.status_label.setStyleSheet("font-size: 14px;")
        status_layout.addWidget(self.status_label)
        status_layout.addStretch()

        main_layout.addWidget(status_widget)

        settings_group = QGroupBox(lm.get_text('display_settings'))
        settings_layout = QVBoxLayout()
        settings_layout.setSpacing(15)

        self.enable_check = QCheckBox(lm.get_text('enable_redshift'))
        self.enable_check.stateChanged.connect(self.on_enable_changed)
        settings_layout.addWidget(self.enable_check)

        temp_layout = QHBoxLayout()
        temp_layout.addWidget(QLabel(lm.get_text('color_temperature') + ":"))

        self.temp_label = QLabel("6500K")
        self.temp_label.setMinimumWidth(60)
        temp_layout.addWidget(self.temp_label)

        self.temp_slider = QSlider(Qt.Orientation.Horizontal)
        self.temp_slider.setRange(1000, 6500)
        self.temp_slider.setValue(6500)
        self.temp_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.temp_slider.setTickInterval(500)
        self.temp_slider.valueChanged.connect(self.on_temperature_changed)
        temp_layout.addWidget(self.temp_slider)

        settings_layout.addLayout(temp_layout)

        presets_group = QGroupBox(lm.get_text('temperature_presets'))
        presets_layout = QHBoxLayout()

        presets = [
            ("6500K (Дневной)", 6500, "#FFE4B5"),
            ("5500K (Утренний)", 5500, "#FFD39B"),
            ("4500K (Вечерний)", 4500, "#FFB6C1"),
            ("3500K (Ночной)", 3500, "#FFA07A"),
            ("2500K (Теплый)", 2500, "#FF8C69")
        ]

        for name, temp, color in presets:
            btn = QPushButton(name)
            btn.setStyleSheet(f"background-color: {color}; color: black; padding: 8px; border-radius: 4px;")
            btn.clicked.connect(lambda checked, t=temp: self.set_temperature_preset(t))
            presets_layout.addWidget(btn)

        presets_group.setLayout(presets_layout)
        settings_layout.addWidget(presets_group)

        #auto_group = QGroupBox(lm.get_text('auto_mode'))
        #auto_layout = QVBoxLayout()

        #self.auto_mode_check = QCheckBox(lm.get_text('enable_auto_mode'))
        #auto_layout.addWidget(self.auto_mode_check)

        #self.location_layout = QHBoxLayout()
        #self.location_layout.addWidget(QLabel(lm.get_text('location') + ":"))

        #self.lat_input = QLineEdit()
        #self.lat_input.setPlaceholderText(lm.get_text('latitude_placeholder'))
        #self.lat_input.setValidator(self.create_coordinate_validator())
        #self.location_layout.addWidget(self.lat_input)

        #self.lon_input = QLineEdit()
        #self.lon_input.setPlaceholderText(lm.get_text('longitude_placeholder'))
        #self.lon_input.setValidator(self.create_coordinate_validator())
        #self.location_layout.addWidget(self.lon_input)

        #auto_layout.addLayout(self.location_layout)

        #detect_btn = QPushButton(lm.get_text('detect_location'))
        #detect_btn.clicked.connect(self.detect_location)
        #auto_layout.addWidget(detect_btn)

        #auto_group.setLayout(auto_layout)
        #settings_layout.addWidget(auto_group)

        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        main_layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.apply_btn = QPushButton(lm.get_text('apply'))
        self.apply_btn.clicked.connect(self.apply_redshift_settings)
        self.apply_btn.setProperty("primary", "true")
        button_layout.addWidget(self.apply_btn)

        self.stop_btn = QPushButton(lm.get_text('stop_redshift'))
        self.stop_btn.clicked.connect(self.stop_redshift)
        button_layout.addWidget(self.stop_btn)

        button_layout.addStretch()

        close_btn = QPushButton(lm.get_text('close'))
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

        self.update_status()

    def create_coordinate_validator(self):
        return QDoubleValidator(-180, 180, 6)

    def on_enable_changed(self, state):
        enabled = state == Qt.CheckState.Checked.value
        self.temp_slider.setEnabled(enabled)
        self.apply_btn.setEnabled(enabled)

    def on_temperature_changed(self, value):
        self.current_temperature = value
        self.temp_label.setText(f"{value}K")

        color = self.temperature_to_color(value)
        self.temp_label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-weight: bold;
                font-size: 14px;
            }}
        """)

    def temperature_to_color(self, temp):
        if temp >= 6000:
            return "#FFE4B5"
        elif temp >= 5000:
            return "#FFD39B"
        elif temp >= 4000:
            return "#FFB6C1"
        elif temp >= 3000:
            return "#FFA07A"
        else:
            return "#FF8C69"

    def set_temperature_preset(self, temperature):
        self.temp_slider.setValue(temperature)
        self.current_temperature = temperature

    def detect_location(self):
        try:
            import requests
            response = requests.get('http://ip-api.com/json/', timeout=5)
            if response.status_code == 200:
                data = response.json()
                lat = data.get('lat', 0)
                lon = data.get('lon', 0)

                self.lat_input.setText(str(round(lat, 4)))
                self.lon_input.setText(str(round(lon, 4)))

                QMessageBox.information(self, self.language_manager.get_text('ok'),
                                      f"Location detected: {data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}")
            else:
                QMessageBox.warning(self, self.language_manager.get_text('error_title'),
                                  "Could not detect location automatically")
        except Exception as e:
            QMessageBox.critical(self, self.language_manager.get_text('error_title'),
                               f"Error detecting location: {str(e)}")

    def load_current_settings(self):
        try:
            result = subprocess.run(['pgrep', '-f', 'redshift'], capture_output=True, text=True)
            if result.returncode == 0:
                self.is_enabled = True
                result = subprocess.run(['pkill', '-USR1', 'redshift'], capture_output=True, text=True)

                self.current_temperature = 6500
        except:
            self.is_enabled = False

        self.update_status()

    def update_status(self):
        if not self.redshift_available:
            self.status_indicator.setStyleSheet("color: red;")
            self.status_label.setText(self.language_manager.get_text('redshift_not_installed'))
            self.enable_check.setEnabled(False)
            return

        if self.is_enabled:
            self.status_indicator.setStyleSheet("color: green;")
            self.status_label.setText(self.language_manager.get_text('redshift_running'))
            self.enable_check.setChecked(True)
        else:
            self.status_indicator.setStyleSheet("color: orange;")
            self.status_label.setText(self.language_manager.get_text('redshift_stopped'))
            self.enable_check.setChecked(False)

    def apply_redshift_settings(self):
        try:
            if not self.enable_check.isChecked():
                self.is_enabled = False
                self.update_status()
                QMessageBox.information(
                    self,
                    self.language_manager.get_text('ok'),
                    self.language_manager.get_text('redshift_disabled')
                )
                return
            self.stop_redshift()

            cmd = ['redshift']

            cmd.extend(['-O', str(self.current_temperature), '&'])

            self.redshift_process = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            self.is_enabled = True
            self.update_status()

            QMessageBox.information(
                self,
                self.language_manager.get_text('ok'),
                self.language_manager.get_text('redshift_applied')
            )

        except Exception as e:
            self.is_enabled = False
            self.update_status()
            QMessageBox.critical(
                self,
                self.language_manager.get_text('error_title'),
                f"{self.language_manager.get_text('error_redshift')}: {str(e)}"
            )


    def stop_redshift(self):
        try:
            subprocess.run(['redshift', '-x'], capture_output=True)
            if self.redshift_process:
                self.redshift_process.terminate()
                self.redshift_process.wait()
                self.redshift_process = None

            self.is_enabled = False
            self.update_status()
        except:
            pass

    def closeEvent(self, event):
        print('close_exent')
        #event.accept()


from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QInputDialog
)
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtGui import QKeyEvent, QKeySequence


class KeyboardSettingsDialog(StyledDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(language_manager.get_text('keyboard_settings'), language_manager, parent)
        self.setFixedSize(880, 680)
        self.lm = language_manager

        self.switch_technical_options = [
            "grp:alt_shift_toggle",
            "grp:ctrl_shift_toggle",
            "grp:win_space_toggle",
            "grp:lwin_toggle"
        ]

        self.keybindings = []

        self.init_ui()
        self.load_current_layouts()
        self.load_keybindings()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(24, 24, 24, 24)

        layouts_group = QGroupBox(self.lm.get_text('keyboard_layouts'))
        layouts_group.setStyleSheet(f"""
            QGroupBox {{
                color: {COLORS['accent']['blue']};
                font-weight: bold;
                font-size: 15px;
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 10px;
                margin-top: 14px;
                padding-top: 14px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 16px;
                padding: 0 10px;
            }}
        """)

        layouts_layout = QGridLayout()
        layouts_layout.setSpacing(14)

        layouts_layout.addWidget(QLabel(self.lm.get_text('primary_layout') + ":"), 0, 0)
        self.primary_combo = QComboBox()
        self.primary_combo.addItems(self.get_available_layouts())
        self.primary_combo.setMinimumWidth(220)
        self.primary_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)
        layouts_layout.addWidget(self.primary_combo, 0, 1, 1, 2)

        layouts_layout.addWidget(QLabel(self.lm.get_text('additional_layouts') + ":"), 1, 0)
        self.additional_list = QListWidget()
        self.additional_list.setFixedHeight(140)
        self.additional_list.setStyleSheet(f"""
            QListWidget {{
                background: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
                padding: 6px;
            }}
            QListWidget::item {{
                padding: 8px 10px;
            }}
            QListWidget::item:selected {{
                background: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)
        layouts_layout.addWidget(self.additional_list, 1, 1, 4, 1)

        add_layout_btn = QPushButton(self.lm.get_text('add_layout'))
        add_layout_btn.clicked.connect(self.add_layout)
        add_layout_btn.setFixedWidth(150)
        layouts_layout.addWidget(add_layout_btn, 1, 2)

        remove_layout_btn = QPushButton(self.lm.get_text('remove_layout'))
        remove_layout_btn.clicked.connect(self.remove_selected_layout)
        remove_layout_btn.setFixedWidth(150)
        layouts_layout.addWidget(remove_layout_btn, 2, 2)

        layouts_layout.addWidget(QLabel(self.lm.get_text('switch_shortcut') + ":"), 5, 0)
        self.switch_combo = QComboBox()
        switch_names = [
            "Alt + Shift",
            "Ctrl + Shift",
            "Win + Пробел",
            "Левая Win"
        ]
        self.switch_combo.addItems(switch_names)
        self.switch_combo.setCurrentIndex(0)
        self.switch_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px 24px 5px 8px;
                min-width: 150px;
                font-size: 13px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
            QComboBox::drop-down {{
                width: 24px;
                border-left: 1px solid {COLORS['misc']['border']};
                background: {COLORS['primary']['medium']};
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                selection-background-color: {COLORS['accent']['blue']};
                selection-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 6px;
                border-radius: 4px;
                border-bottom: 1px solid {COLORS['misc']['border']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {COLORS['primary']['light']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {COLORS['accent']['blue']};
                color: {COLORS['primary']['dark']};
            }}
        """)
        layouts_layout.addWidget(self.switch_combo, 5, 1, 1, 2)

        apply_layouts_btn = QPushButton(self.lm.get_text('apply_layouts'))
        apply_layouts_btn.clicked.connect(self.apply_layouts)
        apply_layouts_btn.setProperty("primary", "true")
        apply_layouts_btn.setMinimumHeight(44)
        layouts_layout.addWidget(apply_layouts_btn, 6, 0, 1, 3)

        layouts_group.setLayout(layouts_layout)
        main_layout.addWidget(layouts_group)

        kb_group = QGroupBox(self.lm.get_text('keybindings'))
        kb_group.setStyleSheet(layouts_group.styleSheet())
        kb_layout = QVBoxLayout()
        kb_layout.setSpacing(14)

        self.kb_table = QTableWidget(0, 2)
        self.kb_table.setHorizontalHeaderLabels([
            self.lm.get_text('shortcut'),
            self.lm.get_text('command')
        ])
        self.kb_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.kb_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.kb_table.setStyleSheet(f"""
            QTableWidget {{
                background: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                gridline-color: {COLORS['misc']['border']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
            }}
            QHeaderView::section {{
                background: {COLORS['primary']['light']};
                color: {COLORS['text']['primary']};
                padding: 10px;
                border: none;
            }}
        """)
        kb_layout.addWidget(self.kb_table)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        add_kb = QPushButton(self.lm.get_text('add'))
        edit_kb = QPushButton(self.lm.get_text('edit'))
        remove_kb = QPushButton(self.lm.get_text('remove'))

        for b in [add_kb, edit_kb, remove_kb]:
            b.setFixedWidth(150)

        apply_kb_btn = QPushButton(self.lm.get_text('apply_keybindings'))
        apply_kb_btn.clicked.connect(self.apply_keybindings)
        apply_kb_btn.setProperty("primary", "true")
        apply_kb_btn.setMinimumHeight(44)

        btn_layout.addWidget(add_kb)
        btn_layout.addWidget(edit_kb)
        btn_layout.addWidget(remove_kb)
        btn_layout.addStretch()
        btn_layout.addWidget(apply_kb_btn)

        add_kb.clicked.connect(self.add_keybinding)
        edit_kb.clicked.connect(self.edit_keybinding)
        remove_kb.clicked.connect(self.remove_keybinding)

        kb_layout.addLayout(btn_layout)
        kb_group.setLayout(kb_layout)
        main_layout.addWidget(kb_group)

        bottom = QHBoxLayout()
        bottom.addStretch()
        close_btn = QPushButton(self.lm.get_text('close'))
        close_btn.clicked.connect(self.close)
        bottom.addWidget(close_btn)
        main_layout.addLayout(bottom)

    def get_available_layouts(self):
        return ['us', 'ru', 'ua', 'de', 'fr', 'es', 'gb', 'it', 'pl', 'tr', 'jp', 'kr', 'cn']

    def load_current_layouts(self):
        try:
            result = subprocess.run(['setxkbmap', '-query'], capture_output=True, text=True, check=True)
            lines = result.stdout.splitlines()

            for line in lines:
                if line.startswith('layout:'):
                    layouts = line.split(':', 1)[1].strip().split(',')
                    if layouts:
                        self.primary_combo.setCurrentText(layouts[0].strip())
                        for lay in layouts[1:]:
                            self.additional_list.addItem(lay.strip())

                elif line.startswith('options:'):
                    options = line.split(':', 1)[1].strip().split(',')
                    for opt in options:
                        if opt.startswith('grp:'):
                            try:
                                idx = self.switch_technical_options.index(opt)
                                self.switch_combo.setCurrentIndex(idx)
                            except ValueError:
                                pass
        except Exception as e:
            QMessageBox.warning(self, self.lm.get_text('error_title'),
                                f"{self.lm.get_text('error_unknown')}: {str(e)}")

    def add_layout(self):
        dlg = QInputDialog(self)
        dlg.setWindowTitle(self.lm.get_text('add_layout'))
        dlg.setLabelText(self.lm.get_text('keyboard_layouts') + ":")
        dlg.setComboBoxItems(self.get_available_layouts())

        combo = dlg.findChild(QComboBox)
        if combo:
            combo.setStyleSheet(f"""
                QComboBox {{
                    background-color: {COLORS['primary']['medium']};
                    color: {COLORS['text']['primary']};
                    border: 1px solid {COLORS['misc']['border']};
                    border-radius: 6px;
                    padding: 5px 24px 5px 8px;
                    min-width: 150px;
                    font-size: 13px;
                    selection-background-color: {COLORS['accent']['blue']};
                }}
                QComboBox::drop-down {{
                    width: 24px;
                    border-left: 1px solid {COLORS['misc']['border']};
                    background: {COLORS['primary']['medium']};
                }}
                QComboBox::down-arrow {{
                    image: none;
                    border-left: 4px solid transparent;
                    border-right: 4px solid transparent;
                    border-top: 4px solid {COLORS['text']['secondary']};
                    width: 0px;
                    height: 0px;
                    margin-right: 8px;
                }}
                QComboBox QAbstractItemView {{
                    background-color: {COLORS['primary']['medium']};
                    color: {COLORS['text']['primary']};
                    selection-background-color: {COLORS['accent']['blue']};
                    selection-color: {COLORS['primary']['dark']};
                    border: 1px solid {COLORS['misc']['border']};
                    padding: 4px;
                    outline: none;
                }}
                QComboBox QAbstractItemView::item {{
                    padding: 6px;
                    border-radius: 4px;
                    border-bottom: 1px solid {COLORS['misc']['border']};
                }}
                QComboBox QAbstractItemView::item:hover {{
                    background-color: {COLORS['primary']['light']};
                }}
                QComboBox QAbstractItemView::item:selected {{
                    background-color: {COLORS['accent']['blue']};
                    color: {COLORS['primary']['dark']};
                }}
            """)

        if dlg.exec() == QDialog.DialogCode.Accepted:
            layout = dlg.textValue()
            if layout:
                items = [self.additional_list.item(i).text() for i in range(self.additional_list.count())]
                if layout not in items:
                    self.additional_list.addItem(layout)



    def remove_selected_layout(self):
        for item in self.additional_list.selectedItems():
            self.additional_list.takeItem(self.additional_list.row(item))

    def apply_layouts(self):
        primary = self.primary_combo.currentText()
        additional = [self.additional_list.item(i).text() for i in range(self.additional_list.count())]
        all_layouts = [primary] + additional

        if not all_layouts:
            QMessageBox.warning(self, self.lm.get_text('error_title'),
                                self.lm.get_text('select_layout_first', default="Выберите хотя бы одну раскладку"))
            return

        switch_idx = self.switch_combo.currentIndex()
        switch_opt = self.switch_technical_options[switch_idx]

        cmd = ['setxkbmap', '-layout', ','.join(all_layouts)]
        if switch_opt:
            cmd += ['-option', switch_opt]

        try:
            subprocess.run(cmd, check=True)

            startup = Path.home() / '.icewm' / 'startup'
            lines = startup.read_text().splitlines() if startup.exists() else []
            new_lines = [l for l in lines if not l.strip().startswith('setxkbmap')]
            new_lines.append(' '.join(cmd))
            startup.parent.mkdir(parents=True, exist_ok=True)
            startup.write_text('\n'.join(new_lines) + '\n')

            QMessageBox.information(self, self.lm.get_text('ok'),
                                    self.lm.get_text('settings_applied'))
        except Exception as e:
            QMessageBox.critical(self, self.lm.get_text('error_title'),
                                 f"{self.lm.get_text('error_apply')}: {str(e)}")

    def load_keybindings(self):
        path = Path.home() / '.icewm' / 'keys'
        self.keybindings.clear()

        if not path.exists():
            return

        try:
            for line in path.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('key "'):
                    parts = line[5:].split('"', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        command = parts[1].strip()
                        self.keybindings.append({'key': key, 'command': command})
        except Exception as e:
            print("Ошибка чтения keys:", e)

        self.update_kb_table()

    def update_kb_table(self):
        self.kb_table.setRowCount(len(self.keybindings))
        for row, binding in enumerate(self.keybindings):
            self.kb_table.setItem(row, 0, QTableWidgetItem(binding['key']))
            self.kb_table.setItem(row, 1, QTableWidgetItem(binding['command']))

    def add_keybinding(self):
        dlg = ShortcutRecordDialog(self.lm, self)
        if dlg.exec() != QDialog.DialogCode.Accepted or not dlg.recorded:
            return

        cmd, ok = QInputDialog.getText(
            self,
            self.lm.get_text('add'),
            self.lm.get_text('command') + ":"
        )

        if ok and cmd.strip():
            self.keybindings.append({
                'key': dlg.recorded,
                'command': cmd.strip()
            })
            self.update_kb_table()


    def edit_keybinding(self):
        row = self.kb_table.currentRow()
        if row < 0:
            QMessageBox.warning(
                self,
                self.lm.get_text('error_title'),
                self.lm.get_text(
                    'select_row',
                    default="Выберите сочетание для редактирования"
                )
            )
            return

        dlg = ShortcutRecordDialog(self.lm, self)
        dlg.preview.setText(self.keybindings[row]['key'])

        if dlg.exec() != QDialog.DialogCode.Accepted:
            return

        new_key = dlg.recorded or self.keybindings[row]['key']

        cmd, ok = QInputDialog.getText(
            self,
            self.lm.get_text('edit'),
            self.lm.get_text('command') + ":",
            text=self.keybindings[row]['command']
        )

        if ok:
            self.keybindings[row] = {
                'key': new_key,
                'command': cmd.strip()
            }
            self.update_kb_table()


    def remove_keybinding(self):
        row = self.kb_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, self.lm.get_text('error_title'),
                                "Выберите строку для удаления")
            return

        del self.keybindings[row]
        self.update_kb_table()

    def apply_keybindings(self):
        path = Path.home() / '.icewm' / 'keys'
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write("# Горячие клавиши IceWM — изменено через EN-OS Settings manager\n\n")
                for b in self.keybindings:
                    f.write(f'key "{b["key"]}" {b["command"]}\n')

            subprocess.run(['icewm', '--restart'], check=True, timeout=8)
            QMessageBox.information(self, self.lm.get_text('ok'),
                                    self.lm.get_text('settings_applied'))
        except Exception as e:
            QMessageBox.critical(self, self.lm.get_text('error_title'),
                                 f"{self.lm.get_text('error_apply')}\n{str(e)}")


class ShortcutRecordDialog(QDialog):
    def __init__(self, language_manager, parent=None):
        super().__init__(parent)
        self.lm = language_manager
        self.recorded = None

        self.setWindowTitle(self.lm.get_text(
            'record_shortcut'
        ))
        self.setFixedSize(440, 180)

        self.setStyleSheet(f"""
            QDialog {{
                background: {COLORS['primary']['dark']};
                color: {COLORS['text']['primary']};
            }}
            QLabel {{
                font-size: 14px;
            }}
            QLineEdit {{
                background: {COLORS['primary']['medium']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
                padding: 10px;
                font-size: 15px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(14)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel(self.lm.get_text(
            'press_shortcut',
        ))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hint = QLabel(self.lm.get_text(
            'shortcut_hint',
        ))
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hint.setStyleSheet("opacity: 0.7; font-size: 12px;")

        self.preview = QLineEdit()
        self.preview.setReadOnly(True)
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btns = QHBoxLayout()
        cancel = QPushButton(self.lm.get_text('cancel'))
        ok = QPushButton(self.lm.get_text('ok'))
        ok.setEnabled(False)
        ok.setProperty("primary", "true")

        btns.addStretch()
        btns.addWidget(cancel)
        btns.addWidget(ok)

        layout.addWidget(title)
        layout.addWidget(hint)
        layout.addWidget(self.preview)
        layout.addLayout(btns)

        cancel.clicked.connect(self.reject)
        ok.clicked.connect(self.accept)

        self._ok_btn = ok

    def keyPressEvent(self, event: QKeyEvent):
        if event.isAutoRepeat():
            return

        ignore = {
            Qt.Key.Key_Control,
            Qt.Key.Key_Shift,
            Qt.Key.Key_Alt,
            Qt.Key.Key_Meta
        }
        if event.key() in ignore:
            return

        parts = []

        mods = event.modifiers()
        if mods & Qt.KeyboardModifier.ControlModifier:
            parts.append("Ctrl")
        if mods & Qt.KeyboardModifier.AltModifier:
            parts.append("Alt")
        if mods & Qt.KeyboardModifier.ShiftModifier:
            parts.append("Shift")
        if mods & Qt.KeyboardModifier.MetaModifier:
            parts.append("Super")

        key = QKeySequence(event.key()).toString()
        if not key:
            return

        parts.append(key)
        combo = "+".join(parts)

        self.recorded = combo
        self.preview.setText(combo)
        self._ok_btn.setEnabled(True)


class IceWMSettingsManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language_manager = LanguageManager()

        self.setWindowTitle(self.language_manager.get_text('app_title'))
        self.setFixedSize(900, 700)

        self.load_fonts()
        self.set_modern_theme()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 15)
        main_layout.setSpacing(15)

        self.create_header(main_layout)
        self.create_main_page(main_layout)
        main_layout.addStretch()
        self.create_footer(main_layout)

    def create_header(self, parent_layout):
        header_layout = QHBoxLayout()

        self.header_label = QLabel(self.language_manager.get_text('header'))
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet(f"""
            QLabel {{
                color: {COLORS['accent']['blue']};
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                background-color: {COLORS['primary']['dark']};
                border-radius: 12px;
                border: 1px solid {COLORS['misc']['border']};
            }}
        """)
        self.header_label.setMinimumHeight(60)

        language_layout = QHBoxLayout()
        language_layout.setSpacing(8)

        self.language_combo = QComboBox()
        self.language_combo.addItem("EN", 'en')
        self.language_combo.addItem("RU", 'ru')
        self.language_combo.addItem("ES", 'es')
        self.language_combo.addItem("FR", 'fr')
        self.language_combo.addItem("DE", 'de')
        self.language_combo.addItem("简体中文", 'zh_CN')
        self.language_combo.addItem("日本語", 'ja')
        self.language_combo.addItem("한국어", 'ko')

        current_lang_code = {
            'en': "EN",
            'ru': "RU",
            'es': "ES",
            'fr': "FR",
            'de': "DE",
            'zh_CN': "简体中文",
            'ja': "日本語",
            'ko': "한국어",
        }.get(self.language_manager.current_language, "EN")
        self.language_combo.setCurrentText(current_lang_code)

        self.language_combo.currentIndexChanged.connect(self.on_language_changed)
        self.language_combo.setFixedSize(70, 35)
        self.language_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                padding: 5px;
                font-size: 12px;
                font-weight: bold;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 15px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid {COLORS['text']['secondary']};
                width: 0px;
                height: 0px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['primary']['medium']};
                color: {COLORS['text']['primary']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 6px;
                selection-background-color: {COLORS['accent']['blue']};
            }}
        """)

        language_layout.addWidget(self.language_combo)

        header_layout.addWidget(self.header_label)
        header_layout.addLayout(language_layout)

        parent_layout.addLayout(header_layout)

    def create_main_page(self, parent_layout):
        cards_layout = QGridLayout()
        cards_layout.setSpacing(12)

        self.display_card = ModernCard(
            self.language_manager.get_text('display_settings'),
            self.language_manager.get_text('display_desc')
        )
        self.display_card.mousePressEvent = lambda e: self.open_display_settings()
        self.display_card.setCursor(Qt.CursorShape.PointingHandCursor)

        self.wallpaper_card = ModernCard(
            self.language_manager.get_text('wallpaper_settings'),
            self.language_manager.get_text('wallpaper_desc')
        )
        self.wallpaper_card.mousePressEvent = lambda e: self.open_wallpaper_settings()
        self.wallpaper_card.setCursor(Qt.CursorShape.PointingHandCursor)

        self.mouse_card = ModernCard(
            self.language_manager.get_text('mouse_touchpad'),
            self.language_manager.get_text('mouse_touchpad_desc')
        )
        self.mouse_card.mousePressEvent = lambda e: self.open_mouse_settings()
        self.mouse_card.setCursor(Qt.CursorShape.PointingHandCursor)

        self.theme_card = ModernCard(
            self.language_manager.get_text('theme_settings'),
            self.language_manager.get_text('theme_desc')
        )
        self.theme_card.mousePressEvent = lambda e: self.open_theme_settings()
        self.theme_card.setCursor(Qt.CursorShape.PointingHandCursor)

        self.redshift_card = ModernCard(
            self.language_manager.get_text('redshift_settings'),
            "Adjust screen color temperature for night viewing"
        )
        self.redshift_card.mousePressEvent = lambda e: self.open_redshift_settings()
        self.redshift_card.setCursor(Qt.CursorShape.PointingHandCursor)

        self.keyboard_card = ModernCard(
        self.language_manager.get_text('keyboard_settings'),"Configure keyboard layouts and shortcuts")
        self.keyboard_card.mousePressEvent = lambda e: self.open_keyboard_settings()
        self.keyboard_card.setCursor(Qt.CursorShape.PointingHandCursor)

        cards_layout.addWidget(self.keyboard_card, 2, 1)
        cards_layout.addWidget(self.redshift_card, 2, 0)
        cards_layout.addWidget(self.display_card, 0, 0)
        cards_layout.addWidget(self.wallpaper_card, 0, 1)
        cards_layout.addWidget(self.mouse_card, 1, 0)
        cards_layout.addWidget(self.theme_card, 1, 1)

        parent_layout.addLayout(cards_layout)

    def open_redshift_settings(self):
            dlg = RedshiftSettingsDialog(self.language_manager, self)
            dlg.exec()

    def create_footer(self, parent_layout):
        self.footer_label = QLabel(self.language_manager.get_text('footer'))
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer_label.setStyleSheet(f"""
            QLabel {{
                color: {COLORS['text']['muted']};
                font-size: 10px;
                font-weight: medium;
                padding: 8px;
                background-color: {COLORS['primary']['dark']};
                border: 1px solid {COLORS['misc']['border']};
                border-radius: 8px;
            }}
        """)
        parent_layout.addWidget(self.footer_label)

    def on_language_changed(self):
        language_code = self.language_combo.currentData()
        if self.language_manager.set_language(language_code):
            self.restart_application()

    def restart_application(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def retranslate_ui(self):
        self.setWindowTitle(self.language_manager.get_text('app_title'))
        self.header_label.setText(self.language_manager.get_text('header'))
        self.footer_label.setText(self.language_manager.get_text('footer'))

    def open_display_settings(self):
        dlg = DisplaySettingsDialog(self.language_manager, self)
        dlg.exec()

    def open_wallpaper_settings(self):
        dlg = WallpaperSettingsDialog(self.language_manager, self)
        dlg.exec()

    def open_mouse_settings(self):
        dlg = MouseTouchpadDialog(self.language_manager, self)
        dlg.exec()

    def open_theme_settings(self):
        dlg = ThemeSettingsDialog(self.language_manager, self)
        dlg.exec()

    def open_keyboard_settings(self):
        dlg = KeyboardSettingsDialog(self.language_manager, self)
        dlg.exec()

    def load_fonts(self):
        try:
            font_paths = [
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/usr/share/fonts/TTF/DejaVuSans.ttf",
                "/usr/share/fonts/dejavu/DejaVuSans.ttf"
            ]

            for font_path in font_paths:
                if Path(font_path).exists():
                    font_id = QFontDatabase.addApplicationFont(font_path)
                    if font_id != -1:
                        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                        app_font = QFont(font_family, 9)
                        QApplication.setFont(app_font)
                        break
        except Exception as e:
            print(f"Font loading error: {e}")

    def set_modern_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(COLORS['primary']['dark']))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(COLORS['text']['primary']))
        palette.setColor(QPalette.ColorRole.Base, QColor(COLORS['primary']['medium']))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(COLORS['primary']['light']))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(COLORS['primary']['dark']))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(COLORS['text']['primary']))
        palette.setColor(QPalette.ColorRole.Text, QColor(COLORS['text']['primary']))
        palette.setColor(QPalette.ColorRole.Button, QColor(COLORS['primary']['medium']))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(COLORS['text']['primary']))
        palette.setColor(QPalette.ColorRole.BrightText, QColor("red"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(COLORS['accent']['blue']))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("white"))

        self.setPalette(palette)

        self.setStyleSheet(f"""
            QMainWindow {{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 {COLORS['primary']['dark']},
                    stop: 1 #0a0a1a);
                border: none;
            }}
            QScrollBar:vertical {{
                border: none;
                background: {COLORS['primary']['medium']};
                width: 8px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {COLORS['accent']['blue']};
                min-height: 20px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {COLORS['accent']['cyan']};
            }}
        """)

    def showEvent(self, event):
        self.setWindowOpacity(0.0)
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(500)
        self.fade_animation.setStartValue(0.0)
        self.fade_animation.setEndValue(1.0)
        self.fade_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.fade_animation.start()
        super().showEvent(event)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setApplicationName("EN-OS Settings Manager")
        app.setApplicationVersion("1.0")

        window = IceWMSettingsManager()
        window.show()

        sys.exit(app.exec())

    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
