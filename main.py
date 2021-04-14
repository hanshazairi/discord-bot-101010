import discord
import constants as c
import functions as f
import utilities as u

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
  print(f'Discord {bot.user.name} Bot is live!')

@bot.event
async def on_member_join(member):
  if not member.bot:
    u.set_stats(member.id)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('~'):
    if message.content == '~help':
      await message.reply(c.help_text)

    elif message.content.startswith('~echo'):
      await f.echo_command(message)

    elif message.content.startswith('~gamble'):
      await f.gamble_command(message)

    elif message.content.startswith('~give'):
      await f.give_command(message)

    elif message.content == '~greet':
      await message.reply(f'Hello {message.author.name}!')

    elif message.content.startswith('~ichooseyou'):
      await f.ichooseyou_command(message)

    elif message.content == '~joke':
      await f.joke_command(message)

    elif message.content.startswith('~roll'):
      await f.roll_command(message)

    elif message.content == '~stats':
      await f.stats_command(message)

    elif message.content == '~wallet':
      await f.wallet_command(message)

    else:
      await message.reply('I do not recognise that command.')

@bot.event
async def on_message_delete(message):
  if message.author.id != c.me and message.author.id != c.mybot:
    await message.channel.send(f'{message.author.mention} deleted something. :eyes:')

u.keep_alive()
bot.run(c.token)