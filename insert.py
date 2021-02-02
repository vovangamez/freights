from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from tkinter import messagebox
import tkinter

def insert_truck(truckmodel, power, gosnumber, cost):
    if truckmodel == "":
        messagebox.showerror('Ошибка', 'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if power == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if gosnumber == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if cost == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    else:
        query = "INSERT INTO trucks(truckmodel,power,gosnumber,cost) VALUES(%s,%s,%s,%s)"
        args = (truckmodel, power, gosnumber, cost)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                messagebox.showinfo('Сообщение', 'запись добавлена в базу')
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()


def insert_trailer(NameTrailer, type, tonnage, gosnumber, cost):
    if NameTrailer == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if type == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if tonnage == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if gosnumber == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if cost == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    else:
        query = "INSERT INTO trailers(NameTrailer,type,tonnage,gosnumber,cost) VALUES(%s,%s,%s,%s,%s)"
        args = (NameTrailer, type, tonnage, gosnumber, cost)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                messagebox.showinfo('Сообщение', 'запись добавлена в базу')
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()


def insert_driver(name, tel, email):
    if name == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if tel == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if email == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    else:
        query = "INSERT INTO drivers(name,telephone,email) VALUES(%s,%s,%s)"
        args = (name, tel, email)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                messagebox.showinfo('Сообщение', 'запись добавлена в базу')
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()


def insert_orderer(name, tel, email):
    if name == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if tel == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    if email == "":
        messagebox.showerror('Ошибка',
                             'Отсутствуют необходимые параметры.\nЗаполните все поля формы и попробуйте снова')
        return 0
    else:
        query = "INSERT INTO orderers(name,telephone,email) VALUES(%s,%s,%s)"
        args = (name, tel, email)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                messagebox.showinfo('Сообщение', 'запись добавлена в базу')
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()


def insert_order(orderer, truck, driver, trailer, cargotype, cost, timedostav, start, end, weight):
    if orderer == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if driver == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if truck == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if trailer == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if cargotype == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if cost == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля ")
        return 0
    if timedostav == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if start == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    if end == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля ")
        return 0
    if weight == "":
        messagebox.showinfo("Ошибка!!!",
                            "Недостаточно информации для заполнения формы заказа\nЗаполните все поля")
        return 0
    else:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor(buffered=True)
        zapr = 'select idtrailer from trailers where nametrailer=%s'
        arg = (trailer,)
        cursor.execute(zapr, arg)
        trailers=cursor.fetchall()
        trailer = ''
        for item in trailers:
            item = list(item)
            trailer=item[0]
            print(trailers)
        zapr = 'select idtruck from Trucks where truckmodel=%s'
        arg = (truck,)
        cursor.execute(zapr, arg)
        trucks=cursor.fetchall()
        truck = ''
        for item in trucks:
            item = list(item)
            truck=item[0]
            print(trucks)
        zapr = 'select iddriver from drivers where name=%s'
        arg = (driver,)
        cursor.execute(zapr, arg)
        drivers=cursor.fetchall()
        driver = ''
        for item in drivers:
            item = list(item)
            driver=item[0]
            print(driver)
        zapr = 'select idorderer from orderers where name=%s'
        arg = (orderer,)
        cursor.execute(zapr, arg)
        orderers=cursor.fetchall()
        orderer = ''
        for item in orderers:
            item = list(item)
            orderer=item[0]
            print(orderer)
        status='Выполняется'
        zapr='select tonnage from trailers where idTrailer=%s'
        args=(trailer,)
        cursor.execute(zapr,args)
        tonnagez=cursor.fetchone()
        tonnage=int(tonnagez[0])
        try:
            weights=float(weight)
        except:
            messagebox.showerror('Ошибка!', 'Поле "Вес" имеет неправильный тип данных')
            return 0
        if weights > tonnage:
            messagebox.showinfo('Несоответствие',"Выбранный прицеп не расчитан на указанный вес")
            return 0
        query = 'INSERT INTO orders(orderer, driver, truck, trailer, cargotype,weight, cost, timedostav, status,start, end) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args = (orderer, driver, truck, trailer, cargotype, weight, cost, timedostav, status, start, end)
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                messagebox.showinfo('Сообщение', 'запись добавлена в базу')
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
