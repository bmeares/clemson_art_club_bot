#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from __future__ import annotations
from typing import Tuple
from .config import get_club_config, get_token
from .trigger_actions import trigger_functions
from .pipes import artwork_pipe
from .client import get_client
import datetime

def start():
    return get_client().run(get_token())

def get_name(user):
    try:
        name = user.nick 
    except:
        name = None

    if name is None:
        try:
            name = user.display_name
        except:
            name = None

    if name is None:
        name = "#".join(username.split('#')[:-1])

    return name

def register_artwork(user, attachments) -> Tuple[bool, str]:
    d = {'user_id' : [], 'username' : [], 'url' : [], 'datetime' : [],}
    for a in attachments:
        d['user_id'].append(user.id)
        d['username'].append(user.name)
        d['url'].append(a.url)
        d['datetime'].append(datetime.datetime.now())
    if not artwork_pipe.columns:
        artwork_pipe.columns = {'datetime' : 'datetime', 'id' : 'user_id'}
    return artwork_pipe.sync(d, blocking=True)

def get_monthly_submissions(user, now : Optional[datetime.datetime] = None):
    now = now if now is not None else datetime.datetime.now()
    this_month_begin = datetime.datetime(now.year, now.month, 1)
    next_month_begin = datetime.datetime(now.year, now.month + 1, 1)
    return artwork_pipe.get_rowcount(
        begin = this_month_begin,
        end = next_month_begin,
        params = {'user_id' : user.id}
    )

def get_monthly_days(user, now : Optional[datetime.datetime] = None):
    now = now if now is not None else datetime.datetime.now()
    this_month_begin = datetime.datetime(now.year, now.month, 1)
    next_month_begin = datetime.datetime(now.year, now.month + 1, 1)
    df = artwork_pipe.get_data(
        begin = this_month_begin,
        end = next_month_begin,
        params = {'user_id' : user.id}
    )
    seen_days = set()
    for i, row in df.iterrows():
        date_str = row['datetime'].date().strftime('%Y-%m-%d')
        if date_str not in seen_days:
            seen_days.add(date_str)
    return len(seen_days)

def update_roles(message):
    pass


if __name__ == "__main__":
    client.run(TOKEN)
