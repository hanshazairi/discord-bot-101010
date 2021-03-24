import h_db

def set_wallet(amount, id):
  key = f'{id}wallet'
  
  if key in h_db.get_keys():
    h_db.put_value_for_key(key, amount)

def give_money(donor, amount, recipient):
  if donor != recipient:
    d_key = f'{donor.id}wallet'
    r_key = f'{recipient.id}wallet'
    keys = h_db.get_keys()

    if d_key and r_key in keys:
      d_wallet = h_db.get_value_for_key(d_key)

      if d_wallet >= 50:
        r_wallet = h_db.get_value_for_key(r_key)
        h_db.put_value_for_key(d_key, d_wallet - 50)
        h_db.put_value_for_key(r_key, r_wallet + 50)

        return f'{donor.mention} gave you ${amount}.'

      else:
        return f'{donor.mention}, you have insufficient funds to give {recipient.name} ${amount}.'

    else:
      return f'Error occurred giving {recipient.name} ${amount}.'

  else:
    return f'Cannot give yourself ${amount}.'