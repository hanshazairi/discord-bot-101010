from threading import Thread

from flask import Flask
import requests

from replit import db

app = Flask('')

@app.route('/')
def home():
  return 'Discord 101010 Bot is live!'

def run():
  app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()

def keys():
  return db.keys()

def get_value(key):
  return db[key]
  
def del_value(key):
  del db[key]

def put(value, key):
  db[key] = value

def print_keys():
  for index, key in enumerate(keys()):
    print(f'{index + 1}: {key}: {get_value(key)}')

def get_JSON(URL):
  r = requests.get(URL)

  if r.status_code == 200:
    return r.json()
  
  else:
    raise Exception(f'{r.status_code} ERROR: get_JSON({URL})')