Quick Start
===========


1. **Create virtual environnement** ::

    cd python -m venv venv

2. **Activate the virtual environment** ::

    Windows:

    . venv/scripts/activate

    Mac, Linux:
    
    source venv/scripts/activate

3. **Install dependencies** ::

    pip install -r requirements.txt

4. **Add a .env file with the following variables** ::

    SENTRY_DSN = « Your sentry DSN »

    SECRET_KEY = « Your django SECRET KET »

    DEBUG = boolean

5. **Run the development server** ::

    python manage.py runserver         

6. Go to your browser at the address http://localhost:8000

With docker
===========

1. **Build the image at the root** ::

    docker build -t [tag] .

2. **Run the container** ::

    docker run -d -p [8000:8000] [tag]

3. Go to your browser at the address http://localhost:8000

With the last image on Docker Hub
=================================

1. **Make sure you create a .env file** ::

    docker run -d --pull always -p 8000:8000 --env-file .env [username]/[image-name]:[tag]
