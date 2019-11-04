USE [dev];
GO

CREATE LOGIN tfg WITH PASSWORD = '1234';
GO

CREATE USER tfg FOR LOGIN tfg;
GO

EXEC sp_addrolemember 'db_datareader', 'tfg'
EXEC sp_addrolemember 'db_datawriter', 'tfg'
EXEC sp_addrolemember 'db_ddladmin', 'tfg'
GO

USE [test]
GO

CREATE USER tfg FOR LOGIN tfg;
GO

EXEC sp_addrolemember 'db_datareader', 'tfg'
EXEC sp_addrolemember 'db_datawriter', 'tfg'
EXEC sp_addrolemember 'db_ddladmin', 'tfg'
GO