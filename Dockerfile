FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN apt install build-essentials

RUN pip install -r requirements.txt

CMD ["python", "app.py"]