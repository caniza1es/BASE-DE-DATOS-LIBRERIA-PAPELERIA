import random
import string


#0 - Branch name
#1 - Branch address
#2 - 


mail = ['@gmail.com','@hotmail.com','@yahoo.com']
Nombres = ['Hugo','Martin','Lucas','Mateo','Leo','Daniel','Alejandro','Pablo','Juan','Lucia','Sofia','Martina','Julia','Paula','Valeria','Emma','Rosa','Piedad','Maria','Hernan','Zoraida','Martha','Bruno','Diego','Pedro','Edgar','Trevor','Ernesto','Edwin','Ayleen']
Apellidos = ['Gonzales','Rodriguez','Fernandez','Diaz','Perez','Gomez','Lucero','Sosa','Quiroga','Martinez','Muñoz','Soto','Mokou','Melano','Silva','Henao','Smith','Beltran','Barbosa','Herrera','Lamy','Castro','Cubides','Belmont','Montenegro','Russy','Polo','Villamor']
CC = []
Branches = ['Sucursal Norte','Sucursal Sur']
B_address = ['Las Cruces','Las equis']
emplyees = []

Occupations = ['Cajero','Administrador']
O_salary = [1500000,2500000]

Products = ['Micropunta','Estilografo','Cartulina','Caja lapices','Libro','Caja esferos','Paquete Hojas Carta','Paquete Hojas Examen','Tajalapiz','Borrador','Cuaderno','Libreta']
Precios = [3000,100000,500,2500,0,5000,3500,4000,700,600,4500,6000]
pducts = []
books = []
receipts = []

alpha = ['Bello','Solitario','Terrorifico','Infame','Criptico','Dulze','Inocente','Castaño','Verde','Sangriento','Rebelde','Don','Doctor']
beta = ['anhelo','amor','psicopata','juego','odio','pasaje','interprete','navegador','mounstro','canibal','verso','aprendizaje','imbecil']
generos = ['romance','suspenso','terror','ciencia','autoayuda','poesia']

inventories = []

aut = []
edi = []
cli = []

def rO():
	return random.choice(Occupations)

def rN():
	return random.choice(Nombres)+' '+random.choice(Apellidos)
	
def rCC():
	return random.randint(1000000,9000000) 
	
def rBr():
	return random.choice(Branches)
	
def rMal(name):
	return name + str(random.randint(100,900)) + random.choice(mail)

def rDtb():#yyyy-mm-dd
	yyyy = random.randint(1980,2005)
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

def rDtp():#yyyy-mm-dd
	yyyy = random.randint(2010,2015)
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

def rDtpc():
	yyyy = random.randint(2016,2022)
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
		emplyees.append(cc)
		m.write("INSERT INTO Employees(CC,NAME,branch,occupation,working_since,email)VALUES({0},'{1}','{2}','{3}','{4}','{5}');\n".format(cc,a,rBr(),rO(),rDtp(),rMal(b)))

m = open("demo.txt","w")

for i in range(len(Branches)):
	m.write("INSERT INTO Branches(name,address)VALUES('{0}','{1}');\n".format(Branches[i],B_address[i]))

for i in range(len(Occupations)):
	m.write("INSERT INTO Occupations(description,salary)VALUES('{0}',{1});\n".format(Occupations[i],O_salary[i]));
	
for i in range(30):
	while True:
		id = random.randint(10,90)
		if id not in edi:
			break
	i = ['tinta','escritos','trazo','libros']
	name = random.choice(Apellidos) + " " + random.choice(i)
	contacto = random.randint(600000000,690000000)
	edi.append(id)
	m.write("INSERT INTO Companies(ID,NAME,contacto)VALUES({0},'{1}',{2});\n".format(id,name,contacto))
	
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
			m.write("INSERT INTO Products(ID,price,price_bought)VALUES({0},'{1}',{2});\n".format(id,price,bought));
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
		m.write("INSERT INTO Products(ID,price,price_bought)VALUES({0},'{1}',{2});\n".format(id,price,bought));
		m.write("INSERT INTO Stationers(ID,des,company)VALUES({0},'{1}',{2});\n".format(id,des,random.choice(edi)))
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

for i in books:
	title = random.choice(alpha) + " " + random.choice(beta)
	editorial = random.choice(edi)
	auto = random.choice(aut)
	pub_date = rDtb()
	genre = random.choice(generos)
	m.write("INSERT INTO Books(ID,title,editorial,author,pub_date,genre)VALUES({0},'{1}',{2},{3},'{4}','{5}');\n".format(i,title,editorial,auto,pub_date,genre))
for sucursal in Branches:
	for id in pducts:
		amount = random.randint(1000,2000)
		m.write("INSERT INTO Inventories(branch,product,amount)VALUES('{0}',{1},{2});\n".format(sucursal,id,amount))
		inventories.append((sucursal,id))

for i in range(20):
	newEmployee()

for i in range(200):
	name = rN()
	while True:
		ccc = rCC()
		if ccc not in CC:
			break
	cli.append(ccc)
	phone = random.randint(500000000,599999999)
	email = rMal(name.split()[0])
	m.write("INSERT INTO Clients(CC,NAME,email,phone)VALUES({0},'{1}','{2}',{3});\n".format(ccc,name,email,phone))
	
for i in cli:
	for n in range(random.randint(10,20)):
		while True:
			id = random.randint(3000000,3999999)
			if id not in receipts:
				break
		receipts.append(id)
		time = rDtpc()+' '+str(random.randint(1,18))+':'+ str(random.randint(0,59)) + ':' +str(random.randint(0,59))
		client = random.choice(cli)
		empl = random.choice(emplyees)
		m.write("INSERT INTO Receipts(ID,TIME,client,employee)VALUES({0},'{1}',{2},{3});\n".format(id,time,client,empl))

count = 1
for i in receipts:
	used = []
	for n in range(random.randint(1,6)):
		while True:
			prod = random.choice(pducts)
			if prod not in used:
				break
		used.append(prod)
		amount = random.randint(1,3)
		m.write("INSERT INTO Receipts_desc(ID,product,amount)VALUES({0},{1},{2});\n".format(i,prod,amount))
		m.write("CALL insert_remove({0});\n".format(count))
		count+=1

print("Completado!")
