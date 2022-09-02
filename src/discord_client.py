import discord
import discord.voice_client
from discord.ext import commands

import os

import tts
import constants


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def hello_bot(ctx):
    await ctx.send(f"Hello, {ctx.author}")


@bot.command()
async def join_vc(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=constants.VOICE_CHANNEL)
    await voiceChannel.connect()


@bot.command()
async def leave_vc(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def say(ctx, arg):
    tts.create_tts_audio_file(arg)
    
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await voice.play(discord.FFmpegPCMAudio(executable=constants.FFMPEG_PATH, source=constants.AUDIO_FILE_PATH))
