from discord.ext import commands
import discord
import random

class actions(commands.Cog):
    @commands.command()
    async def hug(self, ctx):
        if len(ctx.message.mentions) == 0:
            embed = discord.Embed(title="♥hug♥", color=eval(f"0x{ctx.bot.info['color']}"))
            embed.set_image(url=random.choice(ctx.bot.arrays['hug']['gif']))
            await ctx.message.channel.send(embed=embed)
        if len(ctx.message.mentions) >= 1:
            sender = ctx.message.author.mention
            usr = ctx.message.mentions[0].mention
            desc = random.choice(ctx.bot.arrays['hug']['msg'])
            desc = desc.replace('$user', usr)
            desc = desc.replace('$sender', sender)
            embed = discord.Embed(title="♥hug♥", description=desc, color=eval(f"0x{ctx.bot.info['color']}"))
            embed.set_image(url=random.choice(ctx.bot.arrays['hug']['gif']))
            await ctx.message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(actions())
