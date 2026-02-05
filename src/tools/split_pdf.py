import os
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from ui.base_tool import BaseToolScreen

class SplitPDFScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "Split PDF")
        self.pdf: str = ""
        self.outdir: str = ""

        self.add_button("Select PDF", self.select_pdf)
        self.add_button("Select Output Folder", self.select_out)
        self.add_button("Start Split", self.start)

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    def select_pdf(self):
        self.pdf = filedialog.askopenfilename(
            title="Select PDF File to Split",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if self.pdf:
            self.mark_done(0)
            self.set_instruction("Select output folder")

    def select_out(self):
        output_path = filedialog.asksaveasfilename(
            title="Select Output Folder for Split PDFs",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if output_path and isinstance(output_path, str):
            dirname_str = os.path.dirname(output_path)
            self.outdir = dirname_str if dirname_str else "."
            self.mark_done(1)
            self.set_instruction("Click Start Split")

    def start(self):
        if not self.pdf or not self.outdir:
            from tkinter import messagebox
            messagebox.showerror("Error", "Complete all steps first")
            return
        try:
            reader = PdfReader(self.pdf)
            total = len(reader.pages)
            for i, page in enumerate(reader.pages, 1):
                w = PdfWriter()
                w.add_page(page)
                with open(f"{self.outdir}/page_{i}.pdf", "wb") as f:
                    w.write(f)
                self.progress["value"] = int((i / total) * 100)
            self.mark_done(2)
            self.set_instruction("Split completed successfully")
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Error", f"Split failed: {str(e)}")
