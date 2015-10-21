#!/usr/bin/env python
# Command line program to download a user's avatar from github. 
# Usage: `python get_avatar.py <github_username>`. 
import sys
import json
import argparse
import requests
import shutil
# PARSE COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument(  'username')
ARGS = parser.parse_args()
# Call the github api and get user info
RequestUrl = 'https://api.github.com/users/' + ARGS.username
RESULT = requests.get( RequestUrl )
if RESULT.ok:
    user_info = json.loads(RESULT.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write( "Error fetching user information for {0};"
                      "exiting now, sorry...\n".format(ARGS.username) )
    sys.exit()
# DOWNLOAD AND SAVE IMAGE FILE
I = requests.get(avatarURL , stream=True)
if I.ok:
    with open(ARGS.username + '.png' , 'wb') as OuTfIle:
        shutil.copyfileobj( I.raw,  OuTfIle )
