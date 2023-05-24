FROM python:3.10-slim-buster

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=True

EXPOSE ${PORT}
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]