# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    if(r.status_code == 200):
        data = r.json()
        descripcion = data['value']
        with open('joker.txt', 'w') as dataFile:
            json.dump(descripcion, dataFile, indent=4)
        dataFile.close()
        return 1
    else:
        return 0
