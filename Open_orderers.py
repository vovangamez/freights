import tkinter as tk
from tkinter import ttk
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import New_Orderer
from tkinter import messagebox

def delete(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = 'delete from orderers where idorderer=%s'
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
        open_Orderer()

def remove_orderer_form(window):
    removeOrderForm=tk.Toplevel(window)
    removeOrderForm.title('Удаление записи')
    label=tk.Label(removeOrderForm,text = 'Удаление записи')
    label.grid(row=0,column=1)
    labelID=tk.Label(removeOrderForm, text = 'ID удаляемого заказчика')
    labelID.grid(row=1,column=0)
    entryID=tk.Entry(removeOrderForm)
    entryID.grid(row=1,column=1)
    buttonDelete=tk.Button(removeOrderForm,text='Удалить!',command =lambda: delete(entryID.get(),window))
    buttonDelete.grid(row=2,column=1)
    removeOrderForm.mainloop()

def open_Orderer():
    window=tk.Tk()
    window.title('Заказчики')
    tree=ttk.Treeview(window)
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderers")
    orderers= cursor.fetchall()
    label=tk.Label(window, text = 'Таблица Заказчиков')
    label.grid(row=0,column=0)
    tree['show']='headings'
    tree['columns']=('IDorderer', 'Name', 'telephone', 'email')
    tree.column('IDorderer', width=70, minwidth=50, anchor=tk.CENTER)
    tree.column('Name', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('telephone', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('email', width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading('IDorderer',text = 'ID Заказчика', anchor = tk.CENTER)
    tree.heading('Name', text='Наименование заказчика', anchor=tk.CENTER)
    tree.heading('telephone',text='Номер телефона', anchor=tk.CENTER)
    tree.heading('email', text='Адрес электронной почты', anchor=tk.CENTER)
    i=0
    for ro in orderers:
        tree.insert('',i, text="", values = (ro[0], ro[1], ro[2], ro[3]))
        i=i+1
    tree.grid(row=1, column = 0)
    frame=tk.Frame(window)
    frame.grid(row=2,column=0)
    AddButton=tk.Button(frame,text='Добавить заказчика', command =New_Orderer.new_orderer)
    AddButton.grid(row=0,column=0)
    removeButton=tk.Button(frame,text = 'Удалить заказчика',command=lambda: remove_orderer_form(window))
    removeButton.grid(row=0,column=1)
    cursor.close()
    conn.close()
