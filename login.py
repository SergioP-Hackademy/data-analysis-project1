import sqlite3

from sqlite3 import Error
from dotenv import dotenv_values
import re


def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    config = dotenv_values(".env")
    listas = list(config.items())
    entities = ( 1, 'Sergio', listas[0][1], 'admin', listas[1][1])
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, user text,email text, role text, password text)")
    data = cursorObj.execute("SELECT * FROM users where id = 1")

    if (data.fetchone() == None):
        cursorObj.execute('INSERT INTO users(id, user,email, role, password) VALUES( ?, ?, ?, ?, ?)', entities)
    
    con.commit()
    # con.close()


def loginn(email, password ):

    con = sql_connection()
    sql_table(con)

    data3 = con.execute("SELECT * FROM users where id = 1").fetchone() 
    for row in data3:
        # print(row)
        if(data3[2] == email and data3[4] == password and data3[3] == 'admin' ):
            
            return True
    return False


def validacion(email, password ):
    """Validacion de campo email y passgord lenght
    >>> validacion_credenciales('Cronos@test.com', 'testdelpass')
    true
    """
    expresion_regular_email = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    # Mínimo ocho caracteres, al menos una letra y un número:
    expresion_regular_password =r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(expresion_regular_email, email) is not None and  re.search(expresion_regular_password, password) is not None

# print(validacion_credenciales('luis@gmail@hotmail.com', 'Cronos210'))



# con = sql_connection()
# validacion_password('Cronos@test.com', 'testdelpass')



# sql_table(con)

# login_flag=loginn( 'Cronos@test.com', 'Cronos2111')
# print(login_flag)