import tkinter as tk
from tkinter import ttk
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import New_order
from tkinter import messagebox

def otmena(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = "update orders set status='отменено' where idorder=%s "
        args=(ID,)
        print(args)
        cursor.execute(zapros,args)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
        window.destroy()
        open_orders()

def vipoln(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = "update orders set status='Завершено' where idorder=%s "
        args=(ID,)
        print(args)
        cursor.execute(zapros,args)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
        window.destroy()
        open_orders()

def delete(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = 'delete from orders where idorder=%s'
        args=(ID,)
        print(args)
        cursor.execute(zapros,args)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
        window.destroy()
        open_orders()

def remove_order_form(window):
    removeOrderForm=tk.Toplevel(window)
    removeOrderForm.title('Удаление записи')
    label=tk.Label(removeOrderForm,text = 'Удаление записи')
    label.grid(row=0,column=1)
    labelID=tk.Label(removeOrderForm, text = 'ID удаляемого заказа')
    labelID.grid(row=1,column=0)
    entryID=tk.Entry(removeOrderForm)
    entryID.grid(row=1,column=1)
    buttonDelete=tk.Button(removeOrderForm,text='Удалить!',command =lambda: delete(entryID.get(),window))
    buttonDelete.grid(row=2,column=1)
    removeOrderForm.mainloop()

def vipolnZakaz(window):
    vipolnOrderForm = tk.Toplevel(window)
    vipolnOrderForm.title('Изменение')
    label = tk.Label(vipolnOrderForm, text='Выполненный заказ')
    label.grid(row=0, column=1)
    labelID = tk.Label(vipolnOrderForm, text='ID выполненного заказа')
    labelID.grid(row=1, column=0)
    entryID = tk.Entry(vipolnOrderForm)
    entryID.grid(row=1, column=1)
    buttonDelete = tk.Button(vipolnOrderForm, text='Ввод!', command=lambda: vipoln(entryID.get(), window))
    buttonDelete.grid(row=2, column=1)
    vipolnOrderForm.mainloop()

def otmenaZakaz(window):
    otmenaOrderForm = tk.Toplevel(window)
    otmenaOrderForm.title('Изменение')
    label = tk.Label(otmenaOrderForm, text='Отмена заказа')
    label.grid(row=0, column=1)
    labelID = tk.Label(otmenaOrderForm, text='ID отменяемого заказа')
    labelID.grid(row=1, column=0)
    entryID = tk.Entry(otmenaOrderForm)
    entryID.grid(row=1, column=1)
    buttonDelete = tk.Button(otmenaOrderForm, text='Ввод!', command=lambda: otmena(entryID.get(), window))
    buttonDelete.grid(row=2, column=1)
    otmenaOrderForm.mainloop()


def open_orders():
    window=tk.Tk()
    window.title('Заказы')
    tree=ttk.Treeview(window)
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("""SELECT 
                        orders.idorder,
                        orderers.name, 
                        trucks.truckmodel,
                        trailers.nametrailer,
                        drivers.name, 
                        orders.cargotype,
                        orders.weight,
                        orders.cost,
                        orders.timedostav,
                        orders.status,
                        orders.start,
                        orders.end
                        FROM orders, trucks, trailers, orderers, drivers 
                        where trucks.idtruck=orders.truck and orderers.idorderer=orders.orderer and trailers.idtrailer=orders.trailer and drivers.iddriver=orders.driver
                        order by orders.idorder""")
    orders = cursor.fetchall()
    label=tk.Label(window, text = 'Таблица заказов')
    label.grid(row=0,column=0)
    tree['show']='headings'
    tree['columns']=('ID', 'Orderer', 'truck', 'trailer', 'driver', 'type', 'weight', 'cost', 'timedostav', 'status', 'start', 'end')
    tree.column('ID', width=50, minwidth=50, anchor=tk.CENTER)
    tree.column('Orderer', width=130, minwidth=130, anchor=tk.CENTER)
    tree.column('driver', width=130, minwidth=130, anchor=tk.CENTER)
    tree.column('truck', width=130, minwidth=130, anchor=tk.CENTER)
    tree.column('trailer', width=130, minwidth=130, anchor=tk.CENTER)
    tree.column('type', width=100, minwidth=100, anchor=tk.CENTER)
    tree.column('weight', width=70, minwidth=70, anchor=tk.CENTER)
    tree.column('cost', width=70, minwidth=70, anchor=tk.CENTER)
    tree.column('timedostav', width=100, minwidth=100, anchor=tk.CENTER)
    tree.column('status', width=130, minwidth=130, anchor=tk.CENTER)
    tree.column('start', width=150, minwidth=150, anchor=tk.CENTER)
    tree.column('end', width=150, minwidth=150, anchor=tk.CENTER)
    tree.heading('ID',text = 'Заказ', anchor = tk.CENTER)
    tree.heading('Orderer', text='Заказчик', anchor=tk.CENTER)
    tree.heading('driver', text='Водитель', anchor=tk.CENTER)
    tree.heading('truck', text='Грузовик', anchor=tk.CENTER)
    tree.heading('trailer', text='Использумый прицеп', anchor=tk.CENTER)
    tree.heading('type', text='Тип груза', anchor=tk.CENTER)
    tree.heading('weight', text='Вес груза', anchor=tk.CENTER)
    tree.heading('cost', text='Стоимость доставки', anchor=tk.CENTER)
    tree.heading('timedostav', text='Дата доставки', anchor=tk.CENTER)
    tree.heading('status', text='Статус заказа', anchor=tk.CENTER)
    tree.heading('start', text='Место отправления', anchor=tk.CENTER)
    tree.heading('end', text='Место прибытия', anchor=tk.CENTER)
    i=0
    for ro in orders:
        tree.insert('',i, text="", values = (ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],ro[11]))
        i=i+1
    tree.grid(row=1, column = 0)
    frame = tk.Frame(window)
    frame.grid(row=2, column=0)
    AddButton = tk.Button(frame, text='Добавить заказ', command=New_order.new_order)
    AddButton.grid(row=0, column=0)
    ChangeStatusButtonV=tk.Button(frame,text='Изменить статус заказа\nна "Выполнено"',command=lambda: vipolnZakaz(window))
    ChangeStatusButtonV.grid(row=1, column=0)
    ChangeStatusButtonO = tk.Button(frame, text='Изменить статус заказа\nна "Отменено"',command=lambda: otmenaZakaz(window))
    ChangeStatusButtonO.grid(row=1, column=1)
    removeButton = tk.Button(frame, text='Удалить заказ', command = lambda: remove_order_form(window))
    removeButton.grid(row=0, column=1)
    cursor.close()
    conn.close()