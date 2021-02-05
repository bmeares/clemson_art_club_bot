#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Access the bot's configuration.
"""

from __future__ import annotations
from typing import Dict, Any

def get_club_config(*keys) -> Dict[str, Any]:
    from meerschaum.config import get_config
    valid_root, root = get_config('plugins', 'clemson_art_club_bot', as_tuple=True, warn=False)
    if not valid_root:
        root = {}
    valid, values = get_config('plugins', 'clemson_art_club_bot', *keys, as_tuple=True, warn=False)
    if not valid:
        from .defaults import defaults
        for k, v in defaults.items():
            if k not in root:
                root[k] = v
        write_club_config(root)
        valid, values = get_config('plugins', 'clemson_art_club_bot', *keys, as_tuple=True, warn=False)
        if not valid:
            return None
    return values

def write_club_config(d : Dict[str, Any]) -> bool:
    from meerschaum.config._edit import write_config
    from meerschaum.config import get_config
    plugins_config = get_config('plugins')
    plugins_config['clemson_art_club_bot'] = d
    try:
        write_config({'plugins' : plugins_config})
        success = True
    except:
        success = False
    return success

def get_token():
    token = get_club_config('token')
    if token is None:
        from meerschaum.utils.warnings import info
        from meerschaum.utils.prompt import prompt
        from .defaults import defaults
        info(
            f"I couldn't find the Discord application token.\n\n" +
            f"Please visit https://discord.com/developers/applications and create a new token " +
            f"for the bot to use.\n\n" +
            f"To edit this token later, run the command `edit config plugins` from Meerschaum.\n"
        )
        token = prompt(f"Please enter Discord application token:", is_password=True)
        _club_config = {'token' : token}
        for k, v in defaults.items():
            if k not in get_club_config():
                _club_config[k] = v
        if not write_club_config(_club_config):
            print(f"Failed to write Clemson Art Club configuration!")
    return token


