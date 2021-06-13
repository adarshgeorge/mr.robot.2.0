import requests
from decouple import config

def telegram_bot_sendtext(bot_message):

   bot_token = config('TELE_TOKEN')
   bot_chatID = config('CHAT_ID')
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
