import discord
import os
from api import get_data
from rng import get_random_num
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is live and logged in as {.user.name}!'.format(client))

@client.event
async def on_member_join(member):
  channel = member.channel
  await channel.send('Welcome %s!' % member.author.mention)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  channel = message.channel
  me = 160369095965933568
  robbot = 679302710046097408
  teddybot = 823481842392367144
  
  if message.author.id == me and message.content.startswith('$echo'):
    try:
      text = message.content.split('$echo ', 1)[1]
      await channel.send(text)
      #await message.delete()
    except:
      print('$echo: An error occured.')

  if message.content.startswith('$help'):
    await message.reply("Available commands:\n"
    ">>> `$help` - Shows available commands.\n"
    "`$diss` - Shows `Rob Bot the Cat` who's boss.\n"
    "`$greet` - Sends greeting.\n"
    "`$hirob` - Says hi to `Rob Bot the Cat`.\n"
    "`$hiteddy` - Says hi to `Teddy ʕ•ᴥ•ʔ`.\n"
    "`$joke` - Tells a joke.\n"
    "`$poke [pokémon]` - Returns pokémon sprite.\n"
    "`$rng [num]` - Returns random number in the inclusive range [1, num].\n"
    "`$teddy` - It's a secret."
    )

  if message.content.startswith('$diss'):
    await channel.send('<@%s> is inferior to me! **Beep boop.**' % robbot)

  if message.content.startswith('$greet'):
    await message.reply('Hello {.author.mention}!'.format(message))

  if message.content.startswith('$hirob'):
    await channel.send('Hi <@%s>!' % robbot)

  if message.content.startswith('$hiteddy'):
    await channel.send('Hi <@%s>!' % teddybot)

  if message.content.startswith('$joke'):
    data = get_data('joke')

    if isinstance(data, dict):
      text = data['setup'] + '\n' + data['punchline']
      await message.reply(text)
    else:
      await message.reply('`$joke: %i Error' % data)

  if message.content.startswith('$poke'):
    try:
      pokemon = message.content.split('$poke ', 1)[1]
      data = get_data('pokemon', pokemon)

      if isinstance(data, dict):
        sprite = data['sprites']['front_default']
        await message.reply(sprite)
      else:
        await message.reply('`$poke: %i Error`' % data)
    except:
      print('$poke: An error occurred.')
      await channel.send ('`$poke [pokémon]`')

  if message.content.startswith('$rng'):
    try:
      num = int(message.content.split('$rng ', 1)[1])
      num = get_random_num(num)
      await message.reply('%i' % num)
    except:
      await message.reply('`$rng [base-10 num > 1]`')

  if message.content.startswith('$teddy'):
    await message.reply("I love teddy! :teddy_bear:")

keep_alive()
client.run(os.getenv('TOKEN'))