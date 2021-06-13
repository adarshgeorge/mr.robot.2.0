from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from decouple import config

#VARS

YOUR_TOKEN=config('TELE_TOKEN')
ID=config('CHAT_ID')

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = ID
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(YOUR_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
