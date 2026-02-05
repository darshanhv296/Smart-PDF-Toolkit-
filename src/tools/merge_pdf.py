import threading
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from ui.base_tool import BaseToolScreen

class MergePDFScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "Merge PDF")
        self.files = []
        self.output = None

        self.add_button("Select PDF Files", self.select_files)
        self.add_button("Select output folder", self.save_output)
        self.add_button("Start Merge", self.start)

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    def select_files(self):
        self.files = filedialog.askopenfilenames(
            title="Select PDF Files to Merge",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if self.files:
            self.mark_done(0)
            self.set_instruction("Select output file name and location")

    def save_output(self):
        self.output = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if self.output:
            self.mark_done(1)
            self.set_instruction("Click Start Merge")

    def start(self):
        if len(self.files) < 2 or not self.output:
            messagebox.showerror("Error", "Complete all steps first")
            return
        threading.Thread(target=self.process, daemon=True).start()

    def process(self):
        if not self.output:
            messagebox.showerror("Error", "Output path not set")
            return
        try:
            merger = PdfMerger()
            total = len(self.files)
            for i, f in enumerate(self.files, 1):
                if self.cancelled:
                    merger.close()
                    return
                merger.append(f)
                self.progress["value"] = int((i / total) * 100)
            merger.write(self.output)
            merger.close()
            self.mark_done(2)
            self.set_instruction("Merge completed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Merge failed: {str(e)}")
