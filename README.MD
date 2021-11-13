# OptomBot - A Twitter Bot
[![Build](https://github.com/ShivanS93/twitter-optom-bot/actions/workflows/main.yml/badge.svg)](https://github.com/ShivanS93/twitter-optom-bot/actions/workflows/main.yml)
*Made by Shivan Sivakumaran*

## Introduction

This is a fun little project for me to get acquainted with twitter API through use of `tweepy`. In addition to this, I gain experience in deployment using Docker ~~and Amazon EC2 instance~~ and a Digital Ocean droplet.

The objective is to create a bot that favourites and retweets Optometry related posts on twitter.

[Here is a blog post related to motivation and inception of the bot](https://shivansivakumaran.com/coding/how-i-created-a-twitter-bot-to-help-my-career-as-an-optometrist/). Though this blog is slightly outdated.

## Running it yourself

This requires creating your own requirement `.env` file and authenticated access for a bot account through https://dev.twitter.com.

The `.env` file is used to contain the environment variables, which will house the API keys and tokens. The file is structured as follows:
```
APIkey=<API Key>
APISecretKey=<API Secret Key>
BearerToken=<Bearer Token>
AccessToken=<Access Token>
AccessTokenSecret=<Access Token Secret>
```

## Some more pre-requistes

This requires
- `pipenv`
- `docker`and `docker-compose`
- Any python 3.8.10

## Link to the bot

[Here is the bot on twitter](https://twitter.com/OptomBot).

## Feedback

If you have any feedback, [please get in touch with me](https://shivansivakumaran/contact).
