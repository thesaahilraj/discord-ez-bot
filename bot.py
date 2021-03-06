import asyncio
import discord
from discord.ext.commands import Bot
from discord import message
from discord.abc import Messageable
import os

client = Bot(command_prefix=">")

token = os.environ['token_keys']


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")


@client.command(pass_context=True)
async def clean(ctx, number):
    number = int(number)
    count = 0
    async for msg in Messageable.history(ctx.message.channel, limit=number):
        await message.Message.delete(msg)
        count = count+1
    await ctx.send("{} messages cleared!".format(count))

client.run(token)
