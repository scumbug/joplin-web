#!/usr/bin/env bash
cd joplin-vue
npm run serve &
cd ../joplin_web
python app.py &

