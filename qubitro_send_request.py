import urequests
import ujson

url = "https://webhook.qubitro.com/integrations/http"

# First Device
#headers = {
#    'Authorization' : 'Basic OjgURfXrPFI$PLhhW$1LJQq$CuiMi2q57bad5DSM',
#    'Content-Type' : 'application/json'
#    }
# Second Device
headers = {
    'Authorization' : 'Basic RdnEYkTENAkMOfMEn9Cr$KjZsWh0HXHpXShCxgsg',
    'Content-Type' : 'application/json'
    }

airTemp = 15
airTemp2 = 15.5
airHumid = 25
airHumid2 = 26
soilTemp = 12
soilHumid = 15
Co2 = 30
battery = 40

data = '{{"airTemp": {}, "airTemp2": {}, "airHumid": {}, "airHumid2": {}, "soilTemp": {}, "soilHumid": {}, "Co2": {}, "battery": {}}}'.format(
        airTemp, airTemp2, airHumid, airHumid2, soilTemp, soilHumid, Co2, battery)

response = urequests.post(url, headers=headers, data=data)

print(response.text)
response.close()

