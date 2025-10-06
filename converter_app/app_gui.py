from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from converter_app.img_converter import ImageConverterActions


class ApplicationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.actions = ImageConverterActions(self)  ## Logic instance

        self.setStyleSheet("background-color: #f0f0f0;")  # light gray

        # window title and minimum size
        self.setWindowTitle("File Converter")
        self.setMinimumSize(450, 200)  # W x H

        # vertical layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Label to show instructions or selected file
        self.label = QLabel("Select a file to convert")
        self.label.setFont(QFont("Arial", 14))  ## set font here
        self.label.setStyleSheet("color: #2a9d8f;")  # teal color
        self.layout.addWidget(self.label)

        # Buttons for conversions
        # CONVERT TO JPG
        self.button_convert_to_jpg = QPushButton("Convert to JPG")
        self.button_convert_to_jpg.setFont(QFont("Arial", 12))
        self.button_convert_to_jpg.clicked.connect(self.actions.convert_to_jpg)
        self.layout.addWidget(self.button_convert_to_jpg)

        self.button_jpg_to_png = QPushButton("Convert JPG → PNG")
        self.button_jpg_to_png.setFont(QFont("Arial", 12))
        self.button_jpg_to_png.clicked.connect(self.actions.convert_jpg_to_png)
        self.layout.addWidget(self.button_jpg_to_png)

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)
