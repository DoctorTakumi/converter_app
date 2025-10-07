import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
from os.path import basename


class ImageConverterActions:
    def __init__(self, parent):
        self.parent = parent

    # function for single file conversion
    def select_file(self, filter="Image Files (*.png *.jpg *.jpeg *.bmp *.webp)"):
        """Generic file picker with filter"""
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Open File", "", filter)
        if file_path:
            self.parent.label.setText(f"Selected file: {basename(file_path)}")
            return file_path
        return None
    
    # function for batch conversion
    def select_files(self, filter="Image Files (*.png *.bmp *.webp *.jpeg *.jpg)"):
        """Multi-file picker with filter"""
        file_paths, _ = QFileDialog.getOpenFileNames(self.parent, "Select Files", "", filter)
        if file_paths:
            self.parent.label.setText(f"Selected {len(file_paths)} files")
            return file_paths
        return []

    # conversion to JPG
    def convert_to_jpg(self):
        paths = self.select_files("Image Files (*.png *.bmp *.webp)")
        if not paths:
            return
        
        for path in paths:
            self._convert_image(path, "JPEG")

    # conversion to PNG
    def convert_to_png(self):
        paths = self.select_files("Image Files (*.bmp *.webp *.jpg *.jpeg)")
        if not paths:
            return
        
        for path in paths:
            self._convert_image(path, "PNG")

    def _convert_image(self, path, format):
        """Convert a single image to the specified format and save it next to the original."""
        try:
            img = Image.open(path)

            if format == "JPEG":
                img = img.convert("RGB")  # remove alpha channel (JPEG doesn't support transparency)

            # Build the output file path: originalname_converted.jpg/png
            base_name = os.path.splitext(path)[0]
            output_path = f"{base_name}_converted.{format.lower()}"

            # Save the image
            img.save(output_path, format, quality=70 if format == "JPEG" else None)

            print(f"Saved: {output_path}")

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to convert:\n{path}\n\n{str(e)}")