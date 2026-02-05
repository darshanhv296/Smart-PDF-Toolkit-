import tkinter as tk
from ui.home import HomeScreen

class SmartPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart PDF Toolkit v1.0")
        self.root.geometry("900x550")
        self.root.resizable(False, False)

        self.container = tk.Frame(root, bg="#f4f6f8")
        self.container.pack(fill="both", expand=True)

        self.show_home()

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def show_home(self):
        self.clear()
        HomeScreen(self.container, self)

if __name__ == "__main__":
    root = tk.Tk()
    SmartPDFApp(root)
    root.mainloop()
