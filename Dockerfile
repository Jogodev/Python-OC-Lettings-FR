FROM python:3.11.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
