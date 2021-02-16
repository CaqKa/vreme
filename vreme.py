# Vreme izris
# TODO Izrišem temperature iz dvodnevne arso napovedi za podravsko regijo
# TODO preberem podatke iz 5-dnevne napovedi ARSO: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/forecast_SI_PODRAVSKA_latest.xml
# XML iz katerega jemljem podatke je: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml

import ARSO_API as arso
import json
from lxml import etree
import xmltodict, json



xmlNapoved = arso.prikaziNapoved()
obj = xmltodict.parse(xmlNapoved)
napovedneTocke = obj['data']['metData']
print(json.dumps(obj['data']['metData']))
for tocka in napovedneTocke:
    print(tocka['t'])