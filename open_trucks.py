import tkinter as tk
from tkinter import ttk
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import New_Truck
from tkinter import messagebox

def delete(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = 'delete from trucks where idtruck=%s'
        args=(ID,)
        print(args)
        cursor.execute(zapros,args)
        conn.commit()
    except:
        messagebox.showerror('Ошибка', "Удаляемый объект используется в таблице заказов")
    finally:
        cursor.close()
        conn.close()
        window.destroy()
        open_trucks()

def remove_truck_form(window):
    removetruckForm=tk.Toplevel(window)
    removetruckForm.title('Удаление записи')
    label=tk.Label(removetruckForm,text = 'Удаление записи')
    label.grid(row=0,column=1)
    labelID=tk.Label(removetruckForm, text = 'ID удаляемого грузовика')
    labelID.grid(row=1,column=0)
    entryID=tk.Entry(removetruckForm)
    entryID.grid(row=1,column=1)
    buttonDelete=tk.Button(removetruckForm,text='Удалить!',command =lambda: delete(entryID.get(),window))
    buttonDelete.grid(row=2,column=1)
    removetruckForm.mainloop()


def open_trucks():
    window=tk.Tk()
    window.title('Грузовики')
    tree=ttk.Treeview(window)
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trucks")
    trucks = cursor.fetchall()
    label=tk.Label(window, text = 'Таблица грузовиков')
    label.grid(row=0,column=0)
    tree['show']='headings'
    tree['columns']=('IDTruck', 'TruckModel', 'TruckPower', 'GosNumber', 'Cost')
    tree.column('IDTruck', width=70, minwidth=50, anchor=tk.CENTER)
    tree.column('TruckModel', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('TruckPower', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('GosNumber', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('Cost', width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading('IDTruck',text = 'ID Грузовика', anchor = tk.CENTER)
    tree.heading('TruckModel', text='Модель Грузовика', anchor=tk.CENTER)
    tree.heading('TruckPower', text='Мощность Грузовика(ЛС)', anchor=tk.CENTER)
    tree.heading('GosNumber', text='Государственный номер', anchor=tk.CENTER)
    tree.heading('Cost', text='Стоимость грузовика(р)', anchor=tk.CENTER)
    i=0
    for ro in trucks:
        tree.insert('',i, text="", values = (ro[0], ro[1], ro[2], ro[3], ro[4]))
        i=i+1
    tree.grid(row=1, column = 0)
    frame = tk.Frame(window)
    frame.grid(row=2, column=0)
    AddButton = tk.Button(frame, text='Добавить грузовик', command=New_Truck.new_truck)
    AddButton.grid(row=0, column=0)
    removeButton = tk.Button(frame, text='Удалить грузовик', command=lambda :remove_truck_form(window))
    removeButton.grid(row=0, column=1)
    cursor.close()
    conn.close()

