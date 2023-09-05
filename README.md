# MMORPG - Портал с обьявлениями для онлайн игр

## Getting Started
First create virtualenv (venv) in you directory

Create .env file and install your settings for mailing:

    $ EMAIL_HOST = "..."
    $ EMAIL_PORT = "..."
    $ EMAIL_HOST_USER = "..." 
    $ EMAIL_HOST_PASSWORD = "..."
    $ DEFAULT_FROM_EMAIL = "..."
    $ EMAIL_USE_SSL = True  

Second clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/BYKEFAL/MMORPG.git
    $ cd MMORPG
    
Activate the virtualenv (venv) for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate
    
You can now run the development server:

    $ python manage.py runserver
