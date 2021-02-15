# Vreme izris
# TODO Izrišem temperature iz dvodnevne arso napovedi za podravsko regijo
# XML iz katerega jemljem podatke je: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml
# import hashlib
# import hmac
# import time
import requests
# import uuid
# import sys
# import json

import requests
from lxml import etree
# from io import StringIO, BytesIO
# from lxml2json import convert


def APIpublic(url):
    r = requests.get("http://meteo.arso.gov.si"+url)
#    data = r.json()
#    orderBook = json.loads(data)
###    print(json.dumps(orderBook))
    return r.content

# urlKratek="/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml"
url="http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml"
tree = etree.parse(url)
print(tree)
# tree =etree.parse(StringIO(APIpublic(url)))
# etree.tostring(tree.getroot())
# print(APIpublic(url));
# podatkiJson=convert(tree)
# print(podatkiJson)

