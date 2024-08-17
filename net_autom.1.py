#version 1 de net_autom_test


import requests
import ssl


ip = input("enter ip address: ").strip()
url = "https://ipapi.co/"+ip.strip()+"/json"

context = ssl.create_default_context()
response = requests.get(url = url, cert = None, verify = None).text
print("usted esta consultando la ip: "+ip)
print(response)