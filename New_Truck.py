from tkinter import *
import insert


def new_truck():
    newTruckForm = Tk()
    newTruckForm.title('Новый грузовик')
    label = Label(newTruckForm, text='Добавление нового грузовика',fg='#909')
    label.grid(row=0, column=1)
    labelModel = Label(newTruckForm, text='Модель грузовика')
    labelModel.grid(row=1, column=0)
    textModel = Entry(newTruckForm)
    textModel.grid(row=1, column=1)
    labelPower = Label(newTruckForm, text='Мощность (лс)')
    labelPower.grid(row=2, column=0)
    textPower = Entry(newTruckForm)
    textPower.grid(row=2, column=1)
    labelGosNumber = Label(newTruckForm, text='ГосНомер')
    labelGosNumber.grid(row=3, column=0)
    textNumber = Entry(newTruckForm)
    textNumber.grid(row=3, column=1)
    labelCost = Label(newTruckForm, text='Стоимость (р)')
    labelCost.grid(row=4, column=0)
    textCost = Entry(newTruckForm)
    textCost.grid(row=4, column=1)
    AddButton = Button(newTruckForm, text='Добавить', command=lambda : insert.insert_truck(textModel.get(), textPower.get(), textNumber.get(), textCost.get()))
    AddButton.grid(row=5, column=1)
