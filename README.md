# todo_task_project

Instrucciones para que el test funcione. 

Clonar el repositorio a traves del comando:

#git clone https://github.com/nesmor/todo_task_project.git

En el directorio database de encuentra, existe un respaldo de la base de datos local llamada  todo_task_list

Restaurar el backup de la base de datos realizada en postgres a traves del comando: 
La base de datos respaldada se llama todo_task_db

>su - postgres

>psql -U postgres  -h localhost -f [path donde fue clonado el proyecto]/database/db.sql

Modificar el archivo setting.py según corresponda.

[path donde fue clonado el proyecto]/todoListProject/todoListProject/settings.py

DATABASES = {
	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'todo_task_list',
        	'USER': 'postgres',
        	'PASSWORD': 'postgres',
        	'HOST': '127.0.0.1',
        	'PORT': '5432',
    }

}







Modificar la variable VIRTUAL_ENV segun corresponda. 
VIRTUAL_ENV="[path donde fue clonado el proyecto]/todo_task_project/MYENV"

Importar el archivo de activacion con el entorno para python

#source [path donde fue clonado el proyecto]/MYENV/bin/activate

Ejecutar el comando runserver y 

#python manage.py runserver 0:8000

Acceder a la url 

http://localhost:8000/admin

Ingresar al sistema con las credenciales 

user=admin
passwor=V4l3nt1n4!


Para este test, se desarrolló sobre ubuntu 18, python 3, django 2.1, postgres 9.





