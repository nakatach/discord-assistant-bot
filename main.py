import nextcord
import asyncio
from nextcord.ext import commands
from url_shortener import shorten_link


intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name="h")
async def SendMessage(ctx):
    await ctx.send('1. Use <!shorten> <link> to shorten your url\n2. Use <!play> <title> to play music\n3. Use <!pause> to pause\n4 Use <!resume> to resume\n5. Use <!skip> to skip the current music\n6. Use <!q> to see the queue\n7. Use <!remove> <song index> to remove a music from the queue\n8. Use <!stop> to disconnect the bot from the voice channel')

@bot.command()
async def shorten(ctx, link: str):
    result = shorten_link(link)
    await ctx.send(result)

bot.load_extension('class_reminder')

bot.load_extension('music_player')

@bot.event
async def on_ready():
	print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
	bot.run("PASTE_YOUR_BOT_TOKEN_HERE")
