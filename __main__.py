#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Launch the Clemson Art Club bot.
"""

def main(**kw):
    from clemson_art_club_bot.bot import client, TOKEN
    client.run(TOKEN)

if __name__ == "__main__":
    main()
