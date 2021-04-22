import os

token = os.getenv('TOKEN')

g_test = 823173213663133698
c_casino = 824177726889000980
u_me = 160369095965933568
u_bot = 823438748553183323

echo_regex = '~echo (.+)'
gamble_regex = '~gamble ((?:[1-9]|\d\d\d*)$)'
give_regex = '~give <@![0-9]{18}> ((?:[1-9]|\d\d\d*)$)'
ichooseyou_regex = '~ichooseyou (.+)'

help_text = (
  '```fix\n'
  '~help       - Shows available commands.\n'
  '~echo       - Repeats what you say.\n'
  '~gamble     - Wager your money against me!\n'
  '~give       - Gives money to specifed user.\n'
  '~greet      - Greets you.\n'
  '~ichooseyou - Summons specified pokémon to the chat.\n'
  '~joke       - Tells a joke.\n'
  '~roll       - Returns a random number.\n'
  '~stats      - Shows your gamble stats.\n'
  '~wallet     - Shows your wallet balance.\n'
  '```'
)