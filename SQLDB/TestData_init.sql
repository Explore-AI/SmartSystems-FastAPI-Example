--####################################################################################################
-- This script is intended for local development only.
-- inserts test data into 'Identity_DB' tables
-- V1, 2023-04-19, Qiniso Mazibuko, Initial Version
--####################################################################################################

USE Identity_DB;

-- Add roles
INSERT INTO IdentityRoles (Name) VALUES ('Subscriber');
INSERT INTO IdentityRoles (Name) VALUES ('Admin');

-- Add users
INSERT INTO IdentityUsers (UserName, Email, PasswordSalt,PasswordHash) VALUES ('John Doe', 'john.doe@example.com', 'Password@12', 'Password@12');
INSERT INTO IdentityUsers (UserName, Email,PasswordSalt,PasswordHash) VALUES ('Jane Doe', 'jane.doe@example.com', 'Password@12', 'Password@12');

-- Add user roles
DECLARE @johnUserId INT = (SELECT Id FROM IdentityUsers WHERE UserName = 'John Doe');
DECLARE @janeUserId INT = (SELECT Id FROM IdentityUsers WHERE UserName = 'Jane Doe');
DECLARE @subscriberRoleId INT = (SELECT Id FROM IdentityRoles WHERE Name = 'Subscriber');
DECLARE @adminRoleId INT = (SELECT Id FROM IdentityRoles WHERE Name = 'Admin');

INSERT INTO UserRoles (UserId, RoleId) VALUES (@johnUserId, @adminRoleId);
INSERT INTO UserRoles (UserId, RoleId) VALUES (@janeUserId, @subscriberRoleId);
