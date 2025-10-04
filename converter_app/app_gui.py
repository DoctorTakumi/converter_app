from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from converter_app.img_converter import ImageConverterActions


class ApplicationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.actions = ImageConverterActions(self)  ## Logic instance

        self.setWindowTitle("File Converter")
        self.layout = QVBoxLayout()

        # Label to show instructions or selected file
        self.label = QLabel("Select a file to convert")
        self.layout.addWidget(self.label)

        # Buttons for conversions
        self.button_png_to_jpeg = QPushButton("Convert PNG → JPEG")
        self.button_png_to_jpeg.clicked.connect(self.actions.convert_png_to_jpeg)
        self.layout.addWidget(self.button_png_to_jpeg)

        self.button_jpeg_to_png = QPushButton("Convert JPEG → PNG")
        self.button_jpeg_to_png.clicked.connect(self.actions.convert_jpeg_to_png)
        self.layout.addWidget(self.button_jpeg_to_png)

        self.setLayout(self.layout)
