import discord
from discord.ext import commands
import random
import json

bot = commands.Bot(command_prefix='*')
bot.remove_command('help')
hid = 666317117154525185
info=json.load(open('/app/info.json','r+'))
botinf=info['bot']

@bot.event
async def on_ready():
    global startlat
    await bot.change_presence(activity=discord.Game(name='on ❁| smol sunflowers |❁'), status=discord.Status('online'))
    tmplat = str(round(bot.latency*1000,0))
    startlat = f'{tmplat[0:len(tmplat)-2]}ms'

@bot.command()
async def ping(ctx):
    msg = discord.Embed(title="\U0001f3d3Pong",color=eval(f"0x{botinf['color']}"))
    msg.set_thumbnail(url=f"{botinf['avatar']}")
    msg.set_footer(text=f'created by @{bot.get_user(hid)} <{hid}>', icon_url=bot.get_user(hid).avatar_url)
    tmplat = str(round(bot.latency*1000,0))
    msg.add_field(name='Latency Now',value=f'\U0001f3d3{tmplat[0:len(tmplat)-2]}ms',inline=False)
    msg.add_field(name='Latency At Startup',value='\U0001f3d3'+startlat,inline=False)
    await ctx.message.channel.send(embed=msg)

bot.load_extension('infojson')
bot.load_extension('main')
bot.load_extension('actions')
bot.load_extension('jishaku')
bot.run('BOT_TOKEN')
