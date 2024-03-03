# myappstoreback

# Instructions

# Notes:

## Commands list:

### Models - dataBase:

- python manage.py inspectdb > GenerateModels.py
- python manage.py inspectdb nametable
- python manage.py createsuperuser

### Install django en venv:

+ venv:

    - python -m venv venv (Version > 3.3)
    - virtualenv venv (Version <= a 3.3)

    Activate:
        /venv/Script/Activate.bat
    Deactivate:
        /Venv/Script/deactivate

+ pip

    - pip --version (Check)
    - pip install virtuaenv (Install)
    - python.exe -m pip install --upgrade pip (Upgrade)

- django-admin --version (Check)
- pip install django (Install)
    
- django-admin startproject NameProject . // (Create New Project)
- python manage.py startapp mastertable // (Create new App)
- python manage.py makemigrations // (Create modes)
- python manage.py migrate // (Send Models of table)

## Dependency:

### General:

- pip list // (List all dependency + Lib OS)
- pip freeze > requirements.txt // (Dependency production.)
- pip install -r requirements.txt // (Install all dependency)
    
### Development:

### Production:

- pip install django
- pip install djangorestframework
- pip install django-cors-headersx
- pip install coreapi (Documentation APIs)
- pip install psycopg2

# Bibliography:

- https://www.django-rest-framework.org/

- 

- 

- 

>>> from tasks.serializers import Tasks
>>> serializer = Tasks()
>>> print(repr(serializer))