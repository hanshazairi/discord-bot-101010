from replit import db

def keys():
  return db.keys()

def get_value(key):
  return db[key]

def put(value, key):
  db[key] = value