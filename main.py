import nextcord
import asyncio
from nextcord.ext import commands
from url_shortener import shorten_link


# Create a bot instance
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Command to shorten URL
@bot.command()
async def shorten(ctx, link: str):
    result = shorten_link(link)
    await ctx.send(result)

# Command to download yt vids
bot.load_extension('ytdw')

# Command to load class reminder
bot.load_extension('class_reminder')

# Run the bot
@bot.event
async def on_ready():
	print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
	bot.run("MTI2MzAyNzQzNDM3OTU0MjU4MA.GLAnOy._tzRAZxYoWV1WphNFMs8a4YKN1rhpGYpCNj0wA")
