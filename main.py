import psycopg2

books = []
stationers = []

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
    
def msold_book(limit = 0):
    query = """	
    SELECT B.id,B.title,A.name,M.sold,
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

def product_desc(id):
    table = "Books" if id in books else "Stattioners"
    return """SELECT * FROM {0}
              WHERE {0}.id = {1}""".format(table,id)

def Connection(ps):
    try:
        return psycopg2.connect(database="LIBRERIAPAPELERIA",user='postgres',password=ps,host='127.0.0.1',port='5432')
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

def main():
    while True:
        ps = input("contraseña: ")
        conn = Connection(ps)
        if conn != 0:
            break
    defineProducts(conn)
    cursor = conn.cursor()
    cursor.execute(product_desc(6977))
    m = cursor.fetchall()
    for i in m:
        print(i)


main()
    
    
