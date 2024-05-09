# Little Lemon Backend in Python

Default users:
admin - admin - 6f477c2c557637d58e7b94d44372500895f0f466
manager - man12345 - a85abe70805618fb73e65f53eddb56639b25da13
delivery - del12345 - 9ea2c033ab5318498bbd77cb8716e35980aac359
customer1 - cust12341 - a399e4820d4a696b8914353eac8d17ca788af4bd
customer2 - cust12342 - 38a8b93e2e8e05b2514461ebe8626fe58bec5c36
customer3 - cust12343 - 29577774b1ad9c48b8a67e5d73dc4be7a9b5c404

## How to ...

### How to install all dependencies

1. Install python
```bash
brew install python
```

2. Activate virtual env
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Django
```bash
python3 -m pip install Django
```

4. Install DRF
```bash
pip install djangorestframework
pip install markdown
pip install django-filter
```

5. Install Djoser
```bash
pip install -U djoser
```

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