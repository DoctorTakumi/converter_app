import sys
from PySide6.QtWidgets import QApplication
from converter_app.app_gui import ApplicationGUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationGUI()  # calls appGUI class
    window.show()
    sys.exit(app.exec())
