# LogScope

LogScope es una plataforma que permite a directivos tener control sobre el acceso a las aplicaciones utilizadas en la empresa y el acceso a la red mediante a la VPN. Se trata de una herramienta de soporte a la decision que ayuda a entender mejor como se pueden administrar las licencias y el uso de las aplicaciones.

En este repositorio encontrarás todo lo que necesitas para poner en marcha la aplicación. Los conjuntos de datos que se proporcionan son tan solo un ejemplo con datos anonimizados para mostrar como funciona la aplicación. Algunas funcionalidades (como Power BI) solo están disponibles para los usuarios con permisos.

Este proyecto ha sido desarrollado en colaboración con [ASTI Mobile Robotics](https://www.astimobilerobotics.com/), empresa española dedicada a la ingeniería de robótica móvil.


## PRESENTACIÓN
[Enlace al video de presentación de LogScope](https://www.youtube.com/watch?v=GqBC4lMWGxk)

## INSTALACIÓN

### Python 3.7.5

> Podemos obtener esta versión específica de Python [aquí](https://www.python.org/downloads/release/python-375/). 

> Asegúrate de que la versión de Python instalada es la 3.7.5.

### MySQL 5.7.28

> Para descargar MySQL puedes hacerlo desde [aquí](https://dev.mysql.com/downloads/windows/installer/5.7.html).

### MySQL Workbench (Opcional)

> Además, otra herramienta útil es MySQL Workbench, que puede descargarse desde [aquí](https://dev.mysql.com/downloads/workbench/).


### Scripts para la base de datos

> El siguiente paso es crear nuestra base de datos y usuario para el proyecto, puedes usar los siguientes scripts:
```cmd
~\app\db\create_dbs.sql
~\app\db\create_test_user.sql
```

### Requerimientos

* django - *version 3.0.5*
* django-filter - *version 2.2.0*
* django-tables2 - *version 2.2.1*
* tablib - *version 1.1.0*
* django-bootstrap-form - *version 3.4*
* django-crispy-forms - *version 1.9.0*
* mysqlclient - *version 1.4.5*
* numpy - *version 1.17.3*
* pandas - *version 0.25.2*
* python-gettext - *version 4.0*


> Tanto si usas virtualenv (explicado en la siguiente sección) como si no, todos los requerimientos necesarios están en el fichero requirements.txt y podemos instalarlos fácilmente con:
```cmd
pip install -r ~\requirements.txt
```

### virtualenv (recomendado)

> Una vez tenemos Python instaldo, pip será instalado también. Podemos usar pip para instalar virtualenv, una herramienta para crear entornos virtuales.

```cmd
pip install virtualenv==16.7.7
```

> Creamos el entorno virtual con:
```cmd
virtualenv path
```

> Activamos con:
```cmd
~\venv\Scripts\activate.bat
```
> Desactivamos con:
```cmd
~\venv\Scripts\deactivate.bat
```
> Y podemos comprobar que hay instalado con:
```cmd
pip freeze
```
> Esta aplicación está siendo desarrollada en Windows y eso provoca que los ficheros que se generan no sean los mismos que en Linux.


### Migraciones

> Lo primero que debemos hacer es crear un fichero con la configuración de la base de datos. El nombre del fichero debe ser ```mysqlconfig.py``` y contener algo como esto:
```python
DB = {
    'NAME': 'name_of_database',
    'USER': 'name_of_user',
    'PASSWORD': 'secret_password',
    'HOST': '127.0.0.1', # database IP
    'PORT': 3306, # database port
    'SERVER': '10.10.10.10', # server IP
}
```

> Ahora, ejecutaremos el siguiente comando para crear las entidades en la base de datos:
```cmd
cd ~\app\src
manage.py migrate
```

### Usuario admin

> Cuando creas todo desde cero es importante disponer de una usuario/cuenta de administrador. Puedes crear una con:
```cmd
manage.py createsuperuser
```

> Esta cuenta te permitirá acceder al sistema de administración de la aplicación donde puedes gestionar la autenticación entre otras cosas.

### Fixtures
> Django nos proporciona una forma sencilla de introducir datos iniciales con `manage.py`.

> Utiliza los ficheros json proporcionados para importar datos a la base de datos con:
```cmd
cd ~\app\src
manage.py loaddata 1_anonymized_persons.json
manage.py loaddata 2_logscope_testdata.json
manage.py loaddata 3_dataset_events.json
manage.py loaddata 4_dataset_passages.json
```

> Estos ficheros json están localizados en ```~\app\src\logscope\fixtures```. El proceso puede llevar un par de minutos.

> También puedes extraer los datos de la base de datos cuando quieras con:
```cmd
cd ~\app\src
manage.py dumpdata --format json --indent 4 > dataset_name.json
```


## DESPLIEGUE

Puedes ejecutar la aplicación con:
```cmd
cd ~\app\src
manage.py runserver [IP]:[port]
```
Esto es algo bastante sencillo de hacer, pero Django necesita un par de configuraciones para poner la aplicación en un entorno de producción.

Todo esto puede ser configurado en el fichero ```settings.py``` donde hay que cambiar lo siguiente:
```python
DEBUG = False
```
```python
ALLOWED_HOSTS = [DB['SERVER']]
```
```python
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

Ahora con todos los cambios hechos recogemos los ficheros estáticos que necesita la aplicación:
```cmd
cd ~\app\src
manage.py collectstatic
```

Y ejecutamos:
```cmd
cd ~\app\src
manage.py runserver server_ip:port --insecure
```
Usa ```0.0.0.0:8000``` por ejemplo.

El parámetro ```--insecure``` es utilizado para habilitar los ficheros estáticos con el modo de depuración deshabilidato.

## TOOLS

* [Trello](https://trello.com/) para administración de tareas.
* [Draw.io](https://www.draw.io/) para realizar diagramas.

---
---

# LogScope 

LogScope is a platform that allows managers to keep track of access to business applications and the network through VPN. This is a decision-making support tool that will allow better understanding about license management and application usage.

You will find in this repository everything you need to setup the application. Datasets provided are just an example with anonymized data to show how it looks like. Some functionalities (Power BI) will only be available for users with privileges.

This project has been developed in collaboration with [ASTI Mobile Robotics](https://www.astimobilerobotics.com/), a Spanish mobile robotics engineering company.


## INSTALLATION

### Python 3.7.5

> We can get this version of Python from [here](https://www.python.org/downloads/release/python-375/). 

> Make sure Python 3.7.5 is the version installed, this is important for the requirements.

### MySQL 5.7.28

> To install MySQL we only need to download from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html).

### MySQL Workbench (Optional)

> Also, another useful tool is MySQL Workbench and can be downloaded from [here](https://dev.mysql.com/downloads/workbench/).

### DB Scripts

> Next step is to create our database and user for the project, you can use:
```cmd
~\app\db\create_dbs.sql
~\app\db\create_test_user.sql
```

### Requirements

* django - *version 3.0.5*
* django-filter - *version 2.2.0*
* django-tables2 - *version 2.2.1*
* tablib - *version 1.1.0*
* django-bootstrap-form - *version 3.4*
* django-crispy-forms - *version 1.9.0*
* mysqlclient - *version 1.4.5*
* numpy - *version 1.17.3*
* pandas - *version 0.25.2*
* python-gettext - *version 4.0*


> Whether we use or not virtualenv (shown in the section below), all the requirements needed are located in requirements.txt and we can easily install them with:
```cmd
pip install -r ~\requirements.txt
```

### virtualenv (recommended)

> Once we have Python installed, pip will be installed too.
We can use pip to install virtualenv, a tool used to create virtual environments:
```cmd
pip install virtualenv==16.7.7
```

> Create the virtual environment with:
```cmd
virtualenv path
```

> It can be activated with:
```cmd
~\venv\Scripts\activate.bat
```
> Deactivated with:
```cmd
~\venv\Scripts\deactivate.bat
```
> And check what contains with:
```cmd
pip freeze
```
> This app its being developed in Windows and that causes virtualenv to create different directories than in Linux.


### Migrations

> First of all we need to create a file with the database configuration. The name of the file must be ```mysqlconfig.py``` and contain something like this:
```python
DB = {
    'NAME': 'name_of_database',
    'USER': 'name_of_user',
    'PASSWORD': 'secret_password',
    'HOST': '127.0.0.1', # database IP
    'PORT': 3306, # database port
    'SERVER': '10.10.10.10', # server IP
}
```

> Now that all is installed, we will execute the following command to create the database entities:
```cmd
cd ~\app\src
manage.py migrate
```

### Admin user

> When you create everything from scratch is important to have an admin account. You can create one with:
```cmd
manage.py createsuperuser
```

> This accout will allow you to access the django administration system of the app where you can manage authentication among other things.

### Fixtures
> Django provides an easy way to set some initial data with `manage.py`.

> Use the given json files to import data to the database with:
```cmd
cd ~\app\src
manage.py loaddata 1_anonymized_persons.json
manage.py loaddata 2_logscope_testdata.json
manage.py loaddata 3_dataset_events.json
manage.py loaddata 4_dataset_passages.json
```

> This json files are located in ```~\app\src\logscope\fixtures```. The process might take a couple of minutes.

> You can also extract the current data from your database with:
```cmd
cd ~\app\src
manage.py dumpdata --format json --indent 4 > dataset_name.json
```


## DEPLOYMENT

You run the app with:
```cmd
cd ~\app\src
manage.py runserver [IP]:[port]
```
This is a pretty simple thing to do, but Django needs a couple of settings to put an application in a production environment because this command only runs the server.

All of this can be configured from the file ```settings.py``` where you have to change the following things:
```python
DEBUG = False
```
```python
ALLOWED_HOSTS = [DB['SERVER']]
```
```python
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```
```
```

Now with all this changes we have to collect the static files:
```cmd
cd ~\app\src
manage.py collectstatic
```

And run the app:
```cmd
cd ~\app\src
manage.py runserver server_ip:port --insecure
```
Use ```0.0.0.0:8000``` for example.

Parameter ```--insecure``` is used to enable static files with debug mode set on false.


## TOOLS

* [Trello](https://trello.com/) for task management.
* [Draw.io](https://www.draw.io/) for diagrams.
