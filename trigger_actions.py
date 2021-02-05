#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Define what to do when triggers are pulled.
"""

from __future__ import annotations
from typing import Optional, Dict, Any

from .config import get_club_config
from .pipes import artwork_pipe, leaderboard_pipe

async def _help(message):
    help_msg = (
        "Here's how you can interact with me!\n\n" +
        "**Commands:**\n"
    )
    for t, v in get_club_config('triggers').items():
        help_msg += f"`{v['tag']}`\n{v.get('description', 'No help available!')}\n\n"
    help_msg = help_msg[:-2]
    
    await message.channel.send(help_msg)

async def _leaderboard(message, begin : Optional[datetime.datetime] = None, end : Optional[datetime.datetime] = None):
    import datetime
    from meerschaum.utils.misc import sql_item_name
    tbl = sql_item_name(str(artwork_pipe), flavor=artwork_pipe.instance_connector.flavor)
    q = f"SELECT user_id, COUNT(username) AS count\nFROM {tbl}\n"
    q += "\nWHERE\n" if begin is not None or end is not None else ""
    q += f"datetime > '{begin}'\n" if begin is not None else ""
    q += "AND\n" if begin is not None and end is not None else ""
    q += f"datetime < '{end}'\n" if end is not None else ""
    q += "GROUP BY user_id ORDER BY COUNT(user_id) DESC"
    try:
        _df = artwork_pipe.instance_connector.read(q)
        user_id, count = int(_df.iloc[0]['user_id']), int(_df.iloc[0]['count'])
    except:
        leaderboard_msg = "Nothing on the leadboard yet! Try submitting some art."
        message.channel.send(leaderboard_msg)
        return

    from .bot import get_client, get_name

    msg = ""
    users = {}
    ranks = get_club_config('ranks')
    for i, r in _df.iterrows():
        user_id = int(r['user_id'])
        count = int(r['count'])
        if user_id not in users:
            users[user_id] = await get_client().fetch_user(user_id)
        msg += "**Artist:** " + users[user_id].mention + "\n"
        msg += f"**Submissions:** {count}\n"
        msg += f"**Rank:** {i + 1}" + ((" " + ranks[i]) if len(ranks) > i else "") + "\n"
        msg += "\n"
    msg = msg[:-2]
    await message.channel.send(msg)

trigger_functions = {
    'help' : _help,
    'leaderboard' : _leaderboard,
}
