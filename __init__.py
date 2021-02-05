#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

__version__ = '0.0.2'

required = [
    'discord.py',
    'pandas',
]

from meerschaum.actions import make_action

@make_action
def art_club_bot(**kw):
    """
    Start the Clemson Art Club Discord bot.
    """
    from .__main__ import main
    return main(**kw)
