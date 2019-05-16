from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests, random

# creating new event handler, constantly pulling new messages
updater = Updater(token="827833998:AAEKKJvsXmaI5yMIkqoDeHczNzm5QNpB1ow")

# add new event handler
dispatcher = updater.dispatcher

def choices(bot, update):
    options = [
        [InlineKeyboardButton("Reddit Jokes", callback_data="redditjokes"),
         InlineKeyboardButton("Stupid Stuff", callback_data="stupidstuff"),
         InlineKeyboardButton("Wocka", callback_data="wocka")]
    ]

    reply = InlineKeyboardMarkup(options)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Choose a joke type : ",
                     reply_markup=reply)

dispatcher.add_handler(CommandHandler("jokes", choices))

def jokes(bot, update):
    data = update.callback_query.data
    joke = ""

    if(data == "redditjokes"):
        req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json")
        length = len(req.json())
        select = random.randint(0, length)
        joke = req.json()[select]["title"] + "\n" + req.json()[select]["body"]

    elif(data == "stupidstuff"):
        req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json")
        length = len(req.json())
        select = random.randint(0, length)
        joke = req.json()[select]["title"] + "\n" + req.json()[select]["body"]

    elif(data == "wocka"):
        req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json")
        length = len(req.json())
        select = random.randint(0, length)
        joke = req.json()[select]["title"] + "\n" + req.json()[select]["body"]

    bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                          text=joke,
                          message_id=update.callback_query.message.message_id)

dispatcher.add_handler(CallbackQueryHandler(jokes))

# start pulling
updater.start_polling()

updater.idle()