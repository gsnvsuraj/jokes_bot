from telegram.ext import Updater, MessageHandler, Filters

# creating new event handler, constantly pulling new messages
updater = Updater(token="827833998:AAEKKJvsXmaI5yMIkqoDeHczNzm5QNpB1ow")

# add new event handler
dispatcher = updater.dispatcher

def echo(bot, update):
    update.message.reply_text(update.message.text)

dispatcher.add_handler(MessageHandler(Filters.text, echo))

# start pulling
updater.start_polling()

'''import telegram

bot = telegram.Bot(token="827833998:AAEKKJvsXmaI5yMIkqoDeHczNzm5QNpB1ow")

for chat in bot.getUpdates():
    print(chat.message.text)'''

'''import requests

req = requests.get('https://api.telegram.org/bot827833998:AAEKKJvsXmaI5yMIkqoDeHczNzm5QNpB1ow/getUpdates')

print(req.json())

for chat in req.json()["result"]:
    print(chat["message"]["text"])'''