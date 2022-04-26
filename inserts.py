import random
import string


#0 - Branch name
#1 - Branch address
#2 - 


mail = ['@gmail.com','@hotmail.com','@yahoo.com']
Nombres = ['Hugo','Martin','Lucas','Mateo','Leo','Daniel','Alejandro','Pablo','Juan','Lucia','Sofia','Martina','Julia','Paula','Valeria','Emma']
Apellidos = ['Gonzales','Rodriguez','Fernandez','Diaz','Perez','Gomez','Lucero','Sosa','Quiroga','Martinez','Muñoz','Soto','Mokou','Melano','Silva']
CC = []
Branches = ['Sucursal Norte']
B_address = ['Las Cruces']

Occupations = ['Cajero','Administrador']
O_salary = [1500000,2500000]

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
	d = random.randint(0,3)
	if d == 3:
		dd = random.randint(0,1)
	else:
		dd = random.randint(1,9)
	return '{0}-{1}{2}-{3}{4}'.format(yyyy,m,mm,d,dd)

def newEmployee():
		a = rN()
		b = a.split()[0]
		m.write("INSERT INTO Employees(CC,NAME,branch,occupation,working_since,email)VALUES({0},'{1}','{2}','{3}','{4}','{5}');\n".format(rCC(),a,rBr(),rO(),rDt(),rMal(b)))

m = open("demo.txt","w")

for i in range(len(Branches)):
	m.write("INSERT INTO Branches(name,address)VALUES('{0}','{1}');\n".format(Branches[i],B_address[i]))

for i in range(len(Occupations)):
	m.write("INSERT INTO Occupations(description,salary)VALUES('{0}',{1});\n".format(Occupations[i],O_salary[i]));


	
for i in range(5):
	newEmployee()

	


