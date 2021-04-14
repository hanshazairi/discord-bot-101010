import os

token = os.getenv('TOKEN')
guild = int(os.getenv('GUILD'))
casino = int(os.getenv('CASINO_CHANNEL'))
me = int(os.getenv('ME'))
mybot = int(os.getenv('MYBOT'))

help_text = (
  '```'
  '~help       - Shows available commands.\n'
  f'~gamble     - Wages money against <@{mybot}>.\n'
  '~give       - Gives money to user.\n'
  '~greet      - Sends greeting.\n'
  '~ichooseyou - Returns a pokémon.\n'
  '~joke       - Tells a joke.\n'
  '~roll       - Returns a random number.\n'
  '~stats      - Shows gamble stats.\n'
  '~wallet     - Returns wallet balance.\n'
  '```'
)