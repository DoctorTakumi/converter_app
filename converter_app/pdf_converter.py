import os
from PySide6.QtWidgets import QFileDialog, QMessageBox, QInputDialog
from pdf2image import convert_from_path
from .helpers import get_unique_filename
from docx2pdf import convert
from PyPDF2 import PdfMerger

class PDFConverterActions:
    def __init__(self, parent):
        self.parent = parent
        # path to the bundled Poppler binaries
        self.poppler_path = os.path.join(os.path.dirname(__file__), "poppler", "bin")
        # print("Poppler path set to:", self.poppler_path)
        # print("Files in poppler/bin:", os.listdir(self.poppler_path))

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

    
    def select_docx_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self.parent, "Select DOCX Files", "", "Word Documents (*.docx)"
        )
        if file_paths:
            if len(file_paths) == 1:
                self.parent.label.setText("1 DOCX selected")
            else:
                self.parent.label.setText(f"{len(file_paths)} DOCX files selected")
            return file_paths
        return []

    def docx_to_pdf(self):
        paths = self.select_docx_files()
        if not paths:
            return

        # Use QMessageBox as a mini popup
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("DOCX to PDF Options")
        msg.setText(
            "Do you want to bundle all selected DOCX files into one PDF,\n"
            "or create one PDF per DOCX?"
        )
        bundle_button = msg.addButton("Single PDF (merge all)", QMessageBox.AcceptRole)
        multiple_button = msg.addButton("Multiple PDFs (one per DOCX)", QMessageBox.AcceptRole)
        msg.setStandardButtons(QMessageBox.Cancel)

        msg.exec()

        try:
            if msg.clickedButton() == multiple_button:
                for path in paths:
                    convert(path)  # one PDF per DOCX
            elif msg.clickedButton() == bundle_button:
                temp_dir = os.path.dirname(paths[0])
                merged_pdf_path = os.path.join(temp_dir, "merged.pdf")
                temp_pdf_paths = []
                for path in paths:
                    temp_pdf = os.path.splitext(path)[0] + "_temp.pdf"
                    convert(path, temp_pdf)
                    temp_pdf_paths.append(temp_pdf)

                merger = PdfMerger()
                for pdf in temp_pdf_paths:
                    merger.append(pdf)
                merger.write(merged_pdf_path)
                merger.close()

                for pdf in temp_pdf_paths:
                    os.remove(pdf)

            else:
                return  # Cancel pressed

            QMessageBox.information(self.parent, "Success", "DOCX converted to PDF successfully!")

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to convert DOCX files:\n{str(e)}")
