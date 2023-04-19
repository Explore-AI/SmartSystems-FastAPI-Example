--####################################################################################################
--This script is intended for local development only.
-- Creates a new database 'Identity_DB'
-- V1, 2023-04-19, Qiniso Mazibuko, Initial Version
--####################################################################################################

USE [master]
GO
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'Identity_DB')
BEGIN
    CREATE DATABASE [Identity_DB]
END
