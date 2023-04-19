--####################################################################################################
--This script is intended for local development only.
-- Creates initial tables [users,roles,userRoles] for 'Identity_DB' 
-- V1, 2023-04-19, Qiniso Mazibuko, Initial Version
--####################################################################################################

USE Identity_DB;

CREATE TABLE IdentityUser (
    Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    UserName NVARCHAR(50) NOT NULL UNIQUE,
    Email NVARCHAR(320) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(256) NOT NULL,
    PasswordSalt NVARCHAR(256) NOT NULL
);

CREATE TABLE IdentityRole (
    Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE UserRoles (
    UserId INT NOT NULL,
    RoleId INT NOT NULL,
    PRIMARY KEY (UserId, RoleId),
    FOREIGN KEY (UserId) REFERENCES Users (Id),
    FOREIGN KEY (RoleId) REFERENCES Roles (Id)
);
