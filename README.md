# TFG 

Platform that allows system administrators to keep track of access to business applications and the network through VPN access.

## REQUIREMENTS FOR DEVELOPERS
* SQLServer 2017
* SQLServer Management Studio 18.3.1
* Python 3.7.5
* Django 2.2.6

## INSTALLING
### SQLServer
To install SQLServer we only need to download from [here](https://www.microsoft.com/es-es/sql-server/sql-server-downloads).

Also, another useful tool is SQLServer Management Studio from [here](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15).

### Python 3.7.5
We can get this version of Python from [here](https://www.python.org/downloads/).

### Django 2.2.6
We will use pip to install Django:
```
pip install django==2.2.6
```
Using SQL Server also requires the [ODBC Driver](https://www.microsoft.com/en-us/download/details.aspx?id=56567) and the mssql backend:
```
pip install django-mssql-backend
```

## TOOLS

* [Trello](https://trello.com/) for task management
* [Draw.io](https://www.draw.io/) for diagrams