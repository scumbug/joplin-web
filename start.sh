#!/usr/bin/env bash
source ../bin/activate
cd joplin-vue
npm run serve &
cd ../joplin_web
python app.py &

