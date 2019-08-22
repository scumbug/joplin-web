# Joplin Web : The BackEnd

A Web application for [JoplinApp](https://joplinapp.org)

## why that project ?

Because it may happened we need to access to [JoplinApp](https://joplinapp.org) without having access to his/her smartphone or the Joplin Desktop, and a Web Application could to the trick at a given moment.

## Requirements

* Python >= 3.6
* [Joplin-API](https://github.com/foxmask/joplin-api)
* [starlette](https://starlette.io)

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

then set at least this parm: 

* the `JOPLIN_WEBCLIPPER_TOKEN` you have in the Webclipper config page in Joplin
* the `JOPLIN_RESOURCES` to find the files of joplin and being able to load them in the editori 

the config file is commented to be able to help you to fill the parameters, like `HTTP_PORT`, `PAGINATOR` or `DEBUG`


### Running

```python
python app.py &
Joplin Web - Starlette powered
Started server process [10043]
Waiting for application startup.
Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
```

Don't forget to start your joplin editor to be able to reach the webclipper port 

# Docker

## build the docker image by

```
docker build -t joplin-web-build . 
```

## run the image
```
docker run --network="host" -p 8001:8001 -v JOPLIN_RESOURCES:/path/to/.config/joplin-desktop/resources joplin-web-build

docker run --network="host" -p 8001:8001 -v JOPLIN_RESOURCES:/home/foxmask/.config/joplin-desktop/resources joplin-web-build
WARNING: Published ports are discarded when using host network mode
Joplin Web - Starlette powered
2019-08-22 17:43:39,659 - INFO - Started server process [1]
2019-08-22 17:43:39,659 - INFO - Waiting for application startup.
2019-08-22 17:43:39,661 - INFO - Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
2019-08-22 17:43:49,374 - INFO - ('127.0.0.1', 50996) - "GET / HTTP/1.1" 200
2019-08-22 17:43:49,458 - INFO - ('127.0.0.1', 50996) - "GET /static/css/chunk-vendors.css HTTP/1.1" 200
2019-08-22 17:43:49,464 - INFO - ('127.0.0.1', 50998) - "GET /static/js/chunk-vendors.js HTTP/1.1" 200
2019-08-22 17:43:49,465 - INFO - ('127.0.0.1', 51000) - "GET /static/js/app.js HTTP/1.1" 200
2019-08-22 17:43:50,408 - INFO - ('127.0.0.1', 51026) - "GET /favicon.ico HTTP/1.1" 404
2019-08-22 17:43:50,648 - INFO - ('127.0.0.1', 50996) - "GET /api/jw/tags/ HTTP/1.1" 200
2019-08-22 17:43:51,230 - INFO - ('127.0.0.1', 51000) - "GET /api/jw/notes/ HTTP/1.1" 200
2019-08-22 17:43:51,666 - INFO - ('127.0.0.1', 50998) - "GET /api/jw/folders/ HTTP/1.1" 200

```


# Joplin-front : The Frontend

see [`joplin-web/joplin-vue/README.md`](joplin-vue/README.md) file

![Joplin web](https://raw.githubusercontent.com/foxmask/joplin-web/master/joplin_web.png)


