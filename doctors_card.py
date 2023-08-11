from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()
root.title("Doctor's Card")
root.geometry("600x500+300+100")
    
def main():
    label_main = ttk.Label(root, text="Doctor's Card", bootstyle=SUCCESS, font="Helvetica 20 bold").grid(row=0, column=0, sticky=W, padx=10)
    label1 = ttk.Label(root, text="Name", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=0, sticky=W, pady=10, padx=10) 
    label2 = ttk.Label(root, text="Age", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=0, sticky=W, pady=10, padx=10) 
    label3 = ttk.Label(root, text="Birthday", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=0, sticky=W, pady=10, padx=10) 
    label4 = ttk.Label(root, text="Package", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=0, sticky=W, pady=10, padx=10) 
    label5 = ttk.Label(root, text="Arrival", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=0, sticky=W, pady=10, padx=10) 
    label6 = ttk.Label(root, text="Departure", font="Helvetica 15", bootstyle=DARK).grid(row=7, column=0, sticky=W, pady=10, padx=10) 
    
    label20 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=1, sticky=W, pady=10, padx=10)
    label21 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=1, sticky=W, pady=10, padx=10)
    label22 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=1, sticky=W, pady=10, padx=10)
    label23 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=1, sticky=W, pady=10, padx=10)
    label24 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=1, sticky=W, pady=10, padx=10)
    label25 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=7, column=1, sticky=W, pady=10, padx=10)
    
    input_name = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=30) #, columnspan=5)
    input_name.grid(row=1, column=2, columnspan=3, sticky=W, pady=10, padx=10)
    input_age = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=6)
    input_age.grid(row=2, column=2, sticky=W, pady=10, padx=10)
    label_age = ttk.Label(root, text="years", font="Arial 12", bootstyle=DARK).grid(row=2, column=3, sticky=W, pady=10, padx=10)
    input_birthday = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_birthday.grid(row=3, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    package_values = ["Ayurveda Regeneration Package", "Ayurveda Panchakarma Package", "Ayurveda Slimming Package"]
    input_package = ttk.Combobox(root, values=package_values, width=28, state='readonly', font='Arial 12')
    input_package.grid(row=4, column=2, columnspan=3, sticky=W, pady=8, padx=8)
    input_package.current(0)
    
    input_arrival = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_arrival.grid(row=5, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    input_arrival.insert(END, "YYYY-MM-DD")
    
    input_Departure = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_Departure.grid(row=7, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    input_Departure.insert(END, "YYYY-MM-DD")

    def first_checkbutton_checked():
        global first_checkbutton_checked_now
        first_checkbutton_checked_now = var1.get()
        if first_checkbutton_checked_now:
            input_time1.config(state="normal", bootstyle=DARK)
        else:
            input_time1.config(state="disabled", bootstyle=LIGHT)

    var1 = IntVar()
    checkbox_notimespecified1 = ttk.Checkbutton(root, text="Time Not Specified", variable=var1, onvalue=0, offvalue=1, command=first_checkbutton_checked)
    checkbox_notimespecified1.grid(row=6, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    input_time1 = ttk.Entry(root, font="Arial 12", bootstyle=LIGHT, width=7, state="disabled")
    input_time1.grid(row=6, column=4, sticky=W, padx=10, pady=10)

    def second_checkbutton_checked():
        global second_checkbutton_checked_now
        second_checkbutton_checked_now = var2.get()
        if second_checkbutton_checked_now:
            input_time2.config(state="normal", bootstyle=DARK)
        else:
            input_time2.config(state="disabled", bootstyle=LIGHT)

    var2 = IntVar()
    checkbox_notimespecified2 = ttk.Checkbutton(root, text="Time Not Specified", variable=var2, onvalue=0, offvalue=1, command=second_checkbutton_checked)
    checkbox_notimespecified2.grid(row=8, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    input_time2 = ttk.Entry(root, font="Arial 12", bootstyle=LIGHT, width=7, state="disabled")
    input_time2.grid(row=8, column=4, sticky=W, padx=10, pady=10)
    

    button_quit = ttk.Button(root, text='Quit', style='info.outline.TButton', command=quit_command)
    button_quit.grid(row=9, column=3, sticky=W, padx=10, pady=10)
    
    button_create = ttk.Button(root, text='Create', style='success.TButton')
    button_create.grid(row=9, column=4, sticky=W, padx=10, pady=10)

    def second_checked():
        input_time1.configure(state=NORMAL, bootstyle=DARK)

    root.mainloop()

def quit_command():
    root.quit()

main()
