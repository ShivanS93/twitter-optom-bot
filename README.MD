# OptomBot - A Twitter Bot
*Made by Shivan Sivakumaran*

Started: 16th December 2020

## Introduction

This is a fun little project for me to get acquainted with twitter API through use of `tweepy`. In addition to this, I gain experience in deployment using Docker and Amazon EC2 instance.

The objective is to create a bot that favourites and retweets Optometry related posts on twitter.

[Here is a blog post related to motivation and inception of the bot](https://shivansivakumaran.com/coding/how-i-created-a-twitter-bot-to-help-my-career-as-an-optometrist/).

# TO-DOs

- [X] Add more hashtags - optometry and ophthalmology (can only have two hashtags)
- [X] Prevent retweeting the same retweet - author silencing?
- [ ] ~~Learn how to redeploy on docker and create testing ability~~
- [ ] ~~Add content from Youtube~~
- [ ] DM status
- [ ] Most commented / liked post of the month/week?

## Structure of files

```
TwitterOptomBot/
|
|--- bots/
|	|--- config.py
|	|--- fav_and_retweet.py
|   |--- database_connector
    |--- database.db
|	|--- .env**
|--- requirements.txt
|--- Dockerfile
|--- README.MD
|
```
** .env files needs to be created

## .env file

This file is used to contain the environment variables, which will house the API keys and tokens. The file is structured as follows:
```
APIkey=<API Key>
APISecretKey=<API Secret Key>
BearerToken=<Bearer Token>
AccessToken=<Access Token>
AccessTokenSecret=<Access Token Secret>
```
## requirements.txt

This contains the packages necessary for this project. Ensure you create a virtual environment. Then, install the packages from the `requirements.txt`. There an assumption that we are using Python 3.7+.

```
python3 -m virtualenv <name of virtual environment>
source <name of virtual environment>/bin/acivate
pip3 -r requirements.txt
```

## Link to the bot

[Here is the bot on twitter](https://twitter.com/OptomBot)

## Feedback

If you have any feedback, [please get in touch with me](https://shivansivakumaran/contact).
