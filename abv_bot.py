from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def start(update, context):
    text = update.message.text.split()
    new_text = []
    for elem in text:
        if 'абв' not in elem:
            new_text.append(elem)
    context.bot.send_message(update.effective_chat.id, ' '.join(new_text))


start_handler = MessageHandler(Filters.text, start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
