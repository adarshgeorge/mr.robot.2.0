import requests 
import time 
import twilio
from twilio.rest import Client
from decouple import config
from datetime import datetime 
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
def dist(district_id): 

    district = district_id 
    today = datetime.today() 
    date = today.strftime("%d-%m-%Y")
    print(date) 
    slots = {} 
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district}&date={date}" 

    data = requests.get(url).json() 
    for center in data['sessions']: 
 
        if center[ 'min_age_limit' ] == 18 and center[ 'available_capacity_dose1' ] > 0 : 
            slots[center['name']] = [ {'dose1' : center['available_capacity_dose1']},  {'Age limit': center['min_age_limit']} ] 
    return(slots) 
     
message = client.messages \
    .create(
         body='Hi Groot!\n {}'.format(dist(571)),
         from_='whatsapp:+14155238886',
         to='whatsapp:+919633131216'
     )

print(message.sid)  
print(dist(571)) 
