CREATE DATABASE IF NOT EXISTS flask_db;

USE flask_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    job VARCHAR(100),
    age INT
);

INSERT INTO users (name, email, job, age)
VALUES ('Olena Kravets', 'olena@example.com', 'QA Engineer', 30),
('Ivan Petrenko', 'ivan@example.com', 'Backend Developer', 35);
