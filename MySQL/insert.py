from mysql.connector import MySQLConnection, Error

from python_mysql_dbconfig import read_db_config


def insert_truck(truckmodel,power,gosnumber,cost):
    query = "INSERT INTO trucks(truckmodel,power,gosnumber,cost) VALUES(%s,%s,%s,%s)"
    args = (truckmodel,power,gosnumber,cost)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
