import constants as c
import utilities as u

def set_stats(user_ID):
  u.put(0, f'{user_ID}-stats-level')
  u.put(0, f'{user_ID}-stats-xp')
  u.put(0, f'{user_ID}-stats-earnings')
  u.put(0, f'{user_ID}-stats-losses')

async def echo_command(message):
  try:
    text = message.content.split('~echo ', 1)[1]
      
  except Exception as e:
    print(f'ERROR: ~echo: {e}')

    await message.reply('Something went wrong..')

  else:
    if message.author.id == int(c.me):
      await message.delete()
      await message.channel.send(text)

    else:
      await message.reply('I will not do that.')

async def gamble_command(message):
  if message.channel.id != c.casino:
    await message.reply(f'No gambling here, you may gamble at <#{c.casino}>.')

  else:
    try:
      wager = int(message.content.split('~gamble ', 1)[1])

    except Exception as e:
      print(f'ERROR: ~gamble: {e}')

      await message.reply('`~gamble [whole number > 0]`')

    else:
      wallet_key = f'{message.author.id}-wallet'
      lvl_key = f'{message.author.id}-stats-level'
      xp_key = f'{message.author.id}-stats-xp'
      earnings_key = f'{message.author.id}-stats-earnings'
      losses_key = f'{message.author.id}-stats-losses'

      try:
        wallet = u.get_value(wallet_key)
        level = u.get_value(lvl_key)
        xp = u.get_value(xp_key)
        earnings = u.get_value(earnings_key)
        losses = u.get_value(losses_key)

      except Exception as e:
        print(f'ERROR: ~gamble: {e}')

        await message.reply('Something went wrong..')

      else:
        if wager < 1:
          await message.reply('`~gamble [whole number > 0]`')

        elif wager > wallet:
          await message.reply(f'Insufficient funds. You have ${wallet}.')

        else:
          chance = 'LLHW'
          draw = u.draw_one(chance)

          if draw == 'L':
            text = f'You lost ${wager}.'
            losses += wager
            wager = -wager

          elif draw == 'H':
            wager = int(wager / 2)
            xp += wager
            earnings += wager
            text = f'You won ${wager}.'

          elif draw == 'W':
            xp += wager
            earnings += wager
            text = f'You won ${wager}.'

          while True:
            xp_to_next_level = 5 * level ** 2 + 50 * level + 100
            
            if xp >= xp_to_next_level:
              level += 1
              xp -= xp_to_next_level

            else:
              break

          wallet += wager
          u.put(wallet, wallet_key)
          u.put(level, lvl_key)
          u.put(xp, xp_key)
          u.put(earnings, earnings_key)
          u.put(losses, losses_key)

          await message.reply(f'{text} Current balance is ${wallet}.')

async def give_command(message):
  try:
    donor = message.author
    recipient = message.mentions[0]
    amount = int(message.content.split(' ', 2)[2])

  except Exception as e:
    print(f'ERROR: ~give: {e}')

    await message.reply('`~give [@user] [amount]`')

  else:
    if recipient.id != donor.id:
      recipient_key = f'{recipient.id}-wallet'
      donor_key = f'{donor.id}-wallet'

      try:
        recipient_walet = u.get_value(recipient_key)
        donor_wallet = u.get_value(donor_key)

      except Exception as e:
        print(f'ERROR: ~give: {e}')

        await message.reply('Something weng wrong..')

      else:
        if donor_wallet >= amount:
          
          u.put(recipient_walet + amount, recipient_key)
          u.put(donor_wallet - amount, donor_key)

          await message.reply( f'You gave {recipient.mention} ${amount}.')

        else:
          await message.reply(f'Insufficient funds. You have ${donor_wallet}.')

    else:
      await message.reply('I will not do that.')

async def ichooseyou_command(message):
  try:
    pokemon = message.content.split('~ichooseyou ', 1)[1]
    
  except Exception as e:
    print(f'ERROR: ~ichooseyou: {e}')

    await message.reply('`~ichooseyou [pokémon]`')

  else:
    try:
      data = u.get_JSON(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    except Exception as e:
      print(f'ERROR: ~ichooseyou: {e}')

      await message.reply('Something went wrong..')

    else:
      await message.reply(data['sprites']['front_default'])

async def joke_command(message):
  try:
      data = u.get_JSON('https://official-joke-api.appspot.com/random_joke')

  except Exception as e:
    print(f'ERROR: ~joke: {e}')

    await message.reply('Something went wrong..')

  else:
    await message.reply(f'{data["setup"]}\n\n{data["punchline"]}')

async def roll_command(message):
  try:
    max = int(message.content.split('$roll ', 1)[1])

  except:
    max = 6

  finally:
    await message.reply(u.get_random_num(1, max))

async def stats_command(message):
  s_key = f'{message.author.id}-stats'
  lvl_key = f'{s_key}-level'
  xp_key = f'{s_key}-xp'
  e_key = f'{s_key}-earnings'
  l_key = f'{s_key}-losses'

  try:
    level = u.get_value(lvl_key)
    xp = u.get_value(xp_key)
    earnings = u.get_value(e_key)
    losses = u.get_value(l_key)

  except Exception as e:
    print(f'ERROR: ~stats: {e}')

    await message.reply('Something went wrong..')

  else:
    xp_to_next_level = 5 * level ** 2 + 50 * level + 100
    stats = (
      f'Level {level}\n'
      f'{xp}/{xp_to_next_level} XP\n'
      f'Earnings = ${earnings}\n'
      f'Losses = ${losses}\n'
    )

    await message.reply(stats)

async def wallet_command(message):
  wallet_key = f'{message.author.id}-wallet'

  try:
    wallet = u.get_value(wallet_key)

  except Exception as e:
    print(f'ERROR: ~wallet: {e}')

    await message.reply('Something went wrong..')

  else:
    await message.reply(f'Current balance is ${wallet}.')