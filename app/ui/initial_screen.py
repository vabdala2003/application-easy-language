from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox
)


class InitialScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.configure_window()
        self.load_ui()

    def configure_window(self):
        self.setWindowTitle("EasyLanguage")
        self.setMinimumSize(800, 500)
        self.setWindowIcon(QIcon("app/ui/assets/icons/easy-language-ico.ico"))

    def load_ui(self):
        pass