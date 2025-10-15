import io.calamares.ui 1.0

Page
{
    id: root

    Header {
        id: header
        title: qsTr("Выбор ядра Linux")
    }

    Rectangle {
        anchors.top: header.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 20

        // Скрываем правую панель со скриншотами
        PackageList {
            id: packageList
            anchors.fill: parent
            showScreenshots: false  // Отключаем скриншоты
        }
    }
}
