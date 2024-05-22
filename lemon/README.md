# Little Lemon Backend in Python

Default users:

admin - admin - 6f477c2c557637d58e7b94d44372500895f0f466

manager - man12345 - a85abe70805618fb73e65f53eddb56639b25da13

delivery - del12345 - 9ea2c033ab5318498bbd77cb8716e35980aac359

customer1 - cust12341 - a399e4820d4a696b8914353eac8d17ca788af4bd

customer2 - cust12342 - 38a8b93e2e8e05b2514461ebe8626fe58bec5c36

customer3 - cust12343 - 29577774b1ad9c48b8a67e5d73dc4be7a9b5c404

## How to ...

### How to install all dependencies on macOS

1. Install python
```bash
brew install python
```

2. Activate virtual env
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install Django
```bash
python -m pip install Django
```

4. Install DRF
```bash
pip install djangorestframework
```

5. Install markdown
```bash
pip install markdown
```

6. Install django-filter
```bash
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

Install 'SQLite Viewer' plugin on your VS code

### How to create a new app

```bash
python manage.py startapp YOUR_APP_NAME
```

### How to create an admin user

```bash
python manage.py createsuperuser
```

### How to make model migrations

```bash
# creates file 0001_initial.py which creates a model file for API app
python manage.py makemigrations api
# creates file 0001_initial.py which creates a model file for Lemon app
python manage.py makemigrations lemon
# apply migrations
python manage.py migrate
# show all migrations
python manage.py showmigrations
# log into sqlite3 shell
pythom manage.py dbshell
```

### How to start up Django project

```bash
python manage.py runserver
```

### How to install and start up MySQL on macOS
Install mysql using next command in terminal (*install brew before)

```bash
brew install mysql
```

We've installed your MySQL database without a root password. To secure it run:
```bash
mysql_secure_installation
```

MySQL is configured to only allow connections from localhost by default

To connect run:
```bash
mysql -u root
```

To start mysql now and restart at login:
```bash
brew services start mysql
```
Or, if you don't want/need a background service you can just run:
```bash
/opt/homebrew/opt/mysql/bin/mysqld_safe --datadir\=/opt/homebrew/var/mysql
```

### How to install MySQL libraries

```bash
brew install pkg-config
```

Upgrade pip
```bash
pip3 install --upgrade pip
```

Upgrade setup tools
```bash
python3 -m pip install --upgrade setuptools
```

Install python connector
```bash
pip3 install mysql-connector-python
```

Install mysqlclient
```bash
pip3 install mysqlclient
```

### How to create a FID user in MySQL

Connect to MySQL database and execute
```bash
CREATE USER 'mysql_fid'@'localhost' IDENTIFIED BY 'mysql_fid' ;
```

```bash
GRANT ALL ON *.* TO 'mysql_fid'@'localhost';
```

```bash
FLUSH PRIVILEGES;
```