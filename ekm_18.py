import requests
import time
from datetime import datetime

district = "307"
today = datetime.today()
#date = today.strftime("%d-%m-%Y")
date = "12-06-2021"


url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district}&date={date}"

data = requests.get(url).json()
for center in data['sessions']:
    #print(center['name'], center['min_age_limit'], center['slots'], center['available_capacity'], center['available_capacity_dose1'])
    #time.sleep(2)
    if center[ 'min_age_limit' ] == 18 and center[ 'available_capacity_dose1' ] > 0 :
        print( center['vaccine'] ,'Dose1:' , center['available_capacity_dose1'], center['name'], 'Age limit:', center['min_age_limit'])
         
time.sleep(10)       
        
