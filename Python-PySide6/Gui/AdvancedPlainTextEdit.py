from typing import Optional

from PySide6.QtWidgets import QPlainTextEdit, QWidget


class AdvancedPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
