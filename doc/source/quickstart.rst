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

5. **Run the development server** ::

    python manage.py runserver         

6. Go to your browser at the address http://localhost:8000