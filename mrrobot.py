import requests 
import time 
import twilio
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from twilio.rest import Client
from decouple import config
from datetime import datetime 


#Function Obtain Slots Of EKM District

def dist(district_id): 

    district = district_id 
    today = datetime.today() 
    date = today.strftime("%d-%m-%Y") 
    slots = {} 
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district}&date={date}" 

    data = requests.get(url).json() 
    for center in data['sessions']: 
 
        if center[ 'min_age_limit' ] == 18 and center[ 'available_capacity_dose1' ] > 0 : 
            slots[center['name']] = [ {'dose1' : center['available_capacity_dose1']},  {'Age limit': center['min_age_limit']} ] 
    return(slots) 
     
slots = dist(571)
print(slots)


def telegram_bot_sendtext(bot_message):

   bot_token = config('TELE_TOKEN')
   bot_chatID = config('CHAT_ID')
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext(str(slots))
print(test)

    
