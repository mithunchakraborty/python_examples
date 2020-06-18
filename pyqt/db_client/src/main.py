import sys
import table
from window import Program
from authorization import Authorization
from PyQt5.QtWidgets import QApplication

def main() :
    app = QApplication(sys.argv)

    window = Program()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__" :
    main()
