from flask import Flask
from replit import db
from threading import Thread
import random
import requests

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
  try:
    del db[key]
  
  except Exception as e:
    print(f'ERROR: del_value({key}): {e}')

def put(value, key):
  db[key] = value

def draw_one(chance):
  return random.choice(chance)

def get_random_num(min, max):
  return random.randint(min, max)

def get_JSON(URL):
  r = requests.get(URL)

  if r.status_code == 200:
    return r.json()
  
  else:
    raise Exception(f'{r.status_code} ERROR: get_JSON({URL})')