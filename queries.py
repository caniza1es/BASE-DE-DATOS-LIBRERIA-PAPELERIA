from tkinter import E, INSERT
import psycopg2
books = []
stationers = []

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

def books_id():
    return """
    SELECT books.id
    from books
    """
    
def stationers_id():
    return """
    SELECT stationers.id
    from stationers
    """

def receipts_desc(limit=100):
    return """
    SELECT * FROM receipts_desc,receipts
    WHERE receipts_desc.id = receipts.id
    ORDER BY receipts.time DESC
    limit {0}
    """.format(limit)

def total_employees():
    return """
    SELECT * FROM employees
    ORDER by branch"""

def total_clients():
    return """
    SELECT * FROM clients
    ORDER BY name ASC"""

def total_books():
    return """
    SELECT B.id,B.title, B.editorial,B.author,B.genre,SUM(I.amount) as total
    FROM books as B, products as P, inventories as I
    WHERE B.id = p.id
    AND I.product = P.id
    GROUP BY B.id,B.title,B.editorial,B.author,B.genre
    """

def total_stationers():
    return """
    SELECT S.id, S.des, S.company, SUM(I.amount) AS total
    FROM stationers as S, products as P, inventories as I
    WHERE S.id = P.id
    AND I.product = P.id
    GROUP BY S.id,S.des,S.company
    """
def products_sold():
    return """
    SELECT P.id, COUNT(P.id) AS sold
    FROM products as P,receipts_desc as R
    WHERE R.product = P.id
    GROUP BY P.id
    """
def msold_product(limit = 0):
    query = """
    SELECT M.id, M.sold, RANK () OVER ( 
		ORDER BY M.sold DESC
	)sold_rank
    FROM ({0}) AS M
    """.format(products_sold())
    if not limit:
        return query
    else:
        return query + " LIMIT {0}".format(limit)

def msold_stationer(limit = 0):
    query = """ 
    SELECT B.id,B.des,B.company,M.sold,
    RANK () OVER ( 
        ORDER BY M.sold DESC
    ) sold_rank 
    FROM stationers as B, ({0}) as M
    WHERE B.id = M.id 
    """.format(msold_product())
    if not limit:
        return query
    else:
        return query + " LIMIT {0}".format(limit)
def msold_book(limit = 0):
    query = """	
    SELECT B.id as book_id ,B.title as book_title ,A.name as author_name,M.sold as quantity,
  	RANK () OVER ( 
		ORDER BY M.sold DESC
	) sold_rank 
  	FROM books as B, ({0}) as M,authors as A
  	WHERE B.id = M.id and A.id = B.author
    """.format(msold_product())
    if not limit:
        return query
    else:
        return query + " LIMIT {0}".format(limit)

def branch_employees(branch):
    return """
    SELECT * FROM employees
    WHERE employees.branch = '{0}'
    """.format(branch)

def receipt_detail(id):
    return"""
      SELECT * FROM receipts_desc,products
      WHERE receipts_desc.id = {0}
      AND receipts_desc.product = products.id
    """.format(id)

def quantity_product(id):
    return """
    SELECT inventories.branch,inventories.amount from inventories
    where inventories.product = {0}
    """.format(id)

def product_desc(id):
    table = "Books" if id in books else "Stationers"
    return """SELECT * FROM {0}
              WHERE {0}.id = {1}""".format(table,id)

def generarFactura(con,client,employee):
    from datetime import datetime
    from random import randint
    from random import choice
    im = randint(4000,8000)
    a = datetime.now()
    quer = """INSERT INTO receipts(id,time,client,employee) VALUES({0},'{1}',{2},{3});""".format(im,a,client,employee)
    br = con.cursor()
    br.execute("SELECT employees.branch from employees where employees.cc = {0}".format(employee))
    br = choice(br.fetchall())
    br = choice(br)
    print("factura ",im)
    while True:
        p = input("producto: ")
        if(p=="exit"):
            break
        p = int(p)
        plp = con.cursor()
        plp.execute(quantity_product(p) + """AND inventories.branch = '{0}'""".format(br))
        print("cantidad en inventario: ")
        mmmm = plp.fetchall()
        print(mmmm)
        am = int(input("cantidad: "))
        quer += """INSERT INTO receipts_desc(id,product,amount) VALUES({0},{1},{2});""".format(im,p,am)
    cursor = con.cursor()
    cursor.execute(quer)
    con.commit()
    cursor.execute("""select M.idd from ({0}) as M""".format(receipt_detail(im)))
    m = cursor.fetchall()
    for i in m:
        i = choice(i)
        print(type(i))
        a = """CALL insert_remove({0});""".format(i)
        cursor.execute(a)
        con.commit()
    return quer,im

def agregarCliente(con):
    cursor = con.cursor()
    cc = int(input("cc: "))
    name = input("nombre: ")
    email = input("email: ")
    phone = int(input("telefono: "))
    query = """INSERT INTO Clients(cc,name,email,phone) VALUES({0},'{1}','{2}',{3})""".format(cc,name,email,phone)
    cursor.execute(query)
    con.commit()

def eliminarFactura(con,idfactura):
    cursor = con.cursor()
    query = """DELETE FROM ingresos WHERE ingresos.r_id = {0}""".format(idfactura)
    cursor.execute(query)
    con.commit()

def actualizarInventario(con,administrador,producto,cantidad):
    from random import choice
    br = con.cursor()
    br.execute("SELECT employees.branch from employees where employees.cc = {0}".format(administrador))
    br = choice(br.fetchall())
    br = choice(br)
    plp = con.cursor()
    plp.execute(quantity_product(producto) + """AND inventories.branch = '{0}'""".format(br))
    print("cantidad en inventario: ")
    mmmm = plp.fetchall()
    print(mmmm)
    quer = """UPDATE inventories SET amount = {0} WHERE branch = '{1}' and product = {2};""".format(cantidad,br,producto)
    cursor = con.cursor()
    cursor.execute(quer)
    con.commit()
    
def agregarEmpleado(psy):
    from datetime import date
    cc = int(input("cc: "))
    name = input("nombre empleado: ")
    branch = input("sucursal: ")
    occupation = input("ocupacion: ")
    working_since = date.today()
    email = input("email:")
    quer = """INSERT INTO Employees(cc,name,branch,occupation,working_since,email) VALUES({0},'{1}','{2}','{3}','{4}','{5}')""".format(cc,name,branch,occupation,working_since,email)
    cursor = psy.cursor()
    cursor.execute(quer)
    psy.commit()

def agregarProducto(con):
    cursor = con.cursor()
    quer = """INSERT INTO Products(id,price,price_bought)VALUES({},{},{})""".format(int(input("id: ")),int(input("precio: ")),int(input("precio_compra: ")))
    cursor.execute(quer)
    con.commit()

def asignarProducto(con):
    product = int(input("id: "))
    tipo = input("tipo: ")
    if tipo == "estacionario":
        id = product
        des = input("des: ")
        company = input("comp: ")
        quer = """INSERT INTO Stationers(id,des,company) VALUES({0},'{1}',{2})""".format(id,des,company)
        cursor = con.cursor()
        cursor.execute(quer)
        con.commit()
    elif tipo == "libro":
        id = product
        titulo = input("titulo: ")
        editorial = int(input("editorial: "))
        author = int(input("autor: "))
        pub_date = input("fecha_publicacion: ")
        genre = input("genero: ")
        quer = """INSERT INTO Books(id,titulo,editorial,author,pub_date,genre)VALUES({0},{1},{2},{3},{4},{5})""".format(id,titulo,editorial,author,pub_date,genre)
        cursor = con.cursor()
        cursor.execute(quer)
        cursor.commit()

def agregarAutor(con):
    id = int(input("id: "))
    name = input("nombre: ")
    email = input("email: ")
    quer = "INSERT INTO Authors(id,name,email) VALUES({0},'{1}','{2}')".format(id,name,email)
    cursor = con.cursor()
    cursor.execute(quer)
    con.commit()

def agregarCompania(con):
    id = int(input("id: "))
    name = input("nombre compañia: ")
    contacto = int(input("telefono contacto: "))
    quer = """INSERT INTO Companies(id,name,contacto) VALUES({0},'{1}',{2})""".format(id,name,contacto)
    cursor = con.cursor()
    cursor.execute(quer)
    con.commit()