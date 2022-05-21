from queries import *
from IPython.display import display
from sqlalchemy import create_engine
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

books = []
stationers = []

def Connection(us,ps):
    try:
        return psycopg2.connect(database="LIBRERIAPAPELERIA",user=us,password=ps,host='127.0.0.1',port='5432'),create_engine('postgresql+psycopg2://{0}:{1}@localhost/LIBRERIAPAPELERIA'.format(us,ps))
    except:
        return 0
        
def defineProducts(conn):
    cursor = conn.cursor()
    cursor.execute(books_id())
    m = cursor.fetchall()
    for i in m:
        books.append(i[0])
    cursor.execute(stationers_id())
    m = cursor.fetchall()
    for i in m:
        stationers.append(i[0])

def switch(usr,engine,psy):
    while True:
        if usr == "caja":
            data = sqlio.read_sql_query(total_books(), engine)
            print("--------LIBROS---------")
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data) 
            print("--------ESTACIONARIOS---------")
            data = sqlio.read_sql_query(total_stationers(), engine)
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data) 
            print("1.Generar Factura")
            a = input(">")
            if a == "exit":
                break
            elif a == '1':
                generarFactura(psy,int(input("cliente: ")),int(input("empleado: ")))



def main():
    while True:
        usr = input("usuario: ")
        psy = input("contraseña: ")
        conpsy,conalch = Connection(usr,psy)
        if conpsy != 0:
            break
    defineProducts(conpsy)
    switch(usr,conalch,conpsy)



main()
    
    
