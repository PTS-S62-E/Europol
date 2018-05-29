FROM python:latest

RUN mkdir /europol
WORKDIR /europol

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
RUN mkdir /europol/static

CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000