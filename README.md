# Joplin Web : The BackEnd

A Web application for [JoplinApp](https://joplinapp.org)

## why that project ?

Because it may happened we need to access to [JoplinApp](https://joplinapp.org) without having access to his/her smartphone or the Joplin Desktop, and a Web Application could to the trick at a given moment.

## Requirements

* Python >= 3.6
* [Joplin-API](https://github.com/foxmask/joplin-api)
* [Django Rest Framework](http://www.django-rest-framework.org/#installation)
* django-environ
* requests

## Installation 

```python
python3 -m venv joplin-web
cd joplin-web
source bin/activate
git clone https://github.com/foxmask/joplin-web
cd joplin-web
pip install -r requirements.txt
```

### settings 

copy env.sample to .env

then set : 

* the `JOPLIN_PATH` to the database 
* the `JOPLIN_TOKEN` you have in the Webclipper config page in Joplin


If you plan to use joplin-terminal and not the WebClipper, in your `.env` file, set `API_USE_JOPLIN_WEBCLIPPER` to `False` then joplin-web will switch of API calls from Rest to command line.


#### Database

```python
python manage.py migrate
```

this will add the tables of django but will not change any joplin tables

### Running

```python
python manage.py runserver localhost:8001 &
```
if you map another port, you will need to have a look at the front end `vue.config.js` file

don't forget to start your joplin editor to be able to reach the webclipper port 

## Docker 

if you prefer to use docker instead of using the previous virtualenv, set the paramaters from the ` settings` section above
then

### build

build the image docker
```
docker build -t foxmask/joplin-web .
```

### run

then launch it like this
```
docker run -it --network host -p 8001:8001 --rm --name foxmask-joplin-web-1 --mount type=bind,source="/home/foxmask/.config/joplin-desktop/database.sqlite",target=/home/foxmask/.config/joplin-desktop/database.sqlite foxmask/joplin-web
```

explanations :

1) we will need to "mount" a volume to access to the Joplin database from our docker container 

this is the purpose of the ` --mount` parm with `source` and `target` which point, both, to the path `/home/foxmask/.config/joplin-desktop/database.sqlite`
this is needed by the `.env` file  where you will need to set the JOPLIN_PATH which is in my case `/home/foxmask/.config/joplin-desktop/`
 
2) Once the image is built, docker does not even know our local Joplin Webclipper service on the port 41148, so the final trick is to use :
`--network host` which allow docker to access to the network of the host, and here we go.
 
### changing the port 8001 

if you want / need to switch the 8001 for the docker image, you will need to make the following changes :

1) edit the Dockerfile and change 8001 anywhere with your own port
2) change the param `-p` on the `docker run` command 


# Joplin-front : The Frontend

see [`joplin-web/joplin-vue/README.md`](joplin-vue/README.md) file

![Joplin web](https://raw.githubusercontent.com/foxmask/joplin-web/master/joplin_web.png)


