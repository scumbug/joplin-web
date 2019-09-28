# Docker

if you prefer to run the project from docker follow that steps:


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
