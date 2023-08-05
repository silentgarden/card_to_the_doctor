from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()
root.title("Doctor's Card")
root.geometry("600x500+300+100")

label_main = ttk.Label(root, text="Doctor's Card", bootstyle=SUCCESS, font="Helvetica 20 bold").grid(row=0, column=0, sticky=W, padx=10)
label1 = ttk.Label(root, text="Name", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=0, sticky=W, pady=10, padx=10) 
label2 = ttk.Label(root, text="Age", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=0, sticky=W, pady=10, padx=10) 
label3 = ttk.Label(root, text="Birthday", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=0, sticky=W, pady=10, padx=10) 
label4 = ttk.Label(root, text="Package", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=0, sticky=W, pady=10, padx=10) 
label5 = ttk.Label(root, text="Arrival", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=0, sticky=W, pady=10, padx=10) 

label20 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=1, sticky=W, pady=10, padx=10)
label21 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=1, sticky=W, pady=10, padx=10)
label22 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=1, sticky=W, pady=10, padx=10)
label23 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=1, sticky=W, pady=10, padx=10)
label24 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=1, sticky=W, pady=10, padx=10)

input_name = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=30) #, columnspan=5)
input_name.grid(row=1, column=2, sticky=W, pady=10, padx=10)
input_age = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=6)
input_age.grid(row=2, column=2, sticky=W, pady=10, padx=10)
label_age = ttk.Label(root, text="years", font="Arial 12", bootstyle=DARK).grid(row=2, column=3, sticky=W, pady=10, padx=10)
input_birthday = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
input_birthday.grid(row=3, column=2, sticky=W, padx=10, pady=10)

options = ttk.StringVar()
options.set("Select Package")

input_package = ttk.OptionMenu(root, options, "Ayurveda Regeneration Package", "Ayurveda Panchakarma Package", "Ayurveda Slimming Package")
input_package.grid(row=4, column=2, sticky=W, pady=8, padx=8)

input_arrival = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
input_arrival.grid(row=5, column=2, sticky=W, padx=10, pady=10)
input_arrival.insert(END, "YYYY-MM-DD")

var1 = IntVar()
checkbox_notimespecified = ttk.Checkbutton(root, text="Time Not Specified", variable=var1, style='custom.Checkbutton')
checkbox_notimespecified.grid(row=6, column=2, sticky=W, padx=10, pady=10)
style.configure('custom.TCheckbutton', font=('Arial', 12))

root.mainloop()
