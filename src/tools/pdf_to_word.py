import os
import threading
import subprocess
from typing import Optional
from tkinter import filedialog, messagebox
from ui.base_tool import BaseToolScreen
from utils.soffice import find_soffice


class PDFToWordScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "PDF → Word")

        self.pdf_file: Optional[str] = None
        self.output_file: Optional[str] = None

        self.add_button("Select PDF File", self.select_file)
        self.add_button("Save Output File", self.select_output)
        self.add_button("Start Conversion", self.start)

        # Important instruction
        self.set_instruction("Only text-based PDFs are supported")

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    # STEP 1 (SINGLE PDF ONLY)
    def select_file(self):
        self.pdf_file = filedialog.askopenfilename(
            title="Select a PDF file to convert",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if self.pdf_file:
            self.mark_done(0)
            self.set_instruction("Select output Word file name and location")

    # STEP 2
    def select_output(self):
        self.output_file = filedialog.asksaveasfilename(
            title="Save Word Document As",
            defaultextension=".docx",
            filetypes=[("Word Document", "*.docx"), ("All Files", "*.*")]
        )
        if self.output_file:
            self.mark_done(1)
            self.set_instruction("Click Start Conversion")

    # STEP 3
    def start(self):
        if not self.pdf_file or not self.output_file:
            messagebox.showerror("Error", "Complete all steps first")
            return
        threading.Thread(target=self.process, daemon=True).start()

    def process(self):
        if not self.pdf_file or not self.output_file:
            messagebox.showerror("Error", "File paths not set")
            return
        
        soffice = find_soffice()
        if not soffice:
            messagebox.showerror("Error", "LibreOffice not found")
            return

        out_dir = os.path.dirname(self.output_file)
        out_dir = out_dir if out_dir else "."
        desired_name = os.path.basename(self.output_file)

        try:
            result = subprocess.run(
                [
                    soffice,
                    "--headless",
                    "--convert-to", "docx",
                    self.pdf_file,
                    "--outdir", out_dir
                ],
                check=False
            )

            # If conversion failed, show error
            if result.returncode != 0:
                messagebox.showerror("Error", "PDF conversion failed")
                return

            generated = os.path.join(
                out_dir,
                os.path.splitext(os.path.basename(self.pdf_file))[0] + ".docx"
            )

            if os.path.exists(generated):
                os.replace(generated, os.path.join(out_dir, desired_name))

            self.progress["value"] = 100
            self.mark_done(2)
            self.set_instruction("Conversion completed successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Conversion error: {str(e)}")
        self.set_instruction("Conversion completed")
