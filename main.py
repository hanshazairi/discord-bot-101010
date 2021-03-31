from keep_alive import keep_alive
import discord
import constants as c
import helper as h

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
  print(f'Discord {bot.user.name} Bot is live!')
#  members = get_members(c.test_server, '@everyone')
  
#  for member in members:
#    h.set_wallet(200, member.id)

@bot.event
async def on_member_join(member):
  await member.channel.send(f'Welcome {member.author.mention}!')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('$'):
    if message.content == '$help':
      await message.reply(h.help_command())

    elif message.content.startswith('$echo'):
      if message.author.id == int(c.me):
        await message.delete()
        await message.channel.send(h.echo_command(message))

      else:
        await message.reply('I will not do that.')

    elif message.content.startswith('$gamble'):
      await message.reply(h.gamble_command(message))

    elif message.content.startswith('$give'):
      await message.reply(h.give_command(message))

    elif message.content == '$greet':
      await message.reply(f'Hello {message.author.name}!')

    elif message.content.startswith('$ichooseyou'):
      await message.reply(h.ichooseyou_command(message))

    elif message.content == '$joke':
      await message.reply(h.joke_command())

    elif message.content.startswith('$roll'):
      await message.reply(h.roll_command(message))

    elif message.content == '$wallet':
      await message.reply(h.wallet_command(message))

    else:
      await message.reply('I don\'t recognise that command.')

@bot.event
async def on_message_delete(message):
  if message.author.id != int(c.me):
    await message.channel.send(f'{message.author.mention} deleted something. :eyes:')

def get_members(server_ID, role):
  guild = bot.get_guild(int(server_ID))

  for _role in guild.roles:
    if _role.name == role:
      return _role.members

keep_alive()
bot.run(c.token)