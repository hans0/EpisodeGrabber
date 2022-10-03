import requests
import json

def get_ip():
  endpoint = 'https://ipinfo.io/json'
  response = requests.get(endpoint, verify = True)
  if response.status_code != 200:
    return 'Status: ', response.status_code, 'Problem with the request. Exiting'
  data = response.json()
  return data['ip']

def get_country(ip):
  endpoint = f'https://ipinfo.io/{ip}/json'
  response = requests.get(endpoint, verify = True)
  if response.status_code != 200:
    return 'Status: ', response.status_code, 'Problem with the request. Exiting'
  data = response.json()
  return data['country']

print(get_country(get_ip()))