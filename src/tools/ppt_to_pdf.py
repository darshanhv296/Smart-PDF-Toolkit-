import os
import threading
import subprocess
from typing import Sequence
from tkinter import filedialog, messagebox
from ui.base_tool import BaseToolScreen
from utils.soffice import find_soffice


class PPTToPDFScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "PPT → PDF")

        self.files: Sequence[str] = ()
        self.output_dir: str = ""

        self.add_button("Select PPT Files", self.select_files)
        self.add_button("Select Output Folder", self.select_output)
        self.add_button("Start Conversion", self.start)

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    # STEP 1
    def select_files(self):
        self.files = filedialog.askopenfilenames(
            title="Select PowerPoint Files to Convert",
            filetypes=[("PowerPoint Files", "*.ppt *.pptx"), ("All Files", "*.*")]
        )
        if self.files:
            self.mark_done(0)
            self.set_instruction("Now select output folder")

    # STEP 2
    def select_output(self):
        output_path = filedialog.asksaveasfilename(
            title="Select Output Folder for PDF Files",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if output_path and isinstance(output_path, str):
            dirname_str = os.path.dirname(output_path)
            self.output_dir = dirname_str if dirname_str else "."
            self.mark_done(1)
            self.set_instruction("Click Start Conversion")

    # STEP 3
    def start(self):
        if not self.files or not self.output_dir:
            messagebox.showerror("Error", "Complete all steps first")
            return
        threading.Thread(target=self.process, daemon=True).start()

    def process(self):
        if not self.output_dir:
            messagebox.showerror("Error", "Output directory not set")
            return
        try:
            soffice = find_soffice()
            if not soffice:
                messagebox.showerror("Error", "LibreOffice not found")
                return
            total = len(self.files)

            for i, file in enumerate(self.files, 1):
                if self.cancelled:
                    return

                subprocess.run(
                    [
                        soffice,
                        "--headless",
                        "--convert-to", "pdf",
                        file,
                        "--outdir", self.output_dir
                    ],
                    check=True
                )

                self.progress["value"] = int((i / total) * 100)

            self.mark_done(2)
            self.set_instruction("PPT to PDF conversion completed successfully")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
