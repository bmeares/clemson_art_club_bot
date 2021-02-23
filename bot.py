#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from __future__ import annotations
from typing import Tuple, Optional, Dict, List, Union
from .config import get_club_config, get_token
from .trigger_actions import trigger_functions
from .pipes import artwork_pipe
from .client import get_client
import datetime, pytz
eastern = pytz.timezone('US/Eastern')

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
    d : Dict[str, List[Union[str, int, datetime.datetime]]] = {'user_id' : [], 'username' : [], 'url' : [], 'datetime' : [],}
    for a in attachments:
        d['user_id'].append(user.id)
        d['username'].append(user.name)
        d['url'].append(a.url)
        d['datetime'].append(datetime.datetime.now(eastern))
    if not artwork_pipe.columns:
        artwork_pipe.columns = {'datetime' : 'datetime', 'id' : 'user_id'}
    return artwork_pipe.sync(d, blocking=True)

def get_unique_submissions(
        user,
        now : Optional[datetime.datetime] = None,
        begin : Optional[datetime.datetime] = None,
        end : Optional[datetime.datetime] = None,
    ) -> int:
    now = now if now is not None else datetime.datetime.now(eastern)
    begin = begin if begin is not None else datetime.datetime(now.year, now.month, 1)
    end = end if end is not None else datetime.datetime(now.year, now.month + 1, 1)
    return artwork_pipe.get_rowcount(
        begin = begin,
        end = end,
        params = {'user_id' : user.id}
    )

def get_unique_days(
        user,
        now : Optional[datetime.datetime] = None,
        begin : Optional[datetime.datetime] = None,
        end : Optional[datetime.datetime] = None,
    ) -> int:
    now = now if now is not None else datetime.datetime.now(eastern)
    begin = begin if begin is not None else datetime.datetime(now.year, now.month, 1)
    end = end if end is not None else datetime.datetime(now.year, now.month + 1, 1)

    df = artwork_pipe.get_data(
        begin = begin,
        end = end,
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

