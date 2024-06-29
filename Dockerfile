FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-binary :all: -r requirements.txt

CMD ["python", "app.py"]