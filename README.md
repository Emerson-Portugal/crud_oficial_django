## CREAR ENTORNO VIRTUAL

virtualenv -p python3.9 venv 

## CREAR PROYETO INICIAL EN DJANGO

django-admin startproject core .  


## Para crear nuevas Apps

python ../manage.py startapp "nombre_app"

## EJECUTAR PROGRAMA


npm run start

python .\manage.py runserver 127.0.0.1:8000     


## CONEXION A GIT

git remote add origin https://github.com/Emerson-Portugal/Demo_Blog_Venv.git

git push -u origin main

## Para generar la carpeta static

python manage.py collectstatic




## Actualizacion 

python manage.py makemigrations

python manage.py migrate


## Para crear el super Usuario

python manage.py createsuperuser
