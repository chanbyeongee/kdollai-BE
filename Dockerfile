FROM python:3.8-slim

COPY . /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

CMD ["python3","app.py"]

