#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Custom Discord client
"""

from .config import get_club_config
from .trigger_actions import trigger_functions

import discord, datetime
class ClubClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        trigger = None
        for _trigger, attr in get_club_config('triggers').items():
            if message.content.startswith(attr['tag']):
                trigger = _trigger
                break
        if trigger in trigger_functions:
            await trigger_functions[trigger](message)

        if trigger is None and message.content is not None and message.content.startswith(get_club_config('triggers', 'leader')):
            await trigger_functions['unknown'](message)

        if message.attachments and message.channel.name == get_club_config('upload_channel'):
            from meerschaum.utils.formatting import print_tuple
            from .bot import register_artwork, get_monthly_submissions, get_monthly_days
            now = datetime.datetime.now()
            next_month_begin = datetime.datetime(now.year, now.month + 1, 1)

            success, msg = register_artwork(message.author, message.attachments)
            print_tuple((success, msg))

            days_uploaded = get_monthly_days(message.author, now=now)
            monthly_submissions = get_monthly_submissions(message.author, now=now)
            days_remaining = (next_month_begin - now).days

            upload_message = get_club_config('upload_message')
            msg = eval(f'f"""{upload_message}"""')
            await message.channel.send(msg)

_client = None
_loop = None
def get_client():
    import asyncio
    global _client, _loop
    if _loop is None or _loop.is_closed():
        _loop = asyncio.new_event_loop()
        _client = ClubClient(loop=_loop)
    return _client

