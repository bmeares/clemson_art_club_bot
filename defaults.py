#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
The default values for this bot.
"""

defaults = {
    'upload_channel' : 'eternal-suffering',
    'upload_message' : '🎉 Your submission has been accepted! You have uploaded {monthly_submissions} submissions over {days_uploaded} days, with {days_remaining} days left in the month.',
    'triggers' : {
        'leader' : '!',
        'help' : {
            'tag' : '!help',
            'description' : 'Ask me how I work.',
        },
        'leaderboard' : {
            'tag' : '!leaderboard',
            'description' : 'See the coolest of cool people.',
        },
        #  'show_uploads' : {
            #  'tag' : '#dailysuffering',
            #  'description' : 'F',
        #  },
    },
    'roles' : {
        'Dumb Idiot' : {
            'min_upload_threshold' : 1,
            'max_upload_threshold' : 7,
        },
        'Real Human Being' : {
            'min_upload_threshold' : 7,
        },
        'Cool People' : {
            'min_upload_threshold' : 15,
            'max_upload_threshold' : None,
        },
    },
    'ranks' : [
        '🏆',
        '✨',
        '🔥',
    ],
    'mrsm_instance' : 'sql:local',
}
