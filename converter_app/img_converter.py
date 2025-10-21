import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
from os.path import basename
from .helpers import get_unique_filename


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
            if len(file_paths) == 1:
                self.parent.label.setText(f"{len(file_paths)} file selected")
            else:
                self.parent.label.setText(f"{len(file_paths)} files selected")
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
        paths = self.select_files("Image Files (*.bmp *.webp *.jpg *.jpeg *.ico)")
        if not paths:
            return
        
        for path in paths:
            self._convert_image(path, "PNG")

    # conversion to ICO
    def convert_to_ico(self):
        paths = self.select_files("Image Files (*.png *.jpg *.jpeg)")
        if not paths:
            return
        
        for path in paths:
            self._convert_image(path, "ICO")

    def _convert_image(self, path, format):
        """Convert a single image to the specified format and save it next to the original."""
        try:
            img = Image.open(path)
            # Build the output file path: originalname_converted.jpg/png
            base_name = os.path.splitext(path)[0]
            output_path = f"{base_name}_converted.{format.lower()}"
            output_path = get_unique_filename(output_path)

            if format == "JPEG":
                img = img.convert("RGB")  # remove alpha channel (JPEG doesn't support transparency)
                img.save(output_path, format="JPEG", quality=70)

            elif format == "PNG":
                img = img.convert("RGBA") # ensures alpha is preserved
                img.save(output_path, format="PNG")

            elif format == "ICO":
                img = img.convert("RGBA") # ICO supports transparency
                # resize to common icon sizes
                sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
                output_path = f"{base_name}_converted.ico" # overrides extension
                # here Pillow packages all resized versions into one .ico file which OS will auto-select later
                img.save(output_path, format="ICO", sizes=sizes)

            else:
                raise ValueError(f"Unsupported format: {format}")
            

            print(f"Saved: {output_path}")

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to convert:\n{path}\n\n{str(e)}")