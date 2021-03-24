from replit import db

def get_keys():
  return db.keys()

def get_value_for_key(key):
  return db[key]

def put_value_for_key(key, value):
  db[key] = value