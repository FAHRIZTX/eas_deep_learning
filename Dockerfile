FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/community" >> /etc/apk/repositories

# RUN apk update && apk add --no-cache \
#                 ca-certificates \
#                 openblas

# RUN apk update && apk add python3-dev \
#                           gcc \
#                           libc-dev \
#                           libffi-dev \
#                           make cmake \
#                           g++ \
#                           zlib-dev \
#                           gfortran \
#                           openblas-dev

# RUN pip install -r requirements.txt

RUN apk update && apk add py3-scikit-learn

CMD ["python", "app.py"]