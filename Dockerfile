FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/fav_and_retweet.py /bots/
COPY bots/.env /bots/
COPY bots/database_connector.py /bots/
COPY bots/database.db /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "fav_and_retweet.py"]

