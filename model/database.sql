-- Tables SQL

-- 1. Create a database;
CREATE DATABASE product;
use product;

-- 2. Create Tables.
-- 2.1 Mark.
CREATE TABLE Mark(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL
)ENGINE=InnoDB;

-- 2.2 Product.
CREATE TABLE Product(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL,
	price float(30) NOT NULL,
	id_mark int(3),
	FOREIGN KEY (id_mark) REFERENCES Mark(id)
)ENGINE = InnoDB;