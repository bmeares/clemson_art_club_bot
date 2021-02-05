#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os

import discord
from dotenv import load_dotenv
import meerschaum as mrsm

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send('memes')


if __name__ == "__main__":
    client.run(TOKEN)
