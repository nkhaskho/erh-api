## Virtual environment
Separate envirnment 
``` bash
$ python -m venv <name>
```

Activate the created virtual environment 
``` bash
$ ./<env>/Scripts/activate (Windows)
$ source <env>/bin/activate
```

Install (recursively) required modules or libraries 
``` bash
$ pip install -r requirements.txt
```

## Django project
Create django project 
``` bash
$ django-admin startproject erh_api
```

Create django app (api) 
``` bash
$ django-admin startapp users
```

## Database migrations
Create/Make migrations 
``` bash
python manage.py makemigrations
```

Apply migrations 
``` bash
python manage.py migrate
```