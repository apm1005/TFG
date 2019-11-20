# TFG 

Platform that allows system administrators to keep track of access to business applications and the network through VPN access.

Notice that all SQL scripts are <span style="color:#CB2400">only</span> warrantied to work on MySQL.

## REQUIREMENTS FOR DEVELOPER
* MySQL 5.7.28
* MySQL Workbench
* Python 3.7.5
* Django 2.2.6

## INSTALLING
### MySQL
To install MySQL we only need to download from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html).

Also, another useful tool is MySQL Workbench and can be downloaded from [here](https://dev.mysql.com/downloads/workbench/).

### Python 3.7.5
We can get this version of Python from [here](https://www.python.org/downloads/).

### pip
Whether we use or not virtualenv (shown in the section below), all the requirements needed are located in requirements.txt and we can easily 
install them with:
```cmd
pip install -r requirements.txt
```

### virtualenv (recommended)
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