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
            print("2.Agregar Cliente")
            a = input(">")
            if a == "exit":
                break
            elif a == '1':
                generarFactura(psy,int(input("cliente: ")),int(input("empleado: ")))
            elif a == '2':
                agregarCliente(psy)
        elif usr == "caja_administrador":
            data = sqlio.read_sql_query(total_books(), engine)
            print("--------LIBROS---------")
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data) 
            print("--------ESTACIONARIOS---------")
            data = sqlio.read_sql_query(total_stationers(), engine)
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data) 
            print("1.Generar Factura")
            print("2.Agregar Cliente")
            print("3.Eliminar Factura")
            print("4.Actualizar inventario")
            a = input(">")
            if a == "exit":
                break
            elif a == '1':
                generarFactura(psy,int(input("cliente: ")),int(input("empleado: ")))
            elif a == '2':
                agregarCliente(psy)
            elif a == '3':
                eliminarFactura(psy,int(input("id factura: ")))
            elif a == '4':
                actualizarInventario(psy,int(input("cc administrador: ")),int(input("producto: ")),int(input("nueva cantidad: ")))
        elif usr == "administrador_sucursal":
            print("----------SUCURSALES-----------")
            data = sqlio.read_sql_query("""SELECT * from Branches""", engine)
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data) 
            print("----------EMPLEADOS-----------")
            data = sqlio.read_sql_query(total_employees(), engine)
            with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
                display(data)
            print("1.Actualizar inventario")
            print("2.Agregar Empleado")
            print("3.Agregar Producto")
            print("4.Asignar Producto")
            print("5.Agregar Autor")
            print("6.Agregar Compania")
            print("7.Consultas avanzadas")
            a = input(">")
            if a == "exit":
                break
            elif a == '1':
                actualizarInventario(psy,int(input("cc administrador: ")),int(input("producto: ")),int(input("nueva cantidad: ")))
            elif a == '2':
                agregarEmpleado(psy)
            elif a == '3':
                agregarProducto(psy)
            elif a == '4':
                asignarProducto(psy)
            elif a == '5':
                agregarAutor(psy)
            elif a == '6':
                agregarCompania(psy)


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
    
    
