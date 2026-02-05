import tkinter as tk
from tkinter import messagebox
from tools.merge_pdf import MergePDFScreen
from tools.split_pdf import SplitPDFScreen
from tools.word_to_pdf import WordToPDFScreen
from tools.ppt_to_pdf import PPTToPDFScreen
from tools.image_to_pdf import ImageToPDFScreen
from tools.pdf_to_word import PDFToWordScreen


TOOLS = {
    "Merge PDF": MergePDFScreen,
    "Split PDF": SplitPDFScreen,
    "Word → PDF": WordToPDFScreen,
    "PPT → PDF": PPTToPDFScreen,
    "Image → PDF": ImageToPDFScreen,
    "PDF → Word": PDFToWordScreen,
}

class HomeScreen:
    def __init__(self, parent, app):
        self.app = app
        frame = tk.Frame(parent)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="Smart PDF Toolkit", font=("Segoe UI", 20, "bold")).pack()
        tk.Label(frame, text="Offline • Secure • Modular", fg="gray").pack(pady=5)

        grid = tk.Frame(frame)
        grid.pack(pady=20)

        for i, tool in enumerate(TOOLS):
            tk.Button(
                grid,
                text=tool,
                width=25,
                height=2,
                command=lambda t=tool: self.open_tool(t)
            ).grid(row=i//3, column=i%3, padx=10, pady=10)

    def open_tool(self, name):
        self.app.clear()
        TOOLS[name](self.app.container, self.app)
