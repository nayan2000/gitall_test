# project_madara

## Basic Principle

If you have to write a code thrice; make a function.
If you have to explain something thrice; write to gitalltech.

## Run Locally

### 1. Get it onto your system | we prefer ubuntu 

	git clone https://github.com/gitalltech/gitall

### 2. Basic set up
	
	cd project_madara
	
#### 2.1 Creating a virtual environment
	M virtualenv 
	virtualenv 
	venv source venv/bin/activate

#### 2.2 Installing the requirements

	pip install -r requirements.txt

#### 2.3 Setting up the database | we use postgres

	sudo apt-get install libpq-dev postgresql postgresql-contrib

	sudo -i -u postgres

	psql

	# this should bring you in a console.
	create database <database_name>;

	create user <username> with password '<password>';

	grant all privileges on database <database_name> to <username>;

	\q

	exit

#### 2.4 Do the corresponding changes to ProjectMadara/settings.py [line 109]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gitalldb',
            'USER': 'gitalluser',
            'PASSWORD': 'gitall@12345',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

### 3. Running django

    cd projectMadara

	python manage.py migrate

	python manage.py runserver

#### Access the site at 127.0.0.1:8000/

### 4. Creating a superuser

	ctrl+c # this exits you from the running django local-server

	python manage.py createsuperuser

	# proceed accordingly by adding a username and password

	python manage.py runserver

#### 4.1 Access the admin panel at 127.0.0.1:8000/admin

### 5. Happy Coding. No mames!

Want to contribute to the project? Mail us at: team@gitall.tech
