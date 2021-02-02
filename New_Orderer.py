from tkinter import *
import insert

def new_orderer():
    newOrdererForm = Tk()
    newOrdererForm.title('Новый заказчик')
    label = Label(newOrdererForm, text='Добавление нового заказчика',fg='#909')
    label.grid(row=0, column=1)
    labelName = Label(newOrdererForm, text='Наименование заказчика')
    labelName.grid(row=1, column=0)
    textName = Entry(newOrdererForm)
    textName.grid(row=1, column=1)
    labelTelephone = Label(newOrdererForm, text='Номер телефона')
    labelTelephone.grid(row=2, column=0)
    textTelephone = Entry(newOrdererForm)
    textTelephone.grid(row=2, column=1)
    labelEMAIL = Label(newOrdererForm, text='Адрес электронной почты')
    labelEMAIL.grid(row=3, column=0)
    textEMAIL = Entry(newOrdererForm)
    textEMAIL.grid(row=3, column=1)
    AddButton = Button(newOrdererForm, text='Добавить', command=lambda : insert.insert_orderer(textName.get(), textTelephone.get(), textEMAIL.get()))
    AddButton.grid(row=4, column=1)
