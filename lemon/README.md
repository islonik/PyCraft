# Little Lemon Backend in Python

Default test users:
admin - admin - fc7033f3e9a75a22f2951504c44188f671468d13
manager - man12345 - 7c837a4d4a50d65dccaa6ba7acb25e12ea959703
delivery - del12345 - 7e586f9722485180d4d13e3245a8e4df69a8d794
customer - cust12345 - 6cb63cf21cba4dfc4aee9cc83ef64cce32f59e90

## How to ...

### How to debug

In Visual Studio Code go to 'Run and Debug' screen on the rigth tab.
Click 'create a launch.json file' -> Python -> Django -> now you can put your break points -> go to 'Run' on the top -> Start debugging

### How to use profiling

1. Install Django debug toolbar
```bash
pip3 install django-debug-toolbar
```

2. Add 'debug_toolbar' in INSTALLED_APPS

3. Add next url in urlpatterns
```bash
path('__debug__', include('debug_toolbar.urls')),
```

4. Include middleware
```bash
'debug_toolbar.middleware.DebugToolbarMiddleware',
```

5. Add below section in settings.py
```bash
INTERNAL_IPS = [
    '127.0.0.1'
]
```

6. Profiling should be accessible on the right side API endpoint


### How to setup your project in Visual Studio Code

Install 'SQLite Viewer' on your VS code

Install DRF
```bash
pip3 install djangorestframework
```

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