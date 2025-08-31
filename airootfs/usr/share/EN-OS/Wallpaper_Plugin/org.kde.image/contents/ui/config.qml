pragma ComponentBehavior: Bound
import QtQuick 2.15
import QtQuick.Controls 2.15 as QC
import QtQuick.Layouts 1.15
import org.kde.kirigami.layouts 2.0 as KirigamiLayouts

KirigamiLayouts.FormLayout {
    anchors.fill: parent

    property alias cfg_fontSize: fontSpin.value
    property alias cfg_speed: speedSpin.value
    property alias cfg_colorMode: modeCombo.currentIndex
    property alias cfg_singleColor: colorField.text
    property alias cfg_paletteIndex: paletteCombo.currentIndex
    property alias cfg_jitter: jitterSpin.value
    property alias cfg_glitchChance: glitchSpin.value

    QC.SpinBox {
        id: fontSpin; from:8; to:48; stepSize:1; value:configuration.fontSize
        onValueChanged: configuration.fontSize = value
        KirigamiLayouts.FormData.label: qsTr("Font Size")
    }
    QC.SpinBox {
        id: speedSpin; from:1; to:100; stepSize:1; value:configuration.speed
        onValueChanged: configuration.speed = value
        KirigamiLayouts.FormData.label: qsTr("Speed")
    }
    QC.ComboBox {
        id: modeCombo; model:[qsTr("Single Color"), qsTr("Multi Color")]
        currentIndex: configuration.colorMode
        onCurrentIndexChanged: configuration.colorMode = currentIndex
        KirigamiLayouts.FormData.label: qsTr("Color Mode")
    }
    QC.TextField {
        id: colorField; text:configuration.singleColor
        onTextChanged: configuration.singleColor = text
        visible: modeCombo.currentIndex === 0
        KirigamiLayouts.FormData.label: qsTr("Single Color")
    }
    QC.Button {
        text: qsTr("Default"); visible: modeCombo.currentIndex === 0
        onClicked: colorField.text = "#00ff00"
    }
    QC.ComboBox {
        id: paletteCombo; model:[qsTr("Neon"), qsTr("Cyberpunk"), qsTr("Synthwave")]
        currentIndex: configuration.paletteIndex
        onCurrentIndexChanged: configuration.paletteIndex = currentIndex
        visible: modeCombo.currentIndex === 1
        KirigamiLayouts.FormData.label: qsTr("Palette")
    }
    QC.SpinBox {
        id: jitterSpin; from:0; to:100; stepSize:1; value:configuration.jitter * 100
        onValueChanged: configuration.jitter = value / 100
        KirigamiLayouts.FormData.label: qsTr("Jitter (%)")
    }
    QC.SpinBox {
        id: glitchSpin; from:0; to:100; stepSize:1; value:configuration.glitchChance
        onValueChanged: configuration.glitchChance = value
        KirigamiLayouts.FormData.label: qsTr("Glitch Chance (%)")
    }
}
