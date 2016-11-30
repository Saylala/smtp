import sys
import graphics
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW = graphics.Graphics()
    WINDOW.setWindowFlags(
        Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    WINDOW.show()
    sys.exit(APP.exec_())
