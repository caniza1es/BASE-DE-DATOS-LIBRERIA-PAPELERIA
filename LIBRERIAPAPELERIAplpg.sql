CREATE TABLE Branches(
name varchar(25) PRIMARY KEY,
address VARCHAR(25) NOT NULL,
budget INTEGER NOT NULL
);
CREATE TABLE Occupations(
description VARCHAR(20) PRIMARY KEY,
salary integer NOT NULL
);
CREATE TABLE Employees(
CC integer PRIMARY KEY,
name VARCHAR(40) NOT NULL,
branch VARCHAR(25) REFERENCES Branches(name),
occupation VARCHAR(20) REFERENCES Occupations(description),
working_since DATE NOT NULL,
email VARCHAR(50)
);

CREATE TABLE Products(
ID INTEGER PRIMARY KEY,
des varchar(30) NOT NULL
);	

CREATE TABLE Inventories(
branch VARCHAR(25) REFERENCES Branches(name),
product INTEGER REFERENCES Products(ID),
amount INTEGER NOT NUll,
PRIMARY KEY(branch,product)
);

CREATE TABLE Authors(
id INTEGER PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email TEXT NULL
);
CREATE TABLE Books(
id integer REFERENCES Products(ID),
title VARCHAR(50) NOT NULL,
editorial VARCHAR(40),
author INTEGER REFERENCES Authors(ID),
pub_date DATE NOT NULL,
genre VARCHAR(30) NOT NULL,
PRIMARY KEY(ID)
);

CREATE TABLE Clients(
CC INTEGER PRIMARY KEY,
name varchar(50),
email varchar(50) NULL,
phone VARCHAR(50) NULL
);

CREATE TABLE Receipts(
ID INTEGER PRIMARY KEY,
time TIMESTAMP NOT NULL,
client INTEGER REFERENCES Clients(CC) NOT NULL,
employee INTEGER REFERENCES employees(CC) NOT NULL,
branch varchar(25) REFERENCES Branches(name)
);

CREATE TABLE Receipts_desc(
ID INTEGER REFERENCES Receipts(ID),
product INTEGER REFERENCES Products(Id),
amount INTEGER NOT NULL,
PRIMARY KEY(id,product)
);

INSERT INTO branches(name,address,budget)
	VALUES('Norte','Autopista Nte #168-30',5000000);
    
INSERT INTO occupations(description,salary)
	VALUES('Caja',2500000);
    
INSERT INTO employees(cc,name,branch,occupation,working_since,email)
	VALUES(1000518517,'Juan Alvarez','Norte','Caja','2019-01-01','juanalavarez@hotmail.com');
    
INSERT INTO products(id,des)
	VALUES(0001,'Micropunta'),
   		  (0002,'ejericios matematica');
          
INSERT INTo inventories(branch,product,amount)
	VALUES('Norte',0001,300),
     	  ('Norte',0002,5);
INSERT INTo authors(id,name)
	VALUES(2222,'Johann Mastropiero');
    
INSERT INTO books(id,title,editorial,author,pub_date,genre)
	VALUES(0002,'Acertijos','Letras rojas',2222,'2000-01-01','Ciencia');
    
INSERT INTO clients(cc,name,email,phone)
	VALUES(100323678,'Juan Canizales','juan.canizales@urosario.edu.co',3136470503);
    
INSERT INTO receipts(id,time,client,employee,branch)
	VALUES(5000,'2020-06-22 19:10:25-07',100323678,1000518517,'Norte');

INSERT INTO receipts_desc(ID,product,amount)
	VALUES(5000,0001,3),
    	 (5000,0002,1);
