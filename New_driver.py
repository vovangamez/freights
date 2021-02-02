from tkinter import *
import insert

def new_driver():
    newDriverForm = Tk()
    newDriverForm.title('Новый водитель')
    label = Label(newDriverForm, text='Добавление нового водителя',fg='#909')
    label.grid(row=0, column=1)
    labelName = Label(newDriverForm, text='ФИО Водителя')
    labelName.grid(row=1, column=0)
    textName = Entry(newDriverForm)
    textName.grid(row=1, column=1)
    labelTelephone = Label(newDriverForm, text='Номер телефона')
    labelTelephone.grid(row=2, column=0)
    textTelephone = Entry(newDriverForm)
    textTelephone.grid(row=2, column=1)
    labelEMAIL = Label(newDriverForm, text='Адрес электронной почты')
    labelEMAIL.grid(row=3, column=0)
    textEMAIL = Entry(newDriverForm)
    textEMAIL.grid(row=3, column=1)
    AddButton = Button(newDriverForm, text='Добавить', command=lambda : insert.insert_driver(textName.get(), textTelephone.get(), textEMAIL.get()))
    AddButton.grid(row=4, column=1)