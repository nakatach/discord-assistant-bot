import nextcord
import asyncio
from nextcord.ext import commands
from url_shortener import shorten_link


intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def shorten(ctx, link: str):
    result = shorten_link(link)
    await ctx.send(result)

bot.load_extension('ytdw')

bot.load_extension('class_reminder')

@bot.event
async def on_ready():
	print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
	bot.run("PASTE YOUR BOT TOKEN HERE")
