import tkinter as tk
from tkinter import ttk
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import New_driver
from tkinter import messagebox

def delete(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = 'delete from drivers where iddriver=%s'
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
        open_Drivers()

def remove_driver_form(window):
    removeDriverForm=tk.Toplevel(window)
    removeDriverForm.title('Удаление записи')
    label=tk.Label(removeDriverForm,text = 'Удаление записи')
    label.grid(row=0,column=1)
    labelID=tk.Label(removeDriverForm, text = 'ID удаляемого водителя')
    labelID.grid(row=1,column=0)
    entryID=tk.Entry(removeDriverForm)
    entryID.grid(row=1,column=1)
    buttonDelete=tk.Button(removeDriverForm,text='Удалить!',command =lambda: delete(entryID.get(),window))
    buttonDelete.grid(row=2,column=1)
    removeDriverForm.mainloop()

def open_Drivers():
    window=tk.Tk()
    window.title('Водители')
    tree=ttk.Treeview(window)
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drivers")
    Drivers= cursor.fetchall()
    label=tk.Label(window, text = 'Таблица водителей')
    label.grid(row=0,column=0)
    tree['show']='headings'
    tree['columns']=('IDDriver', 'Name', 'telephone', 'email')
    tree.column('IDDriver', width=70, minwidth=50, anchor=tk.CENTER)
    tree.column('Name', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('telephone', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('email', width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading('IDDriver',text = 'ID Водителя', anchor = tk.CENTER)
    tree.heading('Name', text='ФИО Водителя', anchor=tk.CENTER)
    tree.heading('telephone',text='Номер телефона', anchor=tk.CENTER)
    tree.heading('email', text='Адрес электронной почты', anchor=tk.CENTER)
    i=0
    for ro in Drivers:
        tree.insert('',i, text="", values = (ro[0], ro[1], ro[2], ro[3]))
        i=i+1
    tree.grid(row=1, column = 0)
    frame = tk.Frame(window)
    frame.grid(row=2, column=0)
    AddButton = tk.Button(frame, text='Добавить водителя', command=New_driver.new_driver)
    AddButton.grid(row=0, column=0)
    removeButton = tk.Button(frame, text='Удалить водителя', command = lambda: remove_driver_form(window))
    removeButton.grid(row=0, column=1)
