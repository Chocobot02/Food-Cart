from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from landingUI import landingUI

'''
this file should be executed :>
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = landingUI()
    main_window.show()
    sys.exit(app.exec())