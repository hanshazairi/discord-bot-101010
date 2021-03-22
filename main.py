import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is live and logged in as {.user.name}!'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  channel = message.channel
  robbot = '<@679302710046097408>'
  me = 160369095965933568
  
  if message.author.id == me and message.content.startswith('$echo'):
      text = message.content.split('$echo ', 1)[1]
      await message.channel.send(text)
      await message.delete()

  if message.content.startswith('$help'):
    await channel.send("Commands available:\n"
    ">>> `$help` - Shows available commands.\n"
    "`$diss` - Shows `Rob Bot` who's boss.\n"
    "`$greet` - Sends greeting.\n"
    "`$hi` - Says hi to `Rob Bot`.\n"
    "`$teddy` - It's a secret."
    )

  if message.content.startswith('$diss'):
    await channel.send('%s is inferior to me! **Beep boop.**' % robbot)

  if message.content.startswith('$greet'):
    await channel.send('Hello {.author.mention}!'.format(message))

  if message.content.startswith('$hi'):
    await channel.send('Hi %s!' % robbot)

  if message.content.startswith('$teddy'):
    await channel.send("I love teddy! :teddy_bear:")

keep_alive()
client.run(os.getenv('TOKEN'))