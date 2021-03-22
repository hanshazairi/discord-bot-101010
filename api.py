import requests

def get_data(type, optional = ""):
  if type == 'joke':
    URL = 'https://official-joke-api.appspot.com/random_joke'
  elif type == 'pokemon':
    URL = 'https://pokeapi.co/api/v2/pokemon/' + optional

  request = requests.get(URL)
  
  if request.status_code == 200:
    return request.json()

  return request.status_code