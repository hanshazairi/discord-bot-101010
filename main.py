import discord
import os
from replit import db
from message_helper import handle_message
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

test_server = 823173213663133698
me = 160369095965933568

@client.event
async def on_ready():
  print(f'{client.user.name} Bot is live!')
  #set_mods_wallet(200)

@client.event
async def on_member_join(member):
  channel = member.channel
  await channel.send(f'Welcome {member.author.mention}!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    if message.author.id == me and message.content.startswith('$echo '):
      await message.delete()
      await message.channel.send(handle_message(message))

    else:
      await message.reply(handle_message(message))

@client.event
async def on_message_delete(message):
  if message.author.id != me:
    await message.channel.send(f'<@{message.author.id}> deleted something. :eyes:')

def set_mods_wallet(balance):
  guild = client.get_guild(test_server)
  for role in guild.roles:
    if role.name == 'Mods':
      for member in role.members:
        key = str(member.id) + 'wallet'
        db[key] = balance

keep_alive()
client.run(os.getenv('TOKEN'))