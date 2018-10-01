# joplin-web

Web application for [Joplin](https://joplin.cozic.net/)

## requirements

### for backend

* [joplin-terminal](https://joplin.cozic.net/terminal/) will be used to manage the life of your notes with the cloud storage service

* Python >= 3.6
* [Django Rest Framework](http://www.django-rest-framework.org/#installation)
* django-environ

#### installation

```python
python3 -m venv joplin-web
cd joplin-web
source bin/activate
git clone https://github.com/foxmask/joplin-web
cd joplin-web
pip install -r requirements.txt
```

#### settings 

copy env.sample to .env

then set the JOPLIN_PATH to the database

#### Database

```python
python manage.py migrate
```

this will add the tables of django but will not change any joplin tables

### Running

```python
python manage.py runserver localhost:8001 &
```

### for frontend

* [VueJS](https://vuejs.org) (Vuex, axios)

## why that project ?

Because it may happened we need to access to [Joplin](https://joplin.cozic.net/) without having access to his/her smartphone or the Joplin Desktop, and a Web Application could to the trick at a given moment.

### Installation

see `joplin-web/README.md` file
