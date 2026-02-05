import tkinter as tk
from tkinter import ttk

class BaseToolScreen:
    def __init__(self, parent, app, title):
        self.app = app
        self.cancelled = False

        self.frame = tk.Frame(parent, bg="#f4f6f8")
        self.frame.pack(fill="both", expand=True)

        tk.Label(
            self.frame, text=title,
            font=("Segoe UI", 20, "bold"),
            bg="#f4f6f8"
        ).pack(pady=10)

        # Steps
        self.steps = []
        for step in ["Select Files", "Save Output", "Processing"]:
            lbl = tk.Label(
                self.frame,
                text=f"⬜ {step}",
                font=("Segoe UI", 11),
                bg="#f4f6f8"
            )
            lbl.pack(anchor="center")
            self.steps.append(lbl)

        self.progress = ttk.Progressbar(self.frame, length=600)
        self.progress.pack(pady=20)

        self.instruction = tk.Label(
            self.frame,
            text="Select files to continue",
            font=("Segoe UI", 10),
            fg="gray",
            bg="#f4f6f8"
        )
        self.instruction.pack(pady=5)

        btn_frame = tk.Frame(self.frame, bg="#f4f6f8")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Cancel", width=15, command=self.cancel).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Home", width=15, command=app.show_home).pack(side="left", padx=10)

    def mark_done(self, index):
        self.steps[index].config(text="🟩 " + self.steps[index].cget("text")[2:])

    def set_instruction(self, text):
        self.instruction.config(text=text)

    def cancel(self):
        self.cancelled = True
