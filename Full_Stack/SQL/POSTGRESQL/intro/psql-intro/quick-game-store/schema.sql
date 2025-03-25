

DROP TABLE IF EXISTS poster;
CREATE TABLE poster (
    id INT PRIMARY KEY,
    quantity INT,
    title VARCHAR(255) UNIQUE,
    price DECIMAL(5,2)
);

DROP TABLE IF EXISTS figure;
CREATE TABLE figure (
    id INT PRIMARY KEY,
    quantity INT,
    title VARCHAR(255) UNIQUE,
    price DECIMAL(5,2)
);

DROP TABLE IF EXISTS game;
CREATE TABLE game (
    id INT PRIMARY KEY,
    quantity INT,
    title VARCHAR(255) UNIQUE,
    price DECIMAL(5,2)
);


DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
    id INT PRIMARY KEY,
    product_id INT
);

DROP TABLE IF EXISTS customer;
    CREATE TABLE customer (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone INT,
    email VARCHAR(255)
);

DROP TABLE IF EXISTS employee;
    CREATE TABLE employee (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    position VARCHAR(255),
    salary INT
);

DROP TABLE IF EXISTS purchase;
CREATE TABLE purchase(
    id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_id INT,
    customer_id INT,
    purchase_price DECIMAL(5,2)
);

DROP TABLE IF EXISTS store;
CREATE TABLE store(
    id INT PRIMARY KEY,
    employee_id INT,
    inventory_id INT,
    sales INT
);