#!/usr/local/bin/python3


import requests 
import time 
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from decouple import config
from datetime import datetime 



def telegram_bot_sendtext(bot_message):

    bot_token = config('TELE_TOKEN')
    bot_chatID = config('CHAT_ID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)


#Function Obtain Slots Of EKM District
def dist(district_id): 
    district = district_id 
    today = datetime.today() 
    date = today.strftime("%d-%m-%Y") 
    slots = {} 
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district}&date={date}" 
    data = requests.get(url).json() 
    mes = ""
    for center in data['sessions']: 
 
        if center[ 'min_age_limit' ] == 45 and center[ 'available_capacity_dose1' ] > 0 : 
           a = '\033[1m' + 'Vaccine slots are available for age 18+\n' + '\033[0m'
           b =  center['name'] + '\n' + 'Location: ' + center['address'] + '\n' 
           c = 'Vaccine : ' + center['vaccine'] + '\n'
           d = 'Dose 1 : ' + str(center['available_capacity_dose1']) + ' | ' +' Dose 2 : ' + str(center['available_capacity_dose2']) + '\n'
           e = 'Fee : ' + center['fee'] + '\n'
           l = 'Book Now: https://selfregistration.cowin.gov.in'
           result = a + b + c + d + e + l
           telegram_bot_sendtext(result)
           print(result)
           time.sleep(2)
           #telegram_bot_sendtext(result)

##def main():


if __name__ == "__main__":
    dist(307)
    #telegram_bot_sendtext(slots)
    

            

    
