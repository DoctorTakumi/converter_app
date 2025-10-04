from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from converter_app.img_converter import ImageConverterActions


class ApplicationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.actions = ImageConverterActions(self)  ## Logic instance

        self.setWindowTitle("File Converter")
        self.layout = QVBoxLayout()

        # Label to show instructions or selected file
        self.label = QLabel("Select a PNG file to convert to JPEG")
        self.layout.addWidget(self.label)

        # Button connected to logic method
        self.button_select = QPushButton("Select PNG File")
        self.button_select.clicked.connect(self.actions.select_file)
        self.layout.addWidget(self.button_select)

        self.setLayout(self.layout)
