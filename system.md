# System settings

you may need to check the number of opened files before starting the application

enter 
```shell script
ulimit -n
1024
```
means 1024 files are opened

and if you enconter this error 
```shell script
OSError: [Errno 24] Too many open files
```
then raise the number by entering
```shell script
ulimit -n 2048 
```
and start the application again