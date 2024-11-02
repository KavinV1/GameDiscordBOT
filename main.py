import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Your existing commands and event handlers...

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="play")
async def play(ctx):
    embed = discord.Embed(title="Choose a Game", description="Select a game to play:")
    for game in ["flappy_bird", "zomb_io"]:
        embed.add_field(name=game, value=f"Type `!{game}` to play", inline=False)
    await ctx.send(embed=embed)

# Run the bot using the token from the .env file
bot.run(DISCORD_TOKEN)
