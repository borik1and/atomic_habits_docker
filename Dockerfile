FROM python:3

WORKDIR /atomic_habits

COPY ./requirements.txt /atomic_habits/

RUN pip install -r requirements.txt

COPY . .

