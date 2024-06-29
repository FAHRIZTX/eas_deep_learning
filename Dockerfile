FROM python:3.10

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install numpy scikit-learn flask gunicorn

CMD ["python", "app.py"]