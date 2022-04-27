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
des varchar(30) NOT NULL,
price INTEGER CHECK(price > price_bought),
price_bought INTEGER CHECK(price_bought > 0)
);	

CREATE TABLE Inventories(
branch VARCHAR(25) REFERENCES Branches(name),
product INTEGER REFERENCES Products(ID),
amount INTEGER CHECK(amount > 0) DEFAULT 0,
PRIMARY KEY(branch,product)
);

CREATE TABLE Authors(
id INTEGER PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email TEXT NULL
);

CREATE TABLE Editorials(
ID INTEGER PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
contacto TEXT NOT NULL
);

CREATE TABLE Books(
id integer REFERENCES Products(ID),
title VARCHAR(50) NOT NULL,
editorial INTEGER REFERENCES Editorials(ID),
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
ON DELETE CASCADE
);

CREATE TABLE Receipts_desc(
ID INTEGER REFERENCES Receipts(ID),
product INTEGER REFERENCES Products(Id),
amount INTEGER NOT NULL CHECK(amount > 0),
PRIMARY KEY(id,product)
);

CREATE OR REPLACE VIEW total_employees AS (
	SELECT * FROM employees
  	ORDER by branch
);
