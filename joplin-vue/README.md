# Joplin-Vue : The Front End of the project

## Requirements

* [VueJS](https://vuejs.org)2 with :
  * Vuex
  * vuex-map-fields
  * axios
  * marked
  * dompurify
  * jsdom
  * js-cookie
  * bootstrap-vue

## Project setup
```
npm install
```
you can set the environment variable `JW_BASE_URL` to allow providing the application else where instead of "/"
for example : 
```
20:31:02 [foxmask@foxmask:~/Projects/joplin-web] $ export JW_BASE_URL='/joplin/'
 INFO  Starting development server...
 98% after emitting CopyPlugin                                                    

 DONE  Compiled successfully in 5070ms                                                                                                                                                                                              8:31:46 PM

 
  App running at:
  - Local:   http://localhost:8080/joplin/ 
  - Network: http://192.168.1.23:8080/joplin/
```
### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

## Joplin-web : The BackEnd

if you want to change the port of your back edit vue.config.js and change
```
target: 'http://127.0.0.1:8001'
```
to the value that fit your needs

see [`joplin-web/joplin_web/README.md`](../README.md) file

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Project structure

- joplin-vue
  - src
    - modules
      - folders (list the folders)
        - components
          - Folder
          - Folders
      - notes (list the note + form to create note)
        - components
          - Note
          - Notes
          - Tag
          - TakeNote
      - tags (list of tags)
        - components
          - Tags
