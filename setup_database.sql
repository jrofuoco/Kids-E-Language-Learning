-- Create the database
CREATE DATABASE IF NOT EXISTS kids_learning;

-- Use the database
USE kids_learning;

-- Create the user's table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    level INT DEFAULT 1
);

-- Insert a test user (optional)
INSERT INTO users (username, password, level) VALUES ('test', 'test123', 1); 