--####################################################################################################
--This script is intended for local development only.
-- inserts test data into 'Identity_DB' tables
-- V1, 2023-04-19, Qiniso Mazibuko, Initial Version
--####################################################################################################

USE Identity_DB;

-- Add roles
INSERT INTO IdentityRole (Name) VALUES ('Subscriber');
INSERT INTO IdentityRole (Name) VALUES ('Admin');

-- Add users
INSERT INTO IdentityUsers (UserName, Email) VALUES ('John Doe', 'john.doe@example.com');
INSERT INTO IdentityUsers (UserName, Email) VALUES ('Jane Doe', 'jane.doe@example.com');

-- Add user roles
DECLARE @johnUserId INT = (SELECT UserId FROM IdentityUsers WHERE UserName = 'John Doe');
DECLARE @janeUserId INT = (SELECT UserId FROM IdentityUsers WHERE UserName = 'Jane Doe');
DECLARE @subscriberRoleId INT = (SELECT RoleId FROM IdentityRole WHERE Name = 'Subscriber');
DECLARE @adminRoleId INT = (SELECT RoleId FROM IdentityRole WHERE Name = 'Admin');

INSERT INTO UserRoles (UserId, RoleId) VALUES (@johnUserId, @adminRoleId);
INSERT INTO UserRoles (UserId, RoleId) VALUES (@janeUserId, @subscriberRoleId);
