import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level = logging.INFO)


PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,'password': settings.PROXY_USERPASSWORD}}

def greet_user(update, context):
    print('Вызваг/srart')
    update.message.reply_text('Я Бетмен!')

def talk_to_me(updete, context):
    text= updete.message.text
    print(text)
    updete.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Batman on mission')
    mybot.start_polling()
    mybot.idle()

main()
