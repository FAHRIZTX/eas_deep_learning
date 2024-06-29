FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/community" >> /etc/apk/repositories

RUN pip install flask gunicorn

RUN apk update && apk add py3-scikit-learn

CMD ["python", "app.py"]