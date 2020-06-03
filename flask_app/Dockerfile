# import Python 3.6.7 image
FROM python:3.6.7

# set working directory to /app
WORKDIR /app

# copy requirements.txt
COPY requirements.txt .

# install requirements.txt packages
RUN pip install -r requirements.txt

# copy all contents from flask_app/
COPY . .
