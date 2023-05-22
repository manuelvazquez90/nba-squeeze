FROM python:3.10-slim-buster

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE 8000
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]
CMD ["python", "app.py"]