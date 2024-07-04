FROM python:3.9

RUN pip install --upgrade pip

RUN apt update && apt install -y libhdf5-dev

WORKDIR /app

COPY . /app

#RUN pip install -r requirements.txt

RUN python -m pip install flask
RUN python -m pip install gunicorn
RUN python -m pip install numpy==1.24.2
RUN python -m pip install scikit-learn==1.2.1
RUN pip install tensorflow==2.15.0

CMD ["python", "app.py"]
