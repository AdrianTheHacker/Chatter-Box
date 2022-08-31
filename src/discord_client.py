from venv import create
import discord
from discord.ext import commands

import tts


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello_bot(ctx):
    await ctx.send(f"Hello, {ctx.author}")

@bot.command()
async def say(ctx, arg):
    await ctx.send(f"Sure, {ctx.author}")
    await tts.create_tts_audio_file(arg)
