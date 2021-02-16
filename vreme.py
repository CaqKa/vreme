# Vreme izris
# TODO Izrišem temperature iz dvodnevne arso napovedi za podravsko regijo

# TODO preberem podatke iz 5-dnevne napovedi ARSO: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/forecast_SI_PODRAVSKA_latest.xml
# XML iz katerega jemljem podatke je: http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml

from ARSO_API import meteoarsogovsi as arso
import json
from lxml import etree

def prikaziNapoved():
    url = "uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml"
#    napoved = json.loads(arso(url))
#    print(json.dumps(napoved, indent=1))
#    napoved = arso(url)
#    return napoved

prikaziNapoved()
url="http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl//forecast_SI_PODRAVSKA_int3h.xml"
tree = etree.parse(url)
convert(tree)
print(tree)
