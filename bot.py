import asyncio
import discord
from discord.ext.commands import Bot
from discord import message
from discord.abc import Messageable

client = Bot(command_prefix=">")

token = "ODA3Mjg4MDYwOTcwMDA4NjA3.YB1zmA.LcpG91t26SOI0_QtrJhAREekaEE"


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command()
async def hello(ctx):
    await ctx.send("Hello Gaandu!")


@client.command(pass_context=True)
async def clean(ctx, number):
    number = int(number)
    async for msg in Messageable.history(ctx.message.channel, limit=number):
        await message.Message.delete(msg)
    await ctx.send("{} messages cleared! Mat Karo bhai itna Cheating".format(number))

client.run(token)