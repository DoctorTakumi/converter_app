import os
from PySide6.QtWidgets import QFileDialog, QMessageBox, QInputDialog
from pdf2image import convert_from_path
from .helpers import get_unique_filename

class PDFConverterActions:
    def __init__(self, parent):
        self.parent = parent
        # path to the bundled Poppler binaries
        self.poppler_path = os.path.join(os.path.dirname(__file__), "poppler", "bin")
        print("Poppler path set to:", self.poppler_path)
        print("Files in poppler/bin:", os.listdir(self.poppler_path))

    def select_files(self, filters="PDF Files (*.pdf)"):
        """Open file dialog to select multiple PDFs"""
        file_paths, _ = QFileDialog.getOpenFileNames(self.parent, "Select PDFs", "", filters)
        if file_paths:
            if len(file_paths) == 1:
                self.parent.label.setText("1 PDF selected")
            else:
                self.parent.label.setText(f"{len(file_paths)} PDFs selected")
            return file_paths
        return []
    


    def pdf_to_image(self):
        """Convert selected PDFs to either JPG or PNG"""
        paths = self.select_files()
        if not paths:
            return

        # Ask user which format
        formats = ["JPG", "PNG"]
        format_choice, ok = QInputDialog.getItem(
            self.parent, "Select Format", "Choose output format:", formats, 0, False
        )
        if not ok or not format_choice:
            return

        try:
            for path in paths:
                images = convert_from_path(path, poppler_path=self.poppler_path)
                for i, img in enumerate(images):
                    ext = format_choice.lower()
                    output_path = get_unique_filename(f"{os.path.splitext(path)[0]}_page{i+1}.{ext}")
                    if format_choice == "JPG":
                        img.save(output_path, "JPEG", quality=80)
                    else:
                        img.save(output_path, "PNG")
            QMessageBox.information(
                self.parent, "Success", f"PDFs converted to {format_choice} successfully!"
            )
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to convert PDFs:\n{str(e)}")
