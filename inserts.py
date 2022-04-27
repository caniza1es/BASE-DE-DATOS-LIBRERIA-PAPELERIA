import random
import string


#0 - Branch name
#1 - Branch address
#2 - 


mail = ['@gmail.com','@hotmail.com','@yahoo.com']
Nombres = ['Hugo','Martin','Lucas','Mateo','Leo','Daniel','Alejandro','Pablo','Juan','Lucia','Sofia','Martina','Julia','Paula','Valeria','Emma']
Apellidos = ['Gonzales','Rodriguez','Fernandez','Diaz','Perez','Gomez','Lucero','Sosa','Quiroga','Martinez','Muñoz','Soto','Mokou','Melano','Silva']
CC = []
Branches = ['Sucursal Norte','Sucursal Sur']
B_address = ['Las Cruces','Las equis']

Occupations = ['Cajero','Administrador']
O_salary = [1500000,2500000]

Products = ['Micropunta','Estilografo','Cartulina','Caja lapices','Libro','Caja esferos','Paquete Hojas Carta','Paquete Hojas Examen','Tajalapiz','Borrador','Cuaderno','Libreta']
Precios = [3000,100000,500,2500,0,5000,3500,4000,700,600,4500,6000]
pducts = []
books = []

alpha = ['Bello','Solitario','Terrorifico','Infame','Criptico','Dulze','Inocente','Castaño','Verde','Sangriento','Rebelde','Don','Doctor']
beta = ['anhelo','amor','psicopata','juego','odio','pasaje','interprete','navegador','mounstro','canibal','verso','aprendizaje','imbecil']
generos = ['romance','suspenso','terror','ciencia','autoayuda','poesia']

inventories = []

aut = []
edi = []

def rO():
	return random.choice(Occupations)

def rN():
	return random.choice(Nombres)+' '+random.choice(Apellidos)
	
def rCC():
	return random.randint(1000000,9000000) 
	
def rBr():
	return random.choice(Branches)
	
def rMal(name):
	return name + str(random.randint(0,10)) + random.choice(mail)

def rDt():#yyyy-mm-dd
	yyyy = random.randint(1980,2022)
	m = random.randint(0,1)
	if m == 0:
		mm = random.randint(1,9)
	else:
		mm = random.randint(0,2)
	d = random.randint(0,2)
	if d == 2:
		dd = random.randint(0,8)
	else:
		dd = random.randint(1,9)
	return '{0}-{1}{2}-{3}{4}'.format(yyyy,m,mm,d,dd)

def newEmployee():
		a = rN()
		b = a.split()[0]
		cc = rCC()
		CC.append(cc)
		m.write("INSERT INTO Employees(CC,NAME,branch,occupation,working_since,email)VALUES({0},'{1}','{2}','{3}','{4}','{5}');\n".format(cc,a,rBr(),rO(),rDt(),rMal(b)))

m = open("demo.txt","w")

for i in range(len(Branches)):
	m.write("INSERT INTO Branches(name,address)VALUES('{0}','{1}');\n".format(Branches[i],B_address[i]))

for i in range(len(Occupations)):
	m.write("INSERT INTO Occupations(description,salary)VALUES('{0}',{1});\n".format(Occupations[i],O_salary[i]));
	
for i in range(len(Products)):
	if Products[i] == 'Libro':
		for mmm in range(100):
			while True:
				id = random.randint(1000,9999)
				if id not in pducts:
					break
			des = Products[i]
			bought = random.randint(50000,250000)
			while True:
				price = bought + random.randint(10000,20000)
				if price%100 == 0:
					break
			m.write("INSERT INTO Products(ID,des,price,price_bought)VALUES({0},'{1}',{2},{3});\n".format(id,des,price,bought));
			pducts.append(id)
			books.append(id)
	else:
		while True:
			id = random.randint(1000,9999)
			if id not in pducts:
				break
		des = Products[i]
		bought = Precios[i]
		while True:
			price = bought + random.randint(500,700)
			if price%100 == 0:
				break;
		m.write("INSERT INTO Products(ID,des,price,price_bought)VALUES({0},'{1}',{2},{3});\n".format(id,des,price,bought));
		pducts.append(id)

for i in range(60):
	while True:
		id = random.randint(100,999)
		if id not in aut:
			break
	name = rN()
	email = rMal(name.split()[1])
	aut.append(id)
	m.write("INSERT INTO Authors(ID,NAME,email)VALUES({0},'{1}','{2}');\n".format(id,name,email))

for i in range(30):
	while True:
		id = random.randint(10,90)
		if id not in edi:
			break
	i = ['tinta','escritos','trazo','libros']
	name = random.choice(Apellidos) + " " + random.choice(i)
	contacto = random.randint(600000000,690000000)
	edi.append(id)
	m.write("INSERT INTO Editorials(ID,NAME,contacto)VALUES({0},'{1}',{2});\n".format(id,name,contacto))

for i in books:
	title = random.choice(alpha) + " " + random.choice(beta)
	editorial = random.choice(edi)
	auto = random.choice(aut)
	pub_date = rDt()
	genre = random.choice(generos)
	m.write("INSERT INTO Books(ID,title,editorial,author,pub_date,genre)VALUES({0},'{1}',{2},{3},'{4}','{5}');\n".format(i,title,editorial,auto,pub_date,genre))
for sucursal in Branches:
	for id in pducts:
		amount = random.randint(0,500)
		m.write("INSERT INTO Inventories(branch,product,amount)VALUES('{0}',{1},{2});\n".format(sucursal,id,amount))
		inventories.append((sucursal,id))

for i in range(20):
	newEmployee()

print("Success!")

	


