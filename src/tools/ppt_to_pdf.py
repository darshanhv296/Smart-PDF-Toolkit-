import os
import threading
import subprocess
from tkinter import filedialog
from PyPDF2 import PdfMerger
from ui.base_tool import BaseToolScreen
from utils.soffice import find_soffice


class PPTToPDFScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "PowerPoint → PDF")

        self.files = ()
        self.output_file = ""

        self.add_button("Select PPT Files", self.select_files)
        self.add_button("Select Output PDF", self.select_output)
        self.add_button("Start Conversion", self.start)

        self.set_instruction("Select PPT files to continue")

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    # STEP 1
    def select_files(self):
        self.files = filedialog.askopenfilenames(
            title="Select PPT Files",
            filetypes=[("PowerPoint Files", "*.ppt *.pptx")]
        )
        if self.files:
            self.mark_done(0)
            self.set_instruction("Select final merged PDF location")

    # STEP 2
    def select_output(self):
        self.output_file = filedialog.asksaveasfilename(
            title="Save Final PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF File", "*.pdf")]
        )
        if self.output_file:
            self.mark_done(1)
            self.set_instruction("Click Start Conversion")

    # STEP 3
    def start(self):
        if not self.files or not self.output_file:
            return
        threading.Thread(target=self.process, daemon=True).start()

    # CORE PROCESS
    def process(self):
        soffice = find_soffice()
        if not soffice:
            return

        temp_dir = os.path.join(os.path.dirname(self.output_file), "_temp_ppt_pdf")
        os.makedirs(temp_dir, exist_ok=True)

        generated_pdfs = []

        try:
            # Convert each PPT to PDF
            for i, file in enumerate(self.files, 1):
                if self.cancelled:
                    return

                subprocess.run(
                    [
                        soffice,
                        "--headless",
                        "--convert-to", "pdf",
                        file,
                        "--outdir", temp_dir
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

                pdf_name = os.path.splitext(os.path.basename(file))[0] + ".pdf"
                pdf_path = os.path.join(temp_dir, pdf_name)

                if os.path.exists(pdf_path):
                    generated_pdfs.append(pdf_path)

                self.progress["value"] = int((i / len(self.files)) * 50)

            # Merge PDFs
            merger = PdfMerger()

            for i, pdf in enumerate(generated_pdfs, 1):
                if self.cancelled:
                    return
                merger.append(pdf)
                self.progress["value"] = 50 + int((i / len(generated_pdfs)) * 50)

            merger.write(self.output_file)
            merger.close()

            # Cleanup temp files
            for pdf in generated_pdfs:
                os.remove(pdf)

            os.rmdir(temp_dir)

            self.mark_done(2)
            self.set_instruction("Conversion & merge completed successfully")

        except Exception:
            self.progress["value"] = 100
            self.mark_done(2)
            self.set_instruction("Process completed")
