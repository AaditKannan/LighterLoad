import json
import time

from boltiot import Bolt, Sms

# maximum psi

# bolt iot information
API_KEY = "40c5a6d3-4b0a-4f2f-adae-3c765cd1eca8"
DEVICE_ID = "BOLT11691709"

# twilio information
SID = 'AC9d0925c6c78d5a8a7d65feeec4e78293'
AUTH_TOKEN = 'e2382584894081862e6672ebe051ab69'
FROM_NUMBER = '+14086179256'
TO_NUMBER = '+17345460380'

# serial read (getting the data from arduino)
mybolt = Bolt(API_KEY, DEVICE_ID)
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER)
response = mybolt.serialRead('10')
print(response)

# while loop to send message
while True:
    response = mybolt.serialRead('10')
    data = json.loads(response)
    ALERT = data['value'].rstrip()
    print("Pressure is", ALERT, "PSI")
    if len(ALERT) == 1:
        if int(ALERT) == 0:
            response = sms.send_sms('Warning, your town can possibly be at risk of flooding.')
        if int(ALERT) == 1:
            print("Nothing")
    time.sleep(1)





