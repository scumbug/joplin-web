# Joplin Web : The BackEnd

A Web application for [JoplinApp](https://joplinapp.org)

## why that project ?

Because it may happened we need to access to [JoplinApp](https://joplinapp.org) without having access to our smartphone or the Joplin Desktop, and a Web Application could to the trick at a given moment.

## Requirements

* Python >= 3.6
* [joplin-api](https://github.com/foxmask/joplin-api)
* [starlette](https://www.starlette.io)

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

to be able to manage the joplin note from the web app, we need to start :

* if you are on your workstation just start "Joplin Desktop"
* if you are using joplin on a dedicated server, you can start "joplin headless", as follow
```
joplin --profile ~/.config/joplin-desktop/ server start
Server is already running on port 41184
```
joplin headless is available with the "joplin terminal" version (since build 147), you can install like that 
```
NPM_CONFIG_PREFIX=~/.joplin-bin npm install -g joplin
sudo ln -s ~/.joplin-bin/bin/joplin /usr/bin/joplin
```
(have a look at https://joplinapp.org/ for more details)

once this is running, start the backend part of joplin-web app like this
```python
python app.py &
Joplin Web - Starlette powered
Started server process [10043]
Waiting for application startup.
Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
```

# Joplin-front : The Frontend

see [`joplin-web/joplin-vue/README.md`](joplin-vue/README.md) file

![Joplin web](https://raw.githubusercontent.com/foxmask/joplin-web/master/joplin_web.png)


# Joplin-web : Docker

if you prefer to run the project from docker :

see [joplin-web/docker.md](docker.md) for details
