import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

games = ["flappy_bird", "zomb_io"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="play")
async def play(ctx):
    embed = discord.Embed(title="Choose a Game", description="Select a game to play:")
    for game in games:
        embed.add_field(name=game, value=f"Type `!{game}` to play", inline=False)
    await ctx.send(embed=embed)

@bot.command(name="flappy_bird")
async def flappy_bird(ctx):
    await ctx.send(f"{ctx.author.mention}, get ready to flap your way through obstacles with your profile pic as the bird!")

    # Fetch and process user's profile picture
    profile_pic_url = ctx.author.avatar_url
    async with bot.http_session.get(profile_pic_url) as response:
        image_data = await response.read()
    profile_image = Image.open(io.BytesIO(image_data)).resize((50, 50))

    # Create a simple representation of the game
    game_image = Image.new("RGB", (800, 400), color="skyblue")
    draw = ImageDraw.Draw(game_image)
    game_image.paste(profile_image, (375, 175))

    # Save and send the image
    with io.BytesIO() as image_binary:
        game_image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="flappy.png"))

@bot.command(name="zomb_io")
async def zomb_io(ctx, mode="ai"):
    if mode == "online":
        await ctx.send(f"{ctx.author.mention}, finding an online match for you...")
        # Online matchmaking logic here
    else:
        await ctx.send(f"{ctx.author.mention}, preparing a battle with 99 bots!")

    # Fetch and process user's profile picture
    profile_pic_url = ctx.author.avatar_url
    async with bot.http_session.get(profile_pic_url) as response:
        image_data = await response.read()
    profile_image = Image.open(io.BytesIO(image_data)).resize((50, 50))

    # Create a simple representation of the game
    game_image = Image.new("RGB", (800, 400), color="darkgreen")
    draw = ImageDraw.Draw(game_image)
    for _ in range(99):
        bot_x, bot_y = random.randint(0, 750), random.randint(0, 350)
        draw.rectangle([bot_x, bot_y, bot_x + 50, bot_y + 50], fill="gray")
    game_image.paste(profile_image, (375, 175))

    # Save and send the image
    with io.BytesIO() as image_binary:
        game_image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="zomb_io.png"))

bot.run('YOUR_BOT_TOKEN')
