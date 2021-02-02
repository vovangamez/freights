import New_Orderer
import New_Trailer
import New_Truck
import New_driver
import New_order
import open_trucks
import Open_Drivers
import Open_Trailers
import Open_orderers
import Open_orders

def help_me():
    helpmain = Toplevel(root)
    helpmain.title('Помощь')
    label1 = Label(helpmain, text='Помощь!')
    label1.pack()
    label2 = Label(helpmain, text='')
    label2.pack()
    helpmain.geometry('400x200')


def about_programm():
    about_form = Toplevel(root)
    about_form.title('О программе')
    labelAbout = Label(about_form, text='Программа разработана \nАлпеевым Владимиром\nВерсия 1.0', font='Arial 10')
    labelAbout.pack()
    about_form.mainloop()


from tkinter import *


def open_new_object():
    newObjectForm = Toplevel(root)
    newObjectForm.title('Добавить запись')
    labelspace1 = Label(newObjectForm, text='       ')
    labelspace2 = Label(newObjectForm, text='       ')
    labelspace1.grid(row=0, column=0)
    label1 = Label(newObjectForm, text='Создать новую запись про', font='times 14')
    label1.grid(row=0, column=1)
    labelspace2.grid(row=0, column=2)
    OrdersTableButton = Button(newObjectForm, text="Заказ", height=2, width=12, command=New_order.new_order)
    OrdersTableButton.grid(row=1, column=1)
    OrderersTableButton = Button(newObjectForm, text="Заказчик", height=2, width=12, command=New_Orderer.new_orderer)
    OrderersTableButton.grid(row=2, column=1)
    DriverTableButton = Button(newObjectForm, text="Водитель", height=2, width=12, command=New_driver.new_driver)
    DriverTableButton.grid(row=3, column=1)
    TruckTableButton = Button(newObjectForm, text="Тягач", height=2, width=12, command=New_Truck.new_truck)
    TruckTableButton.grid(row=4, column=1)
    TrailerTableButton = Button(newObjectForm, text='Прицеп', height=2, width=12, command=New_Trailer.new_trailer)
    TrailerTableButton.grid(row=5, column=1)
    newObjectForm.mainloop()


def open_form():
    openform = Toplevel(root)
    openform.title('Открытие формы')
    labelspace1 = Label(openform, text='       ')
    labelspace2 = Label(openform, text='       ')
    labelspace1.grid(row=0, column=0)
    labelspace2.grid(row=0, column=2)
    label1 = Label(openform, text='Открытие формы', font='times 14')
    label1.grid(row=0, column=1)
    TruckTableButton = Button(openform, text="Тягачи", height=2, width=12, command= open_trucks.open_trucks)
    TruckTableButton.grid(row=4, column=1)
    TrailerTableButton = Button(openform, text='Прицепы', height=2, width=12,command=Open_Trailers.open_trailers)
    TrailerTableButton.grid(row=5, column=1)
    DriverTableButton = Button(openform, text="Водители", height=2, width=12, command= Open_Drivers.open_Drivers)
    DriverTableButton.grid(row=3, column=1)
    OrderersTableButton = Button(openform, text="Заказчики", height=2, width=12,command=Open_orderers.open_Orderer)
    OrderersTableButton.grid(row=2, column=1)
    OrdersTableButton = Button(openform, text="Заказы", height=2, width=12, command = Open_orders.open_orders)
    OrdersTableButton.grid(row=1, column=1)
    openform.mainloop()


root = Tk()
root.title('Основное окно системы')
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Новый', command=open_new_object)
filemenu.add_command(label='Открыть...', command=open_form)
filemenu.add_command(label='Сохранить')
filemenu.add_command(label='Выход', command=root.destroy)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label='Помощь', command=help_me)
helpmenu.add_command(label='О программе', command=about_programm)
mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)
label = Label(root, text='Информационая база \n"Грузоперевозки"', font='times 16', fg='#a00')
label.pack()
root.mainloop()
