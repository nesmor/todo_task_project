# todo_task_project

Instrucciones para que el test funcione. 

Clonar el repositorio a traves del comando:

#git clone https://github.com/nesmor/todo_task_project.git

En el directorio database de encuentra un respaldo de la base de datos local llamada  todo_task_list

Restaurar el backup de la base de datos realizada en postgres a traves del comando:

>su - postgres

>psql -U postgres  -h localhost -f [path donde fue clonado el proyecto]/database/db.sql

Importar el archivo de activacion con el entorno para python

#source MYENV/bin/activate

Ejecutar el comando runserver y 

#python manage.py runserver 0:8000

Acceder a la url 

http://localhost:8000/admin

Ingresar al sistema con las credenciales 

user=admin
passwor=V4l3nt1n4!









