from discord.ext import commands
import discord

class MyCog(commands.Cog):
    @commands.command()
    async def help(self, ctx):
        hid = 666317117154525185
        if ctx.message.content != '*help jsk':
            msgcont = ctx.message.content[5:len(ctx.message.content)]
            if msgcont.startswith(' '):
                msgcont = msgcont[1:len(msgcont)]
            if msgcont == '':
                msg = discord.Embed(title="Command List", color=eval(f"0x{ctx.bot.info['color']}"))
                msg.set_thumbnail(url=ctx.bot.info['avatar'])
                msg.set_footer(text=f'created by @{ctx.bot.get_user(hid)} <{hid}>', icon_url=ctx.bot.get_user(hid).avatar_url)
                msg.add_field(name='**'+ctx.bot.arrays['help']['help']['name']+'**',value='**'+ctx.bot.arrays['help']['help']['syntax']+'**',inline=False)
                for cmd in ctx.bot.arrays['help']:
                    cmd = ctx.bot.arrays['help'][f'{cmd}']
                    if cmd != ctx.bot.arrays['help']['help']:
                        msg.add_field(name=cmd['name'],value=cmd['desc'],inline=False)
                await ctx.message.channel.send(embed=msg)
            if msgcont != '':
                msgcont = msgcont.lower()
                for cmd in ctx.bot.arrays['help']:
                    cmd = ctx.bot.arrays['help'][f'{cmd}']
                    namealt = cmd['name'].replace('*','')
                    if msgcont.startswith(cmd['name']) or msgcont.startswith(namealt):
                        msg = discord.Embed(title=cmd['name'], color=eval(f"0x{ctx.bot.info['color']}"))
                        msg.set_thumbnail(url=ctx.bot.info['avatar'])
                        msg.set_footer(text=f'created by @{ctx.bot.get_user(hid)} <{hid}>', icon_url=ctx.bot.get_user(hid).avatar_url)
                        msg.add_field(name='Synatx',value=cmd['syntax'],inline=False)
                        msg.add_field(name='Description',value=cmd['desc'],inline=False)
                        msg.add_field(name='Who Can Run This Command?',value=cmd['perm'],inline=False)
                        await ctx.message.channel.send(embed=msg)
        if ctx.message.content == '*help jsk' and ctx.message.author.id == hid:
            await ctx.send("""```
The Jishaku debug and diagnostic commands.

This command on its own gives a status brief.
All other functionality is within its subcommands.

Commands:
  cancel     Cancels a task with the given index.
  cat        Read out a file, using syntax highlighting if detected.
  curl       Download and display a text file from the internet.
  debug      Run a command timing execution and catching exceptions.
  git        Shortcut for 'jsk sh git'. Invokes the system shell.
  hide       Hides Jishaku from the help command.
  in         Run a command as if it were run in a different channel.
  load       Loads or reloads the given extension names.
  py         Direct evaluation of Python code.
  py_inspect Evaluation of Python code with inspect information.
  repeat     Runs a command multiple times in a row.
  retain     Turn variable retention for REPL on or off.
  shell      Executes statements in the system shell.
  show       Shows Jishaku in the help command.
  shutdown   Logs this bot out.
  source     Displays the source code for a command.
  su         Run a command as someone else.
  sudo       Run a command bypassing all checks and cooldowns.
  tasks      Shows the currently running jishaku tasks.
  unload     Unloads the given extension names.
  voice      Voice-related commands.
```""")

def setup(bot):
    bot.add_cog(MyCog())
