import base64
from typing import Optional

from PySide6.QtCore import QObject, Qt, Slot, QMetaObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QStyle,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QToolButton,
)

from .AdvancedPlainTextEdit import AdvancedPlainTextEdit
from .Resources import *  # noqa


class MainWindow(QWidget):
    def __init__(
        self,
        parent: Optional[QObject] = None,
        flags: Qt.WindowType = Qt.WindowType.Window,
    ):
        super().__init__(parent, flags)

        self._initUi()

    def _initUi(self):
        # init main layout
        self._mainLayout = QVBoxLayout(self)
        self.setLayout(self._mainLayout)

        # init up label widget
        self._hWidgetUp = QWidget(self)
        self._hLayoutUp = QHBoxLayout(self)
        self._hWidgetUp.setLayout(self._hLayoutUp)
        self._mainLayout.addWidget(self._hWidgetUp)

        # insert source label
        self._labelSource = QLabel("原文", self)
        self._hLayoutUp.addWidget(self._labelSource)

        # insert textedit of source
        self._hWidgetSourceText = AdvancedPlainTextEdit(self)
        self._mainLayout.addWidget(self._hWidgetSourceText)

        # init middle widget bar
        self._hWidgetMid = QWidget(self)
        self._hLayoutMid = QHBoxLayout(self)
        self._hWidgetMid.setLayout(self._hLayoutMid)
        self._mainLayout.addWidget(self._hWidgetMid)

        # insert label and buttons
        self._base64Label = QLabel("base64 编码", self)
        self._hLayoutMid.addWidget(self._base64Label)
        self._hLayoutMid.addItem(
            QSpacerItem(
                80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
            )
        )

        self._encodeButton = QToolButton(self)
        self._encodeButton.setObjectName("encodeButton")
        self._encodeButton.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown)
        )
        self._encodeButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self._hLayoutMid.addWidget(self._encodeButton)

        self._decodeButton = QToolButton(self)
        self._decodeButton.setObjectName("decodeButton")
        self._decodeButton.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowUp)
        )
        self._decodeButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self._hLayoutMid.addWidget(self._decodeButton)

        self._hLayoutMid.addItem(
            QSpacerItem(
                80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
            )
        )

        # insert textedit of base64
        self._hWidgetBase64Text = AdvancedPlainTextEdit(self)
        self._mainLayout.addWidget(self._hWidgetBase64Text)

        # window icon, size, etc...
        self.resize(800, 600)
        self.setWindowIcon(QIcon(":/imgs/window-icon.jpg"))
        self.setWindowTitle("base64code")

        # connect slot
        QMetaObject.connectSlotsByName(self)

    @Slot()
    def on_encodeButton_clicked(self):
        text = self._hWidgetSourceText.toPlainText()
        text = text.strip()

        encoded_bytes = base64.b64encode(text.encode("utf-8"))
        encoded_text = encoded_bytes.decode("utf-8")

        self._hWidgetBase64Text.setPlainText(encoded_text)

    @Slot()
    def on_decodeButton_clicked(self):
        text = self._hWidgetBase64Text.toPlainText()
        text = text.strip()

        decoded_bytes = base64.b64decode(text)
        decoded_text = decoded_bytes.decode("utf-8")

        self._hWidgetSourceText.setPlainText(decoded_text)
