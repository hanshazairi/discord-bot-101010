import random
import re

import constants as c
import utilities as u

def get_role_members(bot, role_id):
  guild = bot.get_guild(c.g_test)

  for role in guild.roles:
    if role.id == role_id:
      return role.members

def on_member_join(member):
  if member.guild.id == c.test_guild and not member.bot:
    u.put(0, f'{member.id}-wallet')
    u.put(0, f'{member.id}-stats-level')
    u.put(0, f'{member.id}-stats-xp')
    u.put(0, f'{member.id}-stats-earnings')
    u.put(0, f'{member.id}-stats-losses')

async def on_message_delete(message):
  if message.author.id != c.u_me and message.author.id != c.u_bot:
    await message.channel.send(f'{message.author.mention} deleted something. :eyes:')

async def echo_command(message):
  match = re.search(c.echo_regex, message.content)

  if match:
    text = match.group(1)

    if message.guild:
        await message.delete()

    await message.channel.send(text)

  else:
    await message.reply('`~echo [text]`')

async def gamble_command(message):
  if message.guild:
    if message.guild.id == c.g_test:
      if message.channel.id == c.c_casino:
        match = re.search(c.gamble_regex, message.content)

        if match:
          wager = int(match.group(1))
          w_key = f'{message.author.id}-wallet'
          lvl_key = f'{message.author.id}-stats-level'
          xp_key = f'{message.author.id}-stats-xp'
          e_key = f'{message.author.id}-stats-earnings'
          l_key = f'{message.author.id}-stats-losses'
          wallet = u.get_value(w_key)
          level = u.get_value(lvl_key)
          xp = u.get_value(xp_key)
          earnings = u.get_value(e_key)
          losses = u.get_value(l_key)

          if wager <= wallet:
            chance = 'LLHW'
            outcome = random.choice(chance)

            if outcome == 'H':
              wager = int(wager / 2)

            if outcome == 'L':
              wallet -= wager
              losses += wager
              text = f'You lost ${wager}.'

            else:
              wallet += wager
              xp += wager
              earnings += wager
              text = f'You won ${wager}.'

            while True:
              xp_to_next_lvl = 5 * level ** 2 + 50 * level + 100
              
              if xp >= xp_to_next_lvl:
                level += 1
                xp -= xp_to_next_lvl

              else:
                break

            u.put(wallet, w_key)
            u.put(level, lvl_key)
            u.put(xp, xp_key)
            u.put(earnings, e_key)
            u.put(losses, l_key)

            await message.reply(f'{text} Current balance is ${wallet}.')

          else:
            await message.reply(f'Insufficient funds. You have ${wallet}.')

        else:
          await message.reply('`~gamble [wager > 0]`')

      else:
        await message.reply(f'Strictly no gambling here. You may gamble at <#{c.c_casino}>.')

    else:
      await message.reply('Feature unavailable.')

  else:
    await message.reply('Feature unavailable.')

async def give_command(message):
  if message.guild:
    if message.guild.id == c.g_test:
      match = re.search(c.give_regex, message.content)

      if match:
        donor = message.author
        recipient = message.mentions[0]
        amount = int(match.group(1))

        if recipient.id != donor.id and not recipient.bot:
          r_key = f'{recipient.id}-wallet'
          d_key = f'{donor.id}-wallet'
          recipient_wallet = u.get_value(r_key)
          d_wallet = u.get_value(d_key)

          if d_wallet >= amount:
            u.put(recipient_wallet + amount, r_key)
            u.put(d_wallet - amount, d_key)

            await message.reply( f'You gave {recipient.mention} ${amount}.')

          else:
            await message.reply(f'Insufficient funds. You have ${d_wallet}.')

        else:
          await message.reply('Unable to fulfill request.')

      else:
        await message.reply('`~give [@user] [amount > 0]`')
      
    else:
      await message.reply('Feature unavailable.')

  else:
    await message.reply('Feature unavailable.')

async def ichooseyou_command(message):
  match = re.search(c.ichooseyou_regex, message.content)

  if match:
    pokemon = match.group(1)

    try:
      data = u.get_JSON(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    except Exception as e:
      print(f'ERROR: ~ichooseyou: {e}')

      await message.reply('Something went wrong..')

    else:
      await message.reply(data['sprites']['front_default'])

  else:
    await message.reply('`~ichooseyou [pokémon]`')

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
    max = int(message.content.split('~roll ', 1)[1])

  except:
    max = 6

  finally:
    await message.reply(random.randint(1, max))

async def stats_command(message):
  if message.guild:
    if message.guild.id == c.g_test:
      lvl_key = f'{message.author.id}-stats-level'
      xp_key = f'{message.author.id}-stats-xp'
      e_key = f'{message.author.id}-stats-earnings'
      l_key = f'{message.author.id}-stats-losses'
      level = u.get_value(lvl_key)
      xp = u.get_value(xp_key)
      earnings = u.get_value(e_key)
      losses = u.get_value(l_key)
      xp_to_next_lvl = 5 * level ** 2 + 50 * level + 100
      stats = (
        f'Level {level}\n'
        f'{xp}/{xp_to_next_lvl} XP\n'
        f'Earnings = ${earnings}\n'
        f'Losses = ${losses}'
      )

      await message.reply(stats)
      
    else:
      await message.reply('Feature unavailable.')

  else:
    await message.reply('Feature unavailable.')

async def wallet_command(message):
  if message.guild:
    if message.guild.id == c.g_test:
      key = f'{message.author.id}-wallet'
      wallet = u.get_value(key)
      
      await message.reply(f'Current balance is ${wallet}.')
      
    else:
      await message.reply('Feature unavailable.')

  else:
    await message.reply('Feature unavailable.')