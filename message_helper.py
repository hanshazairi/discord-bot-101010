import os
from replit import db
from api import get_data
from rng import get_random_choice
from rng import get_random_num

me = os.getenv('ME')
mybot = os.getenv('MYBOT')
casino = os.getenv('CASINO')

def handle_message(message):
  if message.content.startswith('$help'):
    return help(message)

  elif message.content.startswith('$diss'):
    return 'I am a polite Bot.'

  elif message.content.startswith('$echo'):
    return echo(message)

  elif message.content.startswith('$gamble'):
    return gamble(message)
  
  elif message.content.startswith('$greet'):
    return f'Hello {message.author.name}!'

  elif message.content.startswith('$ichooseyou'):
    return ichooseyou(message)

  elif message.content.startswith('$joke'):
    return joke(message)

  elif message.content.startswith('$roll'):
    return roll(message)
  
  elif message.content.startswith('$teddy'):
    return 'I love teddy! :teddy_bear:'

  elif message.content.startswith('$wallet'):
    return wallet(message)
  
  else:
    return 'I don\'t recognise that command.'

def help(message):
  if message.content.startswith('$help'):
    return ('Available commands:\n'
    '>>> `$help` - Shows available commands.\n'
    '`$diss` - Throws random diss.\n'
    f'`$gamble` - Wages money against <@{mybot}>.\n'
    '`$greet` - Sends greeting.\n'
    '`$ichooseyou` - Returns pokémon.\n'
    '`$joke` - Tells a joke.\n'
    '`$roll` - Returns random number.\n'
    '`$teddy` - It\'s a secret.\n'
    '`$wallet` - Returns wallet balance.')

def echo(message):
  try:
    text = message.content.split('$echo ', 1)[1]
      
  except Exception as err:
    print(f'$echo: {err}')
    return '`$echo [text]`'

  else:
    if message.author.id == me:
      return text

    else:
      return 'I only listen to master Hans.'

def gamble(message):
  if message.channel.id != casino:
    return f'No gambling here, you may gamble at <#{casino}>.'
  else:
    try:
      wager = int(message.content.split('$gamble ', 1)[1])

    except Exception as err:
      print(f'$gamble: {err}')
      return '`$gamble [natural number]`'

    else:
      wallet = 0
      walletID = str(message.author.id) + 'wallet'

      if walletID in db.keys():
        wallet = int(db[walletID])

      if wager < 1:
        return '`$gamble [wager >= 1]`'

      elif wager > wallet:
        return f'Insufficient funds. Current balance is ${wallet}.'

      else:
        chance = 'LLHW'
        choice = get_random_choice(chance)

        if choice == 'L':
          wallet = wallet - wager
          text = f'You lost ${wager}.'

        elif choice == 'H':
          temp = int(wager / 2)
          wallet = wallet + temp
          text = f'You won ${temp}.'

        elif choice == 'W':
          wallet = wallet + wager
          text = f'You won ${wager}.'

        db[walletID] = wallet
        text = text + f' Current balance is ${wallet}.'

        return text

def ichooseyou(message):
  try:
    pokemon = message.content.split('$ichooseyou ', 1)[1]
    
  except Exception as err:
    print(f'$ichooseyou: {err}')
    return '`$ichooseyou [pokémon]`'

  else:
    data = get_data('pokemon', pokemon)

    if isinstance(data, dict):
      sprite = data['sprites']['front_default']
      return sprite

    else:
      return f'`$ichooseyou: {data} error`'

def joke(message):
  data = get_data('joke')

  if isinstance(data, dict):
    text = data['setup'] + '\n' + data['punchline']
    return text

  else:
    return f'`$joke: {data} error`'

def roll(message):
  try:
    num = int(message.content.split('$roll ', 1)[1])

  except:
    num = 6

  finally:
    return get_random_num(num)

def wallet(message):
  wallet = 0
  walletID = str(message.author.id) + 'wallet'

  if walletID in db.keys():
    wallet = int(db[walletID])

  return f'Current balance is ${wallet}.'