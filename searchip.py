import json
import requests
from colorama import Fore, Back, Style
from time import sleep
from os import system

lol = '[*]'
fields = ["status","continent","continentCode","country","countryCode","region","regionName","city","district","zip","lat","lon","timezone","currency","isp","org","as","asname","reverse","mobile","proxy","hosting","query"]

ip = input(Fore.GREEN+"Digite um ip: ")
try:
    req = requests.get(f"http://ip-api.com/json/{ip}?fields=status,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
    print(req.status_code)
    if req.status_code == 200:
        print(f"[*] STATUS CODE: {req.status_code}")
        js = json.loads(req.text) 
        
        ip = js["query"]
        status = js["status"]
        continent = js["continent"]
        pais = js["country"]
        regiao = js["region"]
        cidade = js["city"]
        distrito = js["district"]
        zipe = js["zip"]
        latitude = js["lat"]
        longuitude = js["lon"]
        fuso_horario = js["timezone"]
        isp = js["isp"]
        org = js["org"]
        celular = js["mobile"]
        proxy = js["proxy"]   
        
        print(Fore.GREEN + '-'*30)
        print(f"{lol} IP: {ip}\n{lol} Status: {status}\n{lol} Pais: {pais}\n{lol} Região: {regiao}\n{lol} Cidade: {cidade}\n{lol} Distrito: {distrito}\n{lol} ZIP: {zipe}\n{lol} Latitude: {latitude}\n{lol} Longuitude: {longuitude}\n{lol} Presença de Proxy: {proxy}")
    else:
        print(f"[*] STATUS CODE: {req.status_code}")

except Exception as error:
    print(f"ERROR BY {error}")