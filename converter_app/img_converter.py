from PySide6.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
from os.path import basename  # optional if you want just the file name


class ImageConverterActions:
    def __init__(self, parent):
        self.parent = parent

    # QfileDialog opens system's native file picker (Explorer in this case)
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Open Image File",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.webp)",
        )
        if file_path:
            # Update GUI label with the selected file name
            self.parent.label.setText(f"Selected file: {basename(file_path)}")
            self.convert_image(file_path)  ## this converts the file

    def convert_image(self, path):
        try:
            img = Image.open(path)
            rgb_img = img.convert("RGB")  # PNG might have alpha channel

            # this saves the file
            save_path, _ = QFileDialog.getSaveFileName(
                self.parent, "Save JPEG File", "", "JPEG Files (*.jpg *.jpeg)"
            )
            if save_path:
                rgb_img.save(
                    save_path, "JPEG", quality=70
                )  # quality from 0 (worst) to 95 (best)
                QMessageBox.information(
                    self.parent, "Success", f"Image saved as {save_path}"
                )
        except Exception as e:
            QMessageBox.critical(
                self.parent, "Error", f"Failed to convert image:\n{str(e)}"
            )
