import datetime  


def tom(): 
    base = datetime.datetime.today()  
    for x in range(0,2):  
        xday = base + datetime.timedelta(days=x)  
        #print(xday.strftime('%d-%m-%Y'))
    print(xday.strftime('%d-%m-%Y'))
tom()