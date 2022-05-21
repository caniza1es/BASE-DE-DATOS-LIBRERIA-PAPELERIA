CREATE TABLE Branches(
name varchar(25) PRIMARY KEY,
address VARCHAR(25) NOT NULL
);

CREATE TABLE Occupations(
description VARCHAR(20) PRIMARY KEY,
salary integer NOT NULL CHECK(salary > 0)
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
price INTEGER CHECK(price > price_bought),
price_bought INTEGER CHECK(price_bought > 0)
);	

CREATE TABLE Inventories(
branch VARCHAR(25) REFERENCES Branches(name),
product INTEGER REFERENCES Products(ID),
amount INTEGER CHECK(amount >= 0) DEFAULT 0,
PRIMARY KEY(branch,product)
);

CREATE TABLE Authors(
id INTEGER PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email TEXT NULL
);

CREATE TABLE Companies(
ID INTEGER PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
contacto INTEGER NOT NULL
);

CREATE TABLE Stationers(
ID INTEGER pRIMARY KEY,
des VARCHAR(40),
company INTEGER REFERENCES Companies(id)
);

CREATE TABLE Books(
id integer REFERENCES Products(ID),
title VARCHAR(50) NOT NULL,
editorial INTEGER REFERENCES Companies(ID),
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
employee INTEGER REFERENCES employees(CC) NOT NULL
);

CREATE TABLE Receipts_desc(
IDD serial,
ID INTEGER REFERENCES Receipts(ID),
product INTEGER REFERENCES Products(Id),
amount INTEGER NOT NULL CHECK(amount > 0),
PRIMARY KEY(IDD)
);

CREATE TABLE Ingresos(
r_id INTEGER REFERENCES receipts(id),
rd_id INTEGER REFERENCES receipts_desc(IDD),
branch varchar(25) REFERENCES Branches(NAME),
sold_price INTEGER,
year smallint,
month SMALLINT,
DAY SMALLINT,
PRIMARY KEY(r_id,rd_id)
);

CREATE OR REPLACE PROCEDURE insert_remove(iddd INTEGER)
LANGUAGE 'plpgsql'
AS $$
BEGIN
INSERT INTO ingresos(r_id,rd_id,branch,sold_price,year,month,day)
	SELECT R.id,rd.idd,e.branch,p.price,EXTRACT(year FROM R.time),EXTRACT(MONTH FROM R.time),EXTRACT(DAY FROM R.time)
    from receipts_desc as rd,employees as e,receipts as R,products as P
    WHERE rd.idd = iddd
    AND rd.id = R.id
    AND R.employee = e.cc
    AND rd.product = P.id;
UPDATE inventories
set amount = amount - (SELECT SUM(receipts_desc.amount) FROM receipts_desc WHERE receipts_desc.idd = iddd)
WHERE product = (SELECT receipts_desc.product FROM receipts_desc WHERE receipts_desc.idd=iddd);
END;
$$;

CREATE ROLE caja
LOGIN
PASSWORD '123'
CONNECTION LIMIT 1000;

CREATE ROLE caja_administrador
LOGIN
PASSWORD '123'
CONNECTION LIMIT 1000;

CREATE ROLE administrador_sucursal
LOGIN
PASSWORD '123'
CONNECTION LIMIT 1000;

GRANT SELECT,INSERT
ON receipts,receipts_desc
TO caja;

GRANT SELECT
ON Stationers,Books,inventories,Products
TO caja;

GRANT ALL ON PROCEDURE insert_remove TO caja;

GRANT SELECT,INSERT,DELETE
ON receipts,receipts_desc
TO caja_administrador;

GRANT SELECT
ON Stationers,Books,inventories
TO caja_administrador;

GRANT SELECT,UPDATE
ON Products,inventories
TO caja_administrador;

GRANT SELECT
ON ALL TABLES
in schema "public"
TO administrador_sucursal;

GRANT INSERT,UPDATE,DELETE
ON Products,inventories,Books,Stationers
TO administrador_sucursal;


