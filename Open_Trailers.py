import tkinter as tk
from tkinter import ttk
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import New_Trailer
from tkinter import messagebox

def delete(ID,window):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        zapros = 'delete from trailers where idtrailer=%s'
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
        open_trailers()

def remove_trailer_form(window):
    removetrailerForm=tk.Toplevel(window)
    removetrailerForm.title('Удаление записи')
    label=tk.Label(removetrailerForm,text = 'Удаление записи')
    label.grid(row=0,column=1)
    labelID=tk.Label(removetrailerForm, text = 'ID удаляемого прицепа')
    labelID.grid(row=1,column=0)
    entryID=tk.Entry(removetrailerForm)
    entryID.grid(row=1,column=1)
    buttonDelete=tk.Button(removetrailerForm,text='Удалить!',command =lambda: delete(entryID.get(),window))
    buttonDelete.grid(row=2,column=1)
    removetrailerForm.mainloop()

def open_trailers():
    window=tk.Tk()
    window.title("Прицепы")
    tree=ttk.Treeview(window)
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trailers")
    trailers = cursor.fetchall()
    label=tk.Label(window, text = 'Таблица прицепов')
    label.grid(row=0,column=0)
    tree['show']='headings'
    tree['columns']=('IDtrailer', 'nametrailer', 'Type','tonnage' ,'GosNumber', 'Cost')
    tree.column('IDtrailer', width=70, minwidth=50, anchor=tk.CENTER)
    tree.column('nametrailer', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('Type', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('tonnage', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('GosNumber', width=200, minwidth=200, anchor=tk.CENTER)
    tree.column('Cost', width=200, minwidth=200, anchor=tk.CENTER)
    tree.heading('IDtrailer',text = 'ID Прицепа', anchor = tk.CENTER)
    tree.heading('nametrailer', text='Модель прицепа', anchor=tk.CENTER)
    tree.heading('Type', text='Тип прицепа', anchor=tk.CENTER)
    tree.heading('tonnage', text='Грузоподъемность(т)', anchor=tk.CENTER)
    tree.heading('GosNumber', text='Государственный номер', anchor=tk.CENTER)
    tree.heading('Cost', text='Стоимость прицепа(р)', anchor=tk.CENTER)
    i=0
    for ro in trailers:
        tree.insert('',i, text="", values = (ro[0], ro[1], ro[2], ro[3], ro[4],ro[5]))
        i=i+1
    tree.grid(row=1, column = 0)
    frame = tk.Frame(window)
    frame.grid(row=2, column=0)
    AddButton = tk.Button(frame, text='Добавить прицеп', command=New_Trailer.new_trailer)
    AddButton.grid(row=0, column=0)
    removeButton = tk.Button(frame, text='Удалить прицеп', command = lambda : remove_trailer_form(window))
    removeButton.grid(row=0, column=1)
