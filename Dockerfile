FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/community" >> /etc/apk/repositories

RUN apk update && apk add py3-scikit-learn

RUN pip install -r requirements.txt

CMD ["python", "app.py"]