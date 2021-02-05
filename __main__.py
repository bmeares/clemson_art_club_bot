#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Launch the Clemson Art Club bot.
"""

def main(**kw):
    from .bot import start
    from meerschaum.utils.warnings import info
    info(f"Starting Discord bot...")
    return start()

if __name__ == "__main__":
    main()
