from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()
root.title("Doctor's Card")
root.geometry("600x500+300+100")

label_main = ttk.Label(root, text="Doctor's Card", bootstyle=SUCCESS, font="Helvetica 20 bold").grid(row=0, column=0, sticky=W, padx=10)
label1 = ttk.Label(root, text="Name", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=0, sticky=W, pady=10, padx=10)

label2 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=1, sticky=W, pady=10, padx=10)

input_name = ttk.Entry(root, font="Arial 12", bootstyle=LIGHT, width=30)
input_name.grid(row=1, column=2, sticky=W, pady=10, padx=10)

root.mainloop()
