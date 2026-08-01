from PySide6.QtWidgets import QPushButton, QWidget


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self):
        start_language_button = QPushButton("Start Language")
        continue_language_button = QPushButton("Load Language")
        recently_accessed_languages_widget = QWidget()
        exit_button = QPushButton("Exit")
