import constants
import discord
import h
import h_message
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print(f'{client.user.name} Bot is live!')
  #h.set_wallet(200, int(constants.me))

@client.event
async def on_member_join(member):
  await member.channel.send(f'Welcome {member.author.mention}!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    if message.author.id == int(constants.me) and message.content.startswith('$echo '):
      await message.delete()
      await message.channel.send(h_message.echo(message))

    else:
      await message.reply(h_message.handle(message))

@client.event
async def on_message_delete(message):
  if message.author.id != int(constants.me):
    await message.channel.send(f'{message.author.mention} deleted something. :eyes:')

@client.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == '\U0001F4B0':
    await reaction.message.reply(h.give_money(user, 50, reaction.message.author))

def get_members(role, server):
  guild = client.get_guild(server)

  for temp in guild.roles:
    if temp.name == role:
      return temp.members

keep_alive()
client.run(constants.token)