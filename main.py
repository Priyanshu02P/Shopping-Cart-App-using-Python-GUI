from base import EcommerceApp
from const import *
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    app = EcommerceApp(root, creds, product, discount_codes)
    
    style = ttk.Style()
    style.theme_use('clam')
    
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()