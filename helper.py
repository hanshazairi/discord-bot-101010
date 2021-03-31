import constants as c
import helper_db as db
import helper_requests as r
import rng

def set_wallet(amount, user_ID):
  key = f'{user_ID}-wallet'
  db.put(amount, key)

def help_command():
  return ('Available commands:\n'
  '>>> `$help` - Shows available commands.\n'
  f'`$gamble` - Wages money against <@{c.mybot}>.\n'
  '`$give` - Gives money to user.\n'
  '`$greet` - Sends greeting.\n'
  '`$ichooseyou` - Returns a pokémon.\n'
  '`$joke` - Tells a joke.\n'
  '`$roll` - Returns a random number.\n'
  '`$wallet` - Returns wallet balance.')

def echo_command(message):
  try:
    text = message.content.split('$echo ', 1)[1]
      
  except Exception as e:
    print(f'ERROR: $echo: {e}')

    return 'Something went wrong..'

  else:
    return text

def gamble_command(message):
  if message.channel.id != int(c.casino):
    return f'No gambling here, you may gamble at <#{c.casino}>.'

  else:
    try:
      wager = int(message.content.split('$gamble ', 1)[1])

    except Exception as e:
      print(f'ERROR: $gamble: {e}')

      return '`$gamble [whole number > 0]`'

    else:
      wallet = 0
      w_key = f'{message.author.id}-wallet'

      if w_key in db.keys():
        wallet = db.get_value(w_key)

      if wager < 1:
        return '`$gamble [whole number > 0]`'

      elif wager > wallet:
        return f'Insufficient funds. You have ${wallet}.'

      else:
        chance = 'LLHW'
        chance = rng.get_opt(chance)

        if chance == 'L':
          wallet = wallet - wager
          text = f'You lost ${wager}.'

        elif chance == 'H':
          temp = int(wager / 2)
          wallet = wallet + temp
          text = f'You won ${temp}.'

        elif chance == 'W':
          wallet = wallet + wager
          text = f'You won ${wager}.'

        db.put(wallet, w_key)
        text = f'{text}. Current balance is ${wallet}.'

        return text

def give_command(message):
  try:
    donor = message.author
    recipient = message.mentions[0]
    amount = int(message.content.split(' ', 2)[2])

  except Exception as e:
    print(f'ERROR: $give: {e}')

    return '`$give [@user] [amount]`'

  else:
    if recipient != donor:
      r_key = f'{recipient.id}-wallet'
      d_key = f'{donor.id}-wallet'

      if r_key and d_key in db.keys():
        d_wallet = db.get_value(d_key)

        if d_wallet >= amount:
          r_wallet = db.get_value(r_key)
          db.put(r_wallet + amount, r_key)
          db.put(d_wallet - amount, d_key)

          return f'You gave {recipient.mention} ${amount}.'

        else:
          return f'Insufficient funds. You have ${d_wallet}.'
          
      else:
        raise Exception(f'ERROR: give_command({message})')

    else:
      return 'Do not waste my resources.'

def ichooseyou_command(message):
  try:
    pokemon = message.content.split('$ichooseyou ', 1)[1]
    
  except Exception as e:
    print(f'ERROR: $ichooseyou: {e}')

    return '`$ichooseyou [pokémon]`'

  else:
    try:
      data = r.get_JSON(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    except Exception as e:
      print(f'ERROR: $ichooseyou: {e}')

      return 'Something went wrong..'

    else:
      return data['sprites']['front_default']

def joke_command():
  try:
      data = r.get_JSON('https://official-joke-api.appspot.com/random_joke')

  except Exception as e:
    print(f'ERROR: $joke: {e}')

    return 'Something went wrong..'

  else:
    return f'{data["setup"]}\n\n{data["punchline"]}'

def roll_command(message):
  try:
    max = int(message.content.split('$roll ', 1)[1])

  except:
    max = 6

  finally:
    return rng.get_num(1, max)

def wallet_command(message):
  wallet = 0
  w_key = f'{message.author.id}-wallet'

  if w_key in db.keys():
    wallet = db.get_value(w_key)

  return f'Current balance is ${wallet}.'