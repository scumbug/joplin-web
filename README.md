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


If you plan to use joplin-terminal and not the WebClipper, in your `.env` file, set `API_USE_JOPLIN_WEBCLIPPER` to `False` then joplin-web will switch of API calls from Rest to command line.


### Running

```python
python app.py &
Joplin Web - Starlette powered
Started server process [10043]
Waiting for application startup.
Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
```

Don't forget to start your joplin editor to be able to reach the webclipper port 

# Joplin-front : The Frontend

see [`joplin-web/joplin-vue/README.md`](joplin-vue/README.md) file

![Joplin web](https://raw.githubusercontent.com/foxmask/joplin-web/master/joplin_web.png)


