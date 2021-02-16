# ARSO API
# branje iz strani kot je: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/forecast_SI_PODRAVSKA_latest.xml
#import hashlib
#import hmac
#import time
import requests
#import uuid
#import sys
#import json



def meteoarsogovsi(url):
    r = requests.get("http://meteo.arso.gov.si"+url)
#     data = r.json()
#     vremenskaNapoved = json.loads(data)
    return r.content


# Naloži xml preko requests
def prikaziNapoved():
    url = "/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml"
#    napoved = json.loads(meteoarsogovsi(url))
#    print(json.dumps(napoved, indent=1))
    napoved = meteoarsogovsi(url)
    return napoved