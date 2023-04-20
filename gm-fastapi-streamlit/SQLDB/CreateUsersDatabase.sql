-- Use this to create a database for our User App database
-- First we test to see if there are any databases already with the same name
IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'UsersApp_DB')
  BEGIN
    CREATE DATABASE [UsersApp_DB]
    END
    GO
       USE [UsersApp_DB]
    GO
-- Create a table to store user information, if it doesn't already exist
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='UsersTable' and xtype='U')
BEGIN
    CREATE TABLE UsersTable (
        user_id INT PRIMARY KEY IDENTITY (1, 1),
        username VARCHAR(50) NOT NULL , 
        first_name VARCHAR(50) NULL,
        last_name VARCHAR(50) NULL,
        email VARCHAR(50) NOT NULL,
        hashed_password VARCHAR(50) NOT NULL, 
        bio VARCHAR(500)
    )
    -- populate table with initial dummy data
    INSERT INTO UsersTable (username, first_name, last_name, email, hashed_password, bio)
    VALUES 
    ( 'gerald', 'John', 'Matthews', 'admin@gmail.com','2323234kkqq', ''),
    ( 'lando', 'Lando', 'Kalrizian', 'lando@gmail.com','2323234kkqq', ''),
    ( 'thechild', 'Grogu', 'Yodason', 'grogu@gmail.com','2323234kkqq', ''),
    ( 'themando', 'Djinn', 'Djarin', 'themando@gmail.com','2323234kkqq', ''), 
    ('ashoka', 'Ashoka', 'Tanno', 'ashoka@gmail.com','2323234kkqq', '')
END
-- Add in data to the table if it is empty

