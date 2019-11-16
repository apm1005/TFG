# TFG 

Platform that allows system administrators to keep track of access to business applications and the network through VPN access.

Notice that all SQL scripts are <span style="color:#CB2400">only</span> warrantied to work on SQLServer.

## REQUIREMENTS FOR DEVELOPER
* SQLServer 2017
* SQLServer Management Studio 18.3.1
* Python 3.7.5
* Django 2.2.6

## INSTALLING
### SQLServer
To install SQLServer we only need to download from [here](https://www.microsoft.com/es-es/sql-server/sql-server-downloads).

Also, another useful tool is SQLServer Management Studio from [here](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15).

Using SQL Server also requires the [ODBC Driver](https://www.microsoft.com/en-us/download/details.aspx?id=56567).

### Python 3.7.5
We can get this version of Python from [here](https://www.python.org/downloads/).

### pip
Whether we use or not virtualenv (shown in the section below), all the requirements needed are located in requirements.txt and we can easily 
install them with:
```cmd
pip install -r requirements.txt
```

### virtualenv (optional)
Once we have Python installed, pip will be installed too.
We can use pip to install virtualenv, a tool used to create virtual environments:
```
pip install virtualenv==16.7.7
```

It can be activated with:
```cmd
~\venv\Scripts\activate.bat
```
Deactivated with:
```cmd
~\venv\Scripts\deactivate.bat
```
And check what contains with:
```cmd
pip freeze
```
This app its being developed in Windows and that causes virtualenv to create different directories than in Linux.

## TOOLS

* [Trello](https://trello.com/) for task management
* [Draw.io](https://www.draw.io/) for diagrams