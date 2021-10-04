import discord

from discord import message

from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event

async def on_ready():

    print('Bot is Online Now!')

@client.event

async def on_member_join(member):

    print(f'{member} has join a server.')

@client.event

async def on_member_remove(member):

    print(f'{member}has left a server.')

@client.command()

async def ping(ctx):

    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()

async def book(ctx):

    await ctx.send(f'Go to: https://discord.gg/Gg8sHj79Y8')

client.run('ODg2MjI5NjI2OTkxNTQ2NDUx.YTyjqA.gwjRfyoRHYXaH39fx8UL3bpLcaI')
