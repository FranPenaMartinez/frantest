"""Domains Categorization using Investigate API"""
#linea1
#linea2
#linea3
#cambio linea 5
#cambio linea 6

Dom = input('Consulta Dominio: ')

import requests
#url = "https://investigate.api.umbrella.com/domains/categorization/cisco.com"
url = "https://investigate.api.umbrella.com/domains/categorization/"
url = url+Dom
querystring = {"showLabels":""}
headers = {
    "authorization": "Bearer 47438669-9676-4ced-b3a3-c1ff51f929c4",
    'cache-control': "no-cache",
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
