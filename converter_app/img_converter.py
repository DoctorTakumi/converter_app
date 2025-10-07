from PySide6.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
from os.path import basename


class ImageConverterActions:
    def __init__(self, parent):
        self.parent = parent

    def select_file(self, filter="Image Files (*.png *.jpg *.jpeg *.bmp *.webp)"):
        """Generic file picker with filter"""
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Open File", "", filter)
        if file_path:
            self.parent.label.setText(f"Selected file: {basename(file_path)}")
            return file_path
        return None

    def convert_to_jpg(self):
        path = self.select_file("Images (*.png *.bmp *.webp *.jpeg *.jpg)")
        if not path:
            return
        self._convert_image(path, "JPEG", "JPEG Files (*.jpg *.jpeg)")

    def convert_to_png(self):
        path = self.select_file("Image Files (*.bmp *.webp *.jpg *.jpeg)")
        if not path:
            return
        self._convert_image(path, "PNG", "PNG Files (*.png)")

    def _convert_image(self, path, format, save_filter):
        """Generic conversion helper"""
        try:
            img = Image.open(path)
            if format == "JPEG":
                img = img.convert("RGB")  # remove alpha for JPEG

            save_path, _ = QFileDialog.getSaveFileName(
                self.parent, "Save File", "", save_filter
            )
            if save_path:
                img.save(save_path, format, quality=70 if format == "JPEG" else None)
                QMessageBox.information(self.parent, "Success", f"Saved: {save_path}")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed:\n{str(e)}")
