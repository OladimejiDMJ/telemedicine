FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /telemedicine_api
WORKDIR /telemedicine_api
COPY . /telemedicine_api/
RUN pip install -r requirements.txt