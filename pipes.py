#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Meerschaum Pipes used in this project.
"""

from .config import get_club_config
instance = get_club_config('mrsm_instance')

import meerschaum as mrsm
ck = 'clemson_art_club'

artwork_pipe = mrsm.Pipe(ck, 'artwork', mrsm_instance=instance)
leaderboard_pipe = mrsm.Pipe(ck, 'leaderboard', mrsm_instance=instance)
