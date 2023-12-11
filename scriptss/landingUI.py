from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from fetch import uisetup

class landingUI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        uisetup.center_on_screen(self)
    
    def initUI(self):
        uisetup.setup_ui(self, 'Food Cart - Welcome', 450, 500)
        self.greetings = QLabel(self)
        self.greetings.setText('Welcome to \nFood Cart')
        self.greetings.setStyleSheet('''
            color: white;
            font-weight: bold;
            font-family: Poppins, Helvetica, sans-serif;
            font-size: 40px;
''')

        self.go_cart = QPushButton(self)
        self.go_cart.setFixedSize(300,65)
        self.go_cart.setText('GO SHOPPING')
        self.go_cart.setStyleSheet('''
            QPushButton{
                background-color: #557C55;
                color: white;
                font-size: 25px;
                font-weight: bold;
                border: none;
                border-radius: 30px}
                                   
            QPushButton:hover{
                background-color: green;
                color: white;
                border: 1px solid green;
            }
    
''')   
        self.go_cart.clicked.connect(self.gocart)
        
        self.go_about = QPushButton(self)
        self.go_about.setText('ABOUT')
        self.go_about.setFixedSize(300,65)
        self.go_about.setStyleSheet('''
            QPushButton{
                background-color: #1640D6;
                color: white;
                font-size: 25px;
                font-weight: bold;
                border: none;
                border-radius: 25px;}
            QPushButton:hover{
                background-color: white;
                color: #1640D6;
                border: 1px solid #1640D6;
            }
''')
        self.go_about.clicked.connect(self.goto_about)

        self.go_quit = QPushButton(self)
        self.go_quit.setText('EXIT')
        self.go_quit.setFixedSize(300,65)
        self.go_quit.setStyleSheet('''
            QPushButton{
                background-color: red;
                color: white;
                font-size: 25px;
                font-weight: bold;
                border: none;
                border-radius: 25px}
                                   
            QPushButton:hover{
                background-color: white;
                color: red;
                border: 1px solid red;
            }
            
''')
        self.go_quit.clicked.connect(self.close)

        greet_layout = QVBoxLayout()
        greet_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        greet_layout.addWidget(self.greetings)

        btns_layout = QVBoxLayout()
        btns_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btns_layout.addWidget(self.go_cart)
        btns_layout.addWidget(self.go_about)
        btns_layout.addWidget(self.go_quit)
        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(greet_layout)
        main_layout.addSpacing(30)
        main_layout.addLayout(btns_layout)

        self.setLayout(main_layout)

    def goto_about(self):
        from aboutUI import aboutui
        self.switchabout = aboutui()
        self.switchabout.show()
        self.close()

    def gocart(self):
        from cart import cartUI
        self.switchcart = cartUI()
        self.switchcart.show()
        self.close()
