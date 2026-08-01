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

        self.setWindowTitle("EasyLanguage")
        self.setMinimumSize(800, 500)