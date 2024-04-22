# Little Lemon Backend in Python


## How to ...

### How to debug

In Visual Studio Code go to 'Run and Debug' screen on the rigth tab.
Click 'create a launch.json file' -> Python -> Django -> now you can put your break points -> go to 'Run' on the top -> Start debugging

### How to setup your project in Visual Studio Code

Install 'SQLite Viewer' on your vs code

### How to create a new app

```bash
python manage.py startapp YOUR_APP_NAME
```


### How to start up the server

```bash
python manage.py runserver
```

### How to make model migrations

```bash
# creates file 0001_initial.py which creates a model file
python manage.py makemigrations
# apply migrations
python manage.py migrate
# show all migrations
python manage.py showmigrations
# log into sqlite3 shell
pythom manage.py dbshell
```

### How to create an admin user

```bash
python manage.py createsuperuser
```