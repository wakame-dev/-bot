import discord
from discord.ext import commands
import random
import config

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True  
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')
    await bot.tree.sync()
    guild_count = len(bot.guilds)
    activity = discord.Game(name=f"{guild_count} サーバーに参加しています")
    await bot.change_presence(activity=activity)

@bot.event
async def on_guild_join(guild):
    guild_count = len(bot.guilds)
    activity = discord.Game(name=f"{guild_count} サーバーに参加しています")
    await bot.change_presence(activity=activity)

@bot.event
async def on_guild_remove(guild):
    guild_count = len(bot.guilds)
    activity = discord.Game(name=f"{guild_count} サーバーに参加しています")
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    if message.author.bot:
        return  

    if '新八' in message.content:
        username = message.author.name
        await message.channel.send(f"なんだよ！{username}！何か用か！？")
        return

    if random.random() < 0.05:
        await message.channel.send("おいーーーー")
    
    await bot.process_commands(message)

@bot.command()
async def shinpati(ctx, *, text: str):
    formatted_text = f"「{text}」"
    await ctx.send(formatted_text)

@bot.tree.command(name="shinpati")
async def shinpati_slash(interaction: discord.Interaction, text: str):
    formatted_text = f"「{text}」"
    await interaction.response.send_message(formatted_text)

bot.run(config.TOKEN)
