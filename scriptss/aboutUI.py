
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from fetch import uisetup

class aboutui(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uisetup.setup_ui(self, 'Food Cart - About', 500, 600)
        
        self.horizonLine = QFrame(self)
        self.horizonLine.setFrameShape(QFrame.Shape.HLine)
        self.horizonLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizonLine1 = QFrame(self)
        self.horizonLine1.setFrameShape(QFrame.Shape.HLine)
        self.horizonLine1.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizonLine2 = QFrame(self)
        self.horizonLine2.setFrameShape(QFrame.Shape.HLine)
        self.horizonLine2.setFrameShadow(QFrame.Shadow.Sunken)

        titlestylesheet = '''
            color: white;
            font-weight: bold;
            font-family: Poppins, Helvetica, sans-serif;
            font-size: 30px;
'''
        contentstylesheet = '''
            color: white;
            font-family: Poppins, Helvetica, sans-serif;
            font-size: 15px;
'''
        self.aboutsign = QLabel(self)
        self.aboutsign.setText('ABOUT')
        self.aboutsign.setStyleSheet('''
                                    color: white;
                                    font-weight: bold;
                                    font-family: Poppins, Helvetica, sans-serif;
                                    font-size: 55px;
''')
        
        self.Howtotitle = QLabel(self)
        self.Howtotitle.setText('How to Use? ')
        self.Howtotitle.setStyleSheet(titlestylesheet)

        how_content = "<ul>" \
                       "<li>Click the 'click 'GO SHOPPING' button.</li>" \
                       "<li>Choose yout desired food(s).</li>" \
                       "<li>Click the item in the Order Details to delete</li>" \
                       "<li>Click 'Place order' button to buy.</li>" \
                       "</ul>"
        self.list_label = QLabel(self)
        self.list_label.setText(how_content)
        self.list_label.setStyleSheet(contentstylesheet) 

        self.featstitle = QLabel(self)
        self.featstitle.setText('Application Features: ')
        self.featstitle.setStyleSheet(titlestylesheet)

        feats_content = "<Ol>" \
                       "<li>Can add the listed different food(s) in your list.</li>" \
                       "<li>Can Remove/ food(s) in your list.</li>" \
                       "</Ol>"   
        self.feat_list = QLabel(self)
        self.feat_list.setText(feats_content)
        self.feat_list.setStyleSheet(contentstylesheet)

        howtouse_layout = QVBoxLayout()
        howtouse_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        howtouse_layout.addWidget(self.Howtotitle)
        howtouse_layout.addWidget(self.list_label)

        feat_layout = QVBoxLayout()
        feat_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        feat_layout.addWidget(self.featstitle)
        feat_layout.addWidget(self.feat_list)

        self.footer = QLabel(self)
        self.footer.setText('Created on Dec, 2023')
        self.footer.setStyleSheet('''color: white;
            font-weight: bold;
            font-family: Poppins, Helvetica, sans-serif;''')
        self.backbutton = QPushButton(self)
        self.backbutton.setText('BACK')
        self.backbutton.setFixedSize(300,65)
        self.backbutton.setStyleSheet('''
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
        self.backbutton.clicked.connect(self.goback)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.aboutsign)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.horizonLine)
        main_layout.addLayout(feat_layout)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.horizonLine1)
        main_layout.addLayout(howtouse_layout)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.horizonLine2)
        main_layout.addWidget(self.backbutton, Qt.AlignmentFlag.AlignLeft)
        main_layout.addStretch(1)
        main_layout.addWidget(self.footer, Qt.AlignmentFlag.AlignRight)
        self.setLayout(main_layout)
    
    def goback(self):
        from landingUI import landingUI
        self.switchabout = landingUI()
        self.switchabout.show()
        self.close()