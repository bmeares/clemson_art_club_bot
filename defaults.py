#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
The default values for this bot.
"""

defaults = {
    'upload_channel' : 'eternal-suffering',
    'upload_messages' : [
        "{message.author.mention} 🎉 Your submission has been accepted! You\'ve uploaded {monthly_submissions} submission{'s' if monthly_submissions != 1 else ''} over {days_uploaded} day{'s' if days_uploaded != 1 else ''}, with {days_remaining} day{'s' if days_remaining != 1 else ''} left in the month.",
        "Way to go {message.author.mention} 🥳! This is your {ordinal(monthly_submissions)} submission and {ordinal(days_uploaded)} day. There are {days_remaining} more day{'s' if days_remaining != 1 else ''} left in this month's leaderboard.",
    ],
    'triggers' : {
        'leader' : '!',
        'help' : {
            'tag' : '!help',
            'description' : '🔧 Ask me how I work.',
        },
        'leaderboard' : {
            'tag' : '!leaderboard',
            'description' : '😎 See the coolest of cool people.',
        },
        'me' : {
            'tag' : '!me',
            'description' : '👀 Find out what I know about you.'
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
