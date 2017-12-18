# Echo Bot
This was part of the Facebook Developer Circle: Beirut. This tutorial is gonna be delivered on Monday, December 18,2017 at 7:30 PM before the Recurrent Neural Network Session.

## Prerequisites
* Account on Telegram
* Python 2.7 (Does work on python 3 just not my code.)
* A text editor to edit the code and I way to run it.

  I personally use Atom as a text editor and I compile the code from the terminal using the Run Script Addon. Just make sure you add Python 2.7 to your *Path* Variable for it work

* You need to install the following libraries for python: time, grequests, urllib, and json

## Description
This bot is a simple repeat after me. The bot simply sends back what the individual sends to it. The session will take 45 minutes from setting up the bot to testing and executing the code.

## The main URLs
* To Send a message
> https://api.telegram.org/bot444874958:AAGjLuhNCjvZGJkNnwCCP5c4cffIMy_vkNA/sendMessage?text={}&chat_id={}&parse_mode=markdown

* To Receive Messages
>https://api.telegram.org/bot444874958:AAGjLuhNCjvZGJkNnwCCP5c4cffIMy_vkNA/getUpdates

## Extra Resources
* https://core.telegram.org/bots/api
* https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
* You could later on integrate a NLP library like RASA (https://rasa.ai) or wit (https://wit.ai/ ). There are multiple ones but these are free and open sourced.
* If you plan on hosting the code somewhere. Heroku provides free cloud computing.
