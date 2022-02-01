import requests
import json
from types import SimpleNamespace
import re

url="https://api.sbif.cl/api-sbifv3/recursos_api/uf?apikey=98684912805ba34555ac664ea057b90bb264d56d&formato=json"
data = requests.get(url)

x = json.loads(data.text, object_hook=lambda d:SimpleNamespace(**d))

valorUF = x.UFs[0].Valor
valorUF = re.sub('[\.]','',valorUF)
valorUF = valorUF[:5]
valorUF = int(valorUF)
print(valorUF*3) #podemos jugar con las sumas o multiplacación para saber ir dando otro resultado.
