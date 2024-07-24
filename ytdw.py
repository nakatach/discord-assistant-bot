import nextcord
from nextcord.ext import commands
import yt_dlp as youtube_dl
import os
from pathlib import Path

class YTDownloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ytdw', help='Download a YouTube video to your laptop. Usage: !ytdw <youtube_url>')
    async def download_to_laptop(self, ctx, url: str):
        await ctx.send(f"Fetching video information for {url}")
        try:
            # Define the path to cookies file (if needed)
            cookies_file = 'www.youtube.com_cookies.txt'

            # Create yt_dlp options to get information about the video
            ydl_opts = {
                'format': 'bestaudio/best',  # Get the best available audio format
                'noplaylist': True,
                'quiet': True,
                'cookiefile': cookies_file,  # Specify the path to cookies
                'progress_hooks': [self.progress_hook],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            # List available resolutions
            formats = info.get('formats', [])
            resolutions = [f['height'] for f in formats if 'height' in f and f['height'] is not None]
            resolutions = list(set(resolutions))  # Remove duplicates
            resolutions.sort(reverse=True)  # Sort resolutions in descending order

            # Display available resolutions
            resolution_message = "Available resolutions:\n"
            for res in resolutions:
                resolution_message += f"{res}p\n"
            await ctx.send(resolution_message)
            
            # Ask for resolution
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            await ctx.send("Please enter the desired resolution (e.g., 720):")
            msg = await self.bot.wait_for("message", check=check)
            selected_resolution = int(msg.content.strip())

            if selected_resolution not in resolutions:
                await ctx.send("Invalid resolution selected. Downloading the highest resolution available.")
                selected_resolution = resolutions[0]

            # Define download path for laptop
            download_folder = str('C:/Users/MyBook Hype AMD/Downloads')
            await ctx.send(f"Saving video to {download_folder}")

            # Download the video
            ydl_opts = {
                'format': f'best[height<={selected_resolution}]',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'cookiefile': cookies_file,  # Specify the path to cookies
                'progress_hooks': [self.progress_hook],
                'merge_output_format': None,  # Avoid merging formats
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            await ctx.send(f"Video downloaded successfully to {download_folder}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    def progress_hook(self, d):
        if d['status'] == 'finished':
            print(f"\nDone downloading video: {d['filename']}")

def setup(bot):
    bot.add_cog(YTDownloader(bot))
