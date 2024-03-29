import os
import subprocess
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing, Rect, String, Line, Group)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

root = Tk()
root.title("Doctor's Card")
root.geometry("600x550+300+100")

pdfmetrics.registerFont(TTFont('Trebuchet MS', '..\\fonts\\trebuc.ttf'))
pdfmetrics.registerFont(TTFont('Caladea', '..\\fonts\\Caladea-Bold.ttf'))
pdfmetrics.registerFont(TTFont('ErasMediumITC', '..\\fonts\\ErasMediumITC.ttf'))
pdfmetrics.registerFont(TTFont('FRADM', '..\\fonts\\FRADM.ttf'))

directory_name = r"Silent_Garden_Detalis\Doctor Card"
home_directory = os.path.expanduser("~")
directory_path = os.path.join(home_directory, directory_name)

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

selection_path = os.path.join(directory_path, "card.png")

def main():
    label_main = ttk.Label(root, text="Doctor's Card", bootstyle=SUCCESS, font="Helvetica 20 bold").grid(row=0, column=0, sticky=W, padx=10)
    label1 = ttk.Label(root, text="Name", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=0, sticky=W, pady=10, padx=10) 
    label2 = ttk.Label(root, text="Name 2", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=0, sticky=W, pady=10, padx=10) 
    label3 = ttk.Label(root, text="Age", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=0, sticky=W, pady=10, padx=10) 
    label4 = ttk.Label(root, text="Birthday", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=0, sticky=W, pady=10, padx=10) 
    label5 = ttk.Label(root, text="Package", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=0, sticky=W, pady=10, padx=10) 
    label6 = ttk.Label(root, text="Arrival", font="Helvetica 15", bootstyle=DARK).grid(row=6, column=0, sticky=W, pady=10, padx=10) 
    label7 = ttk.Label(root, text="Departure", font="Helvetica 15", bootstyle=DARK).grid(row=8, column=0, sticky=W, pady=10, padx=10) 
    
    label20 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=1, column=1, sticky=W, pady=10, padx=10)
    label21 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=2, column=1, sticky=W, pady=10, padx=10)
    label22 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=3, column=1, sticky=W, pady=10, padx=10)
    label23 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=4, column=1, sticky=W, pady=10, padx=10)
    label24 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=5, column=1, sticky=W, pady=10, padx=10)
    label25 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=7, column=1, sticky=W, pady=10, padx=10)
    label26 = ttk.Label(root, text=":", font="Helvetica 15", bootstyle=DARK).grid(row=8, column=1, sticky=W, pady=10, padx=10)
    
    global input_name
    input_name = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=30)
    input_name.grid(row=1, column=2, columnspan=3, sticky=W, pady=10, padx=10)

    global input_name_2
    input_name_2 = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=30)
    input_name_2.grid(row=2, column=2, columnspan=3, sticky=W, pady=10, padx=10)

    global input_age
    input_age = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=6)
    input_age.grid(row=3, column=2, sticky=W, pady=10, padx=10)
    label_age = ttk.Label(root, text="years", font="Arial 12", bootstyle=DARK).grid(row=3, column=3, sticky=W, pady=10, padx=10)
    global input_birthday
    input_birthday = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_birthday.grid(row=4, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    package_values = ["Ayurveda Regeneration Package", "Ayurveda Panchakarma Package", "Ayurveda Slimming Package"]
    global input_package
    input_package = ttk.Combobox(root, values=package_values, width=28, state='readonly', font='Arial 12')
    input_package.grid(row=5, column=2, columnspan=3, sticky=W, pady=8, padx=8)
    input_package.current(0)
    
    global input_arrival
    input_arrival = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_arrival.grid(row=6, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    input_arrival.insert(END, "YYYY-MM-DD")
    
    global input_Departure
    input_Departure = ttk.Entry(root, font="Arial 12", bootstyle=DARK, width=11)
    input_Departure.grid(row=8, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    input_Departure.insert(END, "YYYY-MM-DD")

    def first_checkbutton_checked():
        global first_checkbutton_checked_now
        first_checkbutton_checked_now = var1.get()
        if first_checkbutton_checked_now:
            input_time1.config(state="normal", bootstyle=DARK)
        else:
            input_time1.config(state="disabled", bootstyle=LIGHT)

    global var1
    var1 = IntVar()
    checkbox_notimespecified1 = ttk.Checkbutton(root, text="Time Not Specified", variable=var1, onvalue=0, offvalue=1, command=first_checkbutton_checked)
    checkbox_notimespecified1.grid(row=7, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    global input_time1
    input_time1 = ttk.Entry(root, font="Arial 12", bootstyle=LIGHT, width=7, state="disabled")
    input_time1.grid(row=7, column=4, sticky=W, padx=10, pady=10)

    def second_checkbutton_checked():
        global second_checkbutton_checked_now
        second_checkbutton_checked_now = var2.get()
        if second_checkbutton_checked_now:
            input_time2.config(state="normal", bootstyle=DARK)
        else:
            input_time2.config(state="disabled", bootstyle=LIGHT)

    global var2
    var2 = IntVar()
    checkbox_notimespecified2 = ttk.Checkbutton(root, text="Time Not Specified", variable=var2, onvalue=0, offvalue=1, command=second_checkbutton_checked)
    checkbox_notimespecified2.grid(row=9, column=2, columnspan=3, sticky=W, padx=10, pady=10)
    
    global input_time2
    input_time2 = ttk.Entry(root, font="Arial 12", bootstyle=LIGHT, width=7, state="disabled")
    input_time2.grid(row=9, column=4, sticky=W, padx=10, pady=10)
    

    button_quit = ttk.Button(root, text='Quit', style='info.outline.TButton', command=quit_command)
    button_quit.grid(row=10, column=3, sticky=W, padx=10, pady=10)
    
    button_create = ttk.Button(root, text='Create', style='success.TButton', command=creating_card)
    button_create.grid(row=10, column=4, sticky=W, padx=10, pady=10)

    root.mainloop()

def quit_command():
    root.quit()

def creating_card():
    card_height = 700
    card_width = 300
    drawing = Drawing(card_height, card_width)
    
    font_trebuchet = 'Trebuchet MS'
    font_caladea = 'Caladea'
    font_eras = 'ErasMediumITC'
    font_fradm = 'FRADM'
    
    font_size_for_name = 45
    font_size_for_4 = 20
    font_size_for_package = 30

    name_String = input_name.get()
    name_2_String = ""
    if input_name_2.get() == None or len(input_name_2.get().strip()) == 0:
        name_2_String = ""
    else:
        name_2_String = input_name_2.get()
        card_height += 30

    age_String = ""
    if input_age.get() == None or len(input_age.get().strip()) == 0 :
       age_String = "" 
    else:
        age_String = f"Age : {input_age.get()} years"

    birthday_String = ""
    if input_birthday.get() == None or len(input_birthday.get().strip()) == 0 :
        birthday_String = ""
    else:
        birthday_String = f"Birthday : {input_birthday.get()}"

    package_String = input_package.get()
    
    arrival_time_string = ""
    if var1.get() == 0 :
        arrival_time_string = "Time Not Specified"
    else:
        arrival_time_string = input_time1.get()

    departure_time_string = ""
    if var2.get() == 0 :
        departure_time_string = "Time Not Specified"
    else:
        departure_time_string = input_time2.get()


    arrival_String = f"Arrival : {input_arrival.get()} [ {arrival_time_string} ]"
    departure_String = f"Departure : {input_Departure.get()} [ {departure_time_string} ]"

    name_Width = pdfmetrics.stringWidth(name_String, font_trebuchet, font_size_for_name)
    name_Width_2 = pdfmetrics.stringWidth(name_2_String, font_trebuchet, font_size_for_name)
    xcenter_name = (drawing.width - name_Width) / 2
    xcenter_name_2 = (drawing.width - name_Width_2) / 2

    position_age_birthday = drawing.width - 590

    package_Width = pdfmetrics.stringWidth(package_String, font_eras, font_size_for_package)
    xcenter_package = (drawing.width - package_Width) / 2

    position_arrival_departure = drawing.width - 620

    name = String(xcenter_name, 250, name_String, fontSize=font_size_for_name, fillColor=colors.black, fontName=font_trebuchet)
    name_2 = String(xcenter_name_2, 205, name_2_String, fontSize=font_size_for_name, fillColor=colors.black, fontName=font_trebuchet)
    age = String(position_age_birthday, 160, age_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_caladea)
    birthday = String(position_age_birthday, 135, birthday_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_caladea)
    package = String(xcenter_package, 90, package_String, fontSize=font_size_for_package, fillColor=colors.black, fontName=font_eras)
    arrival = String(position_arrival_departure, 45, arrival_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_fradm)
    departure = String(position_arrival_departure, 20, departure_String, fontSize=font_size_for_4, fillColor=colors.black, fontName=font_fradm)
    
    drawing.add(name)
    drawing.add(name_2)
    drawing.add(age)
    drawing.add(birthday)
    drawing.add(package)
    drawing.add(arrival)
    drawing.add(departure)

    try:
        drawing.save(formats=['png'], outDir=directory_path, fnRoot="card")
        downloads_path = r'C:\Users\Admin\Downloads'
        subprocess.Popen(f'explorer /select, {selection_path}')
        root.quit()
    except Exception as e:
        print("Error:   ", str(e))
        
if __name__ == "__main__":
    main()
