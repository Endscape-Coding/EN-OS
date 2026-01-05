/* === This file is part of Calamares - <https://calamares.io> ===
 *
 *   SPDX-FileCopyrightText: 2015 Teo Mrnjavac <teo@kde.org>
 *   SPDX-FileCopyrightText: 2018 Adriaan de Groot <groot@kde.org>
 *   SPDX-License-Identifier: GPL-3.0-or-later
 *
 *   Calamares is Free Software: see the License-Identifier above.
 *
 */

import QtQuick 2.0
import QtQuick.Controls 2.0
import calamares.slideshow 1.0

Presentation
{
    id: presentation

    property int transitionDuration: 1000
    property int slideDuration: 6000
    property string easingType: Easing.InOutQuad

    function nextSlide() {
        console.log("Process is running in the background...");
        presentation.goToNextSlide();
    }

    Timer {
        id: advanceTimer
        interval: slideDuration + transitionDuration
        running: true
        repeat: true
        onTriggered: nextSlide()
    }

    transitions: [
        Transition {
            to: "*"
            NumberAnimation {
                properties: "x"
                duration: transitionDuration
                easing.type: Easing[easingType]
            }
        }
    ]

    Rectangle {
        anchors.fill: parent
        color: "#2a2e32"
        z: -1
    }

    Slide {
        id: slide1
        anchors.fill: parent
        x: presentation.currentSlide === 0 ? 0 : (presentation.currentSlide < 0 ? -parent.width : parent.width)

        Behavior on x {
            NumberAnimation {
                duration: transitionDuration
                easing.type: Easing[easingType]
            }
        }

        Image {
            id: slide_trust
            source: "slides-telegram.png"
            fillMode: Image.PreserveAspectCrop
            anchors.fill: parent
            opacity: slide1.x === 0 ? 1 : 0.3

            Behavior on opacity {
                NumberAnimation {
                    duration: transitionDuration/2
                }
            }
        }
    }

    Slide {
        id: slide2
        anchors.fill: parent
        x: presentation.currentSlide === 1 ? 0 : (presentation.currentSlide < 1 ? -parent.width : parent.width)

        Behavior on x {
            NumberAnimation {
                duration: transitionDuration
                easing.type: Easing[easingType]
            }
        }

        Image {
            id: slide_welcome_app
            source: "slides-drivers.png"
            fillMode: Image.PreserveAspectCrop
            anchors.fill: parent
            opacity: slide2.x === 0 ? 1 : 0.3

            Behavior on opacity {
                NumberAnimation {
                    duration: transitionDuration/2
                }
            }
        }
    }

    Slide {
        id: slide3
        anchors.fill: parent
        x: presentation.currentSlide === 2 ? 0 : (presentation.currentSlide < 2 ? -parent.width : parent.width)

        Behavior on x {
            NumberAnimation {
                duration: transitionDuration
                easing.type: Easing[easingType]
            }
        }

        Image {
            id: slide_discover
            source: "slide-userfriendly.png"
            fillMode: Image.PreserveAspectCrop
            anchors.fill: parent
            opacity: slide3.x === 0 ? 1 : 0.3

            Behavior on opacity {
                NumberAnimation {
                    duration: transitionDuration/2
                }
            }
        }
    }

    Slide {
        id: slide4
        anchors.fill: parent
        x: presentation.currentSlide === 3 ? 0 : (presentation.currentSlide < 3 ? -parent.width : parent.width)

        Behavior on x {
            NumberAnimation {
                duration: transitionDuration
                easing.type: Easing[easingType]
            }
        }

        Image {
            id: slide_forum
            source: "slides-community.png"
            fillMode: Image.PreserveAspectCrop
            anchors.fill: parent
            opacity: slide4.x === 0 ? 1 : 0.3

            Behavior on opacity {
                NumberAnimation {
                    duration: transitionDuration/2
                }
            }
        }
    }

    function onActivate() {
        console.log("QML Component (default slideshow) activated");
        presentation.currentSlide = 0;
    }

    function onLeave() {
        console.log("QML Component (default slideshow) deactivated");
    }
}
