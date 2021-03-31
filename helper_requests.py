import requests

def get_JSON(URL):
  r = requests.get(URL)

  if r.status_code == 200:
    return r.json()
  
  else:
    raise Exception(f'{r.status_code} ERROR: get_JSON({URL})')