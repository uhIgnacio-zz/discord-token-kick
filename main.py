import discord
from discord.ext import commands
bot = commands.Bot(".", intents=discord.Intents(guilds=True, messages=True), slash_commands=True)
token = "bot token here"

@bot.event
async def on_ready():
    print(f"{bot.user} (ID: {bot.user.id})")



@bot.command(message_command=False)
async def start(ctx: commands.Context):
    for member in ctx.guild.members: 
        if "skripted on top" or "ghurb" or "amogus scripted funny" or "Aced on top ong" or "motion" in member.name.lower(): 
            ctx.message.reply('banning tokens')
            await member.ban(reason='token')
            ctx.message.edit('tokens banned')

bot.run(token)