-- Tables SQL

-- 1. Create a database;
CREATE DATABASE technologie;
use technologie;

-- 2. Create Tables.
-- 2.1 Mark.
CREATE TABLE Mark(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL
)ENGINE = InnoDB;

-- 2.1 Category.
CREATE TABLE Category(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL
)ENGINE = InnoDB;

-- 2.2 Product.
CREATE TABLE Product(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL,
	price float(30) NOT NULL,
	id_mark int(3),
	id_category int(3),
	FOREIGN KEY (id_mark) REFERENCES Mark(id),
	FOREIGN KEY (id_category) REFERENCES Category(id)
)ENGINE = InnoDB;