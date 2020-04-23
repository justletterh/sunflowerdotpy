import json
def setup(bot):
  with open('/app/info.json', 'r+') as f:
    bot.arrays = json.load(f)
    bot.info = bot.arrays['bot']
