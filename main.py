import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QLabel, QMessageBox
)
from PIL import Image

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PNG to JPEG Converter")
        self.layout = QVBoxLayout()

        self.label = QLabel("Select a PNG file to convert to JPEG")
        self.layout.addWidget(self.label)

        self.btn_select = QPushButton("Select PNG File")
        self.btn_select.clicked.connect(self.select_file)
        self.layout.addWidget(self.btn_select)

        self.setLayout(self.layout)

    # added multiple file formats
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
        self,
        "Open Image File",
        "",
        "Image Files (*.png *.jpg *.jpeg *.bmp *.webp)"
)

    def convert_image(self, path):
        try:
            img = Image.open(path)
            rgb_img = img.convert('RGB')  # PNG might have alpha channel

            save_path, _ = QFileDialog.getSaveFileName(self, "Save JPEG File", "", "JPEG Files (*.jpg *.jpeg)")
            if save_path:
                rgb_img.save(save_path, "JPEG", quality=70)  # quality from 0 (worst) to 95 (best)
                QMessageBox.information(self, "Success", f"Image saved as {save_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to convert image:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())

