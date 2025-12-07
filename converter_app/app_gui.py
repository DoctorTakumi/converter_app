from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox
from PySide6.QtGui import QFont
from converter_app.img_converter import ImageConverterActions
from converter_app.pdf_converter import PDFConverterActions


class ApplicationGUI(QWidget):
    def __init__(self):
        super().__init__()
        # adding ": ImageConverterActions" to tell VSC that self.actions is of type ImageConverterActions
        ## calls __init__ of ImageConverterActions class and assigns it to the self.actions variable
        ### ImageConverterActions class can access and control things in GUI (self.label, etc.)
        self.actions: ImageConverterActions = ImageConverterActions(self)
        self.pdf_actions: PDFConverterActions = PDFConverterActions(self)

        # GUI visuals
        self.setStyleSheet("background-color: #f0f0f0;")  # light gray
        self.setWindowTitle("File Converter")
        self.setMinimumSize(450, 200)  # W x H

        # button style function
        button_style = """
            QPushButton {
                background-color: #add8e6;  /* light blue */
                color: black;
                border: 1px solid #7aa7c7;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #9ec9e0;  /* slightly darker on hover */
            }
        """


        # vertical layout
        ## ": QVBoxLayout" as a type hint to tell VSC that self.layout is a QVBoxLayout
        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)

        # Label to show instructions or selected file
        self.label = QLabel("Select a file to convert")
        self.label.setFont(QFont("Arial", 14))  ## set font here
        self.label.setStyleSheet("color: #2a9d8f;")  # teal color
        self.layout.addWidget(self.label)

        # Info button
        self.button_info = QPushButton("Info")
        self.button_info.setFont(QFont("Arial", 10))
        self.button_info.setStyleSheet(button_style + "QPushButton {min-width: 80px;}")
        self.button_info.clicked.connect(self.show_info_popup)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.label)
        top_layout.addStretch()  # pushes the button to the right
        top_layout.addWidget(self.button_info)
        self.layout.addLayout(top_layout)

    

        # Buttons for conversions
        # CONVERT TO JPG
        self.button_convert_to_jpg = QPushButton("Convert to JPG")
        self.button_convert_to_jpg.setFont(QFont("Arial", 12))
        self.button_convert_to_jpg.clicked.connect(self.actions.convert_to_jpg)
        self.button_convert_to_jpg.setStyleSheet(button_style)
        self.layout.addWidget(self.button_convert_to_jpg)

        # CONVERT TO PNG
        self.button_convert_to_png = QPushButton("Convert to PNG")
        self.button_convert_to_png.setFont(QFont("Arial", 12))
        self.button_convert_to_png.clicked.connect(self.actions.convert_to_png)
        self.button_convert_to_png.setStyleSheet(button_style)
        self.layout.addWidget(self.button_convert_to_png)

        # CONVERT TO ICO
        self.button_convert_to_ico = QPushButton("Convert to ICO")
        self.button_convert_to_ico.setFont(QFont("Arial", 12))
        self.button_convert_to_ico.clicked.connect(self.actions.convert_to_ico)
        self.button_convert_to_ico.setStyleSheet(button_style)
        self.layout.addWidget(self.button_convert_to_ico)

        # IMAGES TO PDF
        self.button_image_to_pdf = QPushButton("Image to PDF")
        self.button_image_to_pdf.setFont(QFont("Arial", 12))
        self.button_image_to_pdf.clicked.connect(self.actions.image_to_pdf)
        self.button_image_to_pdf.setStyleSheet(button_style)
        self.layout.addWidget(self.button_image_to_pdf)

        # PDF TO IMAGES
        self.button_pdf_to_image = QPushButton("PDF to Image")
        self.button_pdf_to_image.setFont(QFont("Arial", 12))
        self.button_pdf_to_image.clicked.connect(self.pdf_actions.pdf_to_image)
        self.button_pdf_to_image.setStyleSheet(button_style)
        self.layout.addWidget(self.button_pdf_to_image)

        # DOCX TO PDF
        # PDF TO DOCX
        #PDF SHRINK

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

    def show_info_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Conversion Modes Info")
        msg.setText(
            "This app supports the following conversion modes:\n\n"
            "• png, bmp, webp, avif to JPG\n"
            "• bmp, webp, jpg, jpeg, ico, avif to PNG\n"
            "• png, jpg, jpeg to ICO\n"
            "• PDF to Image (JPG or PNG)\n"
        )
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
