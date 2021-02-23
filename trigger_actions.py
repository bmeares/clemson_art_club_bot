#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Define what to do when triggers are pulled.
"""

from __future__ import annotations
from typing import Optional, Dict, Any, List

from .config import get_club_config
from .pipes import artwork_pipe, leaderboard_pipe

import datetime, pytz
eastern = pytz.timezone('US/Eastern')

async def _unknown(message):
    header = f"Sorry, I don't know what '{message.content}' means. Here are some commands I know:"
    await _help(message, header)

async def _help(message, header : Optional[str] = None):
    if header is None:
        header = "Here's how you can interact with me!"
    help_msg = (
        header + "\n\n" +
        "**Commands:**\n"
    )
    for t, v in get_club_config('triggers').items():
        help_msg += f"`{v['tag']}`\n{v.get('description', 'No help available!')}\n\n"
    help_msg = help_msg[:-2]
    
    await message.channel.send(help_msg)

async def _leaderboard(
        message,
        begin : Optional[datetime.datetime] = None,
        end : Optional[datetime.datetime] = None
    ):
    from .bot import get_unique_submissions, get_unique_days 
    from dateutil import relativedelta
    import pandas as pd
    from .bot import get_client, get_name
    now = datetime.datetime.now(eastern)
    begin = begin if begin is not None else datetime.datetime(now.year, now.month, 1)
    end = end if end is not None else datetime.datetime(now.year, now.month, 1) + relativedelta.relativedelta(months=1)

    try:
        user_ids = list(set(artwork_pipe.get_data(begin=begin, end=end)['user_id']))
    except:
        user_ids = []
    users = {}
    lb : Dict[str, List[int]] = {'user_id' : [], 'submissions' : [], 'days' : []}
    for user_id in user_ids:
        lb['user_id'].append(user_id)
        if user_id not in users:
            users[user_id] = await get_client().fetch_user(user_id)

        lb['submissions'].append(get_unique_submissions(users[user_id], begin=begin, end=end))
        lb['days'].append(get_unique_days(users[user_id], begin=begin, end=end))

    _df = pd.DataFrame(lb).sort_values(by=['days', 'submissions'], ascending=False)

    msg = f"Leaderboard from {begin.date().strftime('%B %-d')} to {end.date().strftime('%B %-d')}:\n\n"
    ranks = get_club_config('ranks')
    for i, r in _df.iterrows():
        user_id = int(r['user_id'])
        days = int(r['days'])
        submissions = int(r['submissions'])
        if user_id not in users:
            users[user_id] = await get_client().fetch_user(user_id)
        msg += "**Artist:** " + users[user_id].mention + "\n"
        msg += f"**Days Submitted:** {days}\n"
        msg += f"**Submissions:** {submissions}\n"
        msg += f"**Rank:** {i + 1}" + ((" " + ranks[i]) if len(ranks) > i else "") + "\n"
        msg += "\n"
    msg = msg[:-2]
    await message.channel.send(msg)

trigger_functions = {
    'help' : _help,
    'leaderboard' : _leaderboard,
}
