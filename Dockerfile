FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev \
                          make cmake \
                          g++ \
                          zlib-dev \
                          gfortran

RUN pip install -r requirements.txt

CMD ["python", "app.py"]