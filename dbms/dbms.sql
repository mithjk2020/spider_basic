CREATE DATABASE inventoryDB;

USE inventoryDB;

CREATE TABLE products(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40), description VARCHAR(100), price FLOAT NOT NULL, quantity INT, category VARCHAR(50) );

INSERT INTO products (name, description, price, quantity, category) VALUES ("Gaming Laptop", "High-performance laptop with 16GB RAM", 87000, 3, "Electronics"), ("Yoga Mat", "Non-slip yoga mat with carrying strap", 600, 150, "Sports"), ("Backpack","Water-resistant backpack with multiple compartments and USB port", 1300, 25, "Accessories");

#retrieving products
SELECT * FROM products;

SELECT * FROM products WHERE price < 2000;

SELECT * FROM products WHERE quantity > 10;

UPDATE products SET price=800 WHERE name="Yoga mat";

DELETE FROM products WHERE name="Backpack";
