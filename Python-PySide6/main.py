import sys
from typing import Union, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from Gui import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow(None, flags=Qt.WindowType.Window)
    main_window.showNormal()
    sys.exit(app.exec())
