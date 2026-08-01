from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QStackedWidget, QVBoxLayout,
                               QWidget)

from app.core.custom_exceptions import UIException
from app.ui.screens import (CurrentLanguageScreen, HomeScreen,
                            LoadLanguageScreen, NewLanguageScreen)

APP_ICON_PATH = Path("app/ui/assets/icons/easy-language-ico.ico")


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.configure_window()

        self.app_screen_container = QStackedWidget()

        self.screens = {
            "home": HomeScreen(),
            "new_language": NewLanguageScreen(),
            "load_language": LoadLanguageScreen(),
            "current_language": CurrentLanguageScreen(),
        }

        for screen in self.screens.values():
            self.app_screen_container.addWidget(screen)

        self.setCentralWidget(self.app_screen_container)
        self.change_screen("home")

    def configure_window(self) -> None:
        self.setWindowTitle("EasyLanguage")
        self.setMinimumSize(800, 500)
        self.setWindowIcon(QIcon(str(APP_ICON_PATH)))

    def change_screen(self, screen_name: str) -> None:
        screen = self.screens.get(screen_name)

        if screen is None:
            raise UIException(
                f"Application tried to open a non-existing screen: {screen_name}"
            )

        self.app_screen_container.setCurrentWidget(screen)
