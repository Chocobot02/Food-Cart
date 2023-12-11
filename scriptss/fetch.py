import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class uisetup:
    def center_on_screen(self):
        # Center the main window on the screen
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        size = self.geometry()
        self.move(
            screen_geometry.center().x() - size.width() // 2,
            screen_geometry.center().y() - size.height() // 2
        )

    @staticmethod
    def setup_ui(window, title, width, height, iconpath='./resources/images/cart_favicon.png', bgpath='./resources/images/bg.png'):
        window.setWindowTitle(title)
        window.setFixedSize(width, height)

        pixmap1 = QPixmap(os.path.abspath(iconpath))
        icon = QIcon(pixmap1)
        QApplication.setWindowIcon(icon)

        background = QLabel(window)
        pxm = QPixmap(os.path.abspath(bgpath))
        background.setPixmap(pxm)
        background.setGeometry(0, 0, width, height)

    