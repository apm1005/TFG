# LogScope

Platform that allows system administrators to keep track of access to business applications and the network through VPN access.

Notice that all SQL scripts are <span style="color:#CB2400">only</span> warrantied to work on MySQL.

## REQUIREMENTS FOR DEVELOPERS
* MySQL 5.7.28
* MySQL Workbench (Optional)
* Python 3.7.5
* Django 2.2.6

## INSTALLING
### MySQL
To install MySQL we only need to download from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html).

Also, another useful tool is MySQL Workbench and can be downloaded from [here](https://dev.mysql.com/downloads/workbench/).

### DB Scripts
Next step is to create our database and user for the project, you can use:
```cmd
~\app\db\create_dbs.sql
~\app\db\create_test_user.sql
```

### Python 3.7.5
We can get this version of Python from [here](https://www.python.org/downloads/release/python-375/).

Make sure Python 3.7.5 is the version installed, this is important for the requirements.

### pip
Whether we use or not virtualenv (shown in the section below), all the requirements needed are located in requirements.txt and we can easily 
install them with:
```cmd
pip install -r ~\requirements.txt
```

### virtualenv (recommended)
Once we have Python installed, pip will be installed too.
We can use pip to install virtualenv, a tool used to create virtual environments:
```cmd
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

### Migrations
Now that all is installed, we will execute the following command to create the database entities:
```cmd
cd ~\app\src
manage.py migrate
```
For the last step, you can use the ```~\app\db\create_test_user.sql``` script as an example of initial data.

### Fixtures
Django provides an easy way to set some initial data with manage.py.

First of all, you can extract the current data from your database with:
```cmd
cd ~\app\src
manage.py dumpdata --format json --indent 4 > initial.json
```
Now you can use this json file (or one created by yourself) to import data to the database with:
```cmd
cd ~\app\src
manage.py loaddata initial.json
```

## TOOLS

* [Trello](https://trello.com/) for task management
* [Draw.io](https://www.draw.io/) for diagrams