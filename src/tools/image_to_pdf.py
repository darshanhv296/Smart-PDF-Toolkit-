import threading
from tkinter import filedialog, messagebox
from PIL import Image
from ui.base_tool import BaseToolScreen

class ImageToPDFScreen(BaseToolScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app, "Image → PDF")
        self.images = []
        self.output = None

        self.add_button("Select Images", self.select_images)
        self.add_button("Select output folder", self.save_output)
        self.add_button("Start Conversion", self.start)

    def add_button(self, text, cmd):
        import tkinter as tk
        tk.Button(self.frame, text=text, width=35, command=cmd).pack(pady=4)

    def select_images(self):
        self.images = filedialog.askopenfilenames(
            title="Select Images to Convert to PDF",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp"), ("PNG Images", "*.png"), ("JPG Images", "*.jpg *.jpeg"), ("All Files", "*.*")]
        )
        if self.images:
            self.mark_done(0)
            self.set_instruction("Now select output file name and location")

    def save_output(self):
        self.output = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if self.output:
            self.mark_done(1)
            self.set_instruction("Click Start Conversion")

    def start(self):
        if not self.images or not self.output:
            messagebox.showerror("Error", "Complete all steps first")
            return
        threading.Thread(target=self.process, daemon=True).start()

    def process(self):
        if not self.output:
            messagebox.showerror("Error", "Output file not set")
            return
        try:
            imgs = []
            total = len(self.images)
            for i, p in enumerate(self.images, 1):
                if self.cancelled:
                    return
                imgs.append(Image.open(p).convert("RGB"))
                self.progress["value"] = int((i / total) * 100)

            if imgs:
                imgs[0].save(self.output, save_all=True, append_images=imgs[1:] if len(imgs) > 1 else [])
                self.mark_done(2)
                self.set_instruction("Conversion completed successfully")
            else:
                messagebox.showerror("Error", "No images loaded")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
