from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing, Rect, String, Line, Group)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

root = Tk()
root.title("Doctor's Card")
root.geometry("600x500+300+100")

pdfmetrics.registerFont(TTFont('Trebuchet MS', 'C:\\Users\\Admin\\silentgardenapps\\App Fonts\\trebuc.ttf'))
pdfmetrics.registerFont(TTFont('Caladea', 'C:\\Users\\Admin\\silentgardenapps\\App Fonts\\Caladea-Bold.ttf'))
pdfmetrics.registerFont(TTFont('ErasMediumITC', 'C:\\Users\\Admin\\silentgardenapps\\App Fonts\\ErasMediumITC.ttf'))
pdfmetrics.registerFont(TTFont('FRADM', 'C:\\Users\\Admin\\silentgardenapps\\App Fonts\\FRADM.ttf'))

    
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
    
    global input_name
    input_name = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=30) #, columnspan=5)
    input_name.grid(row=1, column=2, columnspan=3, sticky=W, pady=10, padx=10)
    global input_age
    input_age = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=6)
    input_age.grid(row=2, column=2, sticky=W, pady=10, padx=10)
    label_age = ttk.Label(root, text="years", font="Arial 12", bootstyle=DARK).grid(row=2, column=3, sticky=W, pady=10, padx=10)
    global input_birthday
    input_birthday = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_birthday.grid(row=3, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    package_values = ["Ayurveda Regeneration Package", "Ayurveda Panchakarma Package", "Ayurveda Slimming Package"]
    global input_package
    input_package = ttk.Combobox(root, values=package_values, width=28, state='readonly', font='Arial 12')
    input_package.grid(row=4, column=2, columnspan=3, sticky=W, pady=8, padx=8)
    input_package.current(0)
    
    global input_arrival
    input_arrival = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_arrival.grid(row=5, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    input_arrival.insert(END, "YYYY-MM-DD")
    
    global input_Departure
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
    
    button_create = ttk.Button(root, text='Create', style='success.TButton', command=creating_card)
    button_create.grid(row=9, column=4, sticky=W, padx=10, pady=10)

    global input_name_value
    input_name_value = input_name.get()
    print(input_name_value)
    #input_age_value = input_age.get()
    #input_birthday_value = input_birthday.get()
    #input_package_value = input_package.get()
    #input_arrival_value = input_arrival.get()
    #input_Departure_value = input_Departure.get()

    root.mainloop()

def quit_command():
    root.quit()

def creating_card():
    drawing = Drawing(500, 300)
    
    font_trebuchet = 'Trebuchet MS'
    font_caladea = 'Caladea'
    font_eras = 'ErasMediumITC'
    font_fradm = 'FRADM'
    
    font_size_for_name = 45
    font_size_for_4 = 20
    font_size_for_package = 30

    name_String = input_name.get()
    age_String = input_age.get()
    birthday_String = input_birthday.get()
    package_String = input_package.get()
    arrival_String = input_arrival.get()
    departure_String = input_Departure.get()

    name_Width = pdfmetrics.stringWidth(name_String, font_trebuchet, font_size_for_name)
    xcenter_name = (drawing.width / 2) - (name_Width / 2)

    position_age_birthday = drawing.width - 420

    package_Width = pdfmetrics.stringWidth(package_String, font_eras, font_size_for_package)
    xcenter_package = (drawing.width - package_Width) / 2

    position_arrival_departure = drawing.width - 475

    name = String(xcenter_name, 250, name_String, fontSize=font_size_for_name, fillColor=colors.black, fontName=font_trebuchet)
    age = String(position_age_birthday, 210, age_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_caladea)
    birthday = String(position_age_birthday, 182, birthday_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_caladea)
    package = String(xcenter_package, 135, package_String, fontSize=font_size_for_package, fillColor=colors.black, fontName=font_eras)
    arrival = String(position_arrival_departure, 75, arrival_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_fradm)
    departure = String(position_arrival_departure, 40, departure_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_fradm)
    
    drawing.add(name)
    drawing.add(age)
    drawing.add(birthday)
    drawing.add(package)
    drawing.add(arrival)
    drawing.add(departure)
    drawing.save(formats=['pdf', 'png'], outDir=".", fnRoot="card")

if __name__ == "__main__":
    main()
