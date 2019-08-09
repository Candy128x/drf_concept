# Commands

---
- description..
- => pwd


---
- switch on env
- => source env_name/bin/activate
- eg: source venv/bin/activate


---
- install django
- => pip3 install django


---
- install djangorestframework
- pipenv install djangorestframework `OR`
- via IDE install djangorestframework

- => pip install psycopg2 


---
- create django project
- => django-admin startproject projtest


---
- create server drf_db in PostgreSQL
- create database def_fw_db


---
- cd projtest
- => python3 manage.py migrate


---
- => python3 manage.py createsuperuser 
- (un: ashish, pwd: qwerty)


---
- => python3 manage.py startapp languages


---
- => python3 manage.py makemigrations
- => python3 manage.py migrate


---
- Login user to access or take action on data
- add in `projtest/urls.py`, code: `path('api-auth/', include('rest_framework.urls'))`
- add in `languages/views.py`, code: `permission_classes = (permissions.IsAuthenticatedOrReadOnly,)`
- add in `projtest/settings.py`, 
- code: 
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}
```


---
### use JWT (Json Web Token)
- => pip3 install djangorestframework_simplejwt


---
### make send.py file
- => pip3 install requests


---
### Relationship
- Add table struct in model.py

- => python3 manage.py migrations
- op:
```
Migrations for 'languages':
  languages/migrations/0002_auto_20190807_0600.py
    - Create model Paradigm
    - Alter field paradigm on language
    - Create model Programmer

```

- => python3 manage.py migrate
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, languages, sessions
Running migrations:
  Applying languages.0002_auto_20190807_0600... OK
```


---
## emp API
- => python3 manage.py startapp empapi
