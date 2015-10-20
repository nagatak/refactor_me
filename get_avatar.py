#!/usr/bin/env python
# COMMAND LINE PROGRAM TO DOWNLOAD A USER'S AVATAR FROM GITHUB. USAGE: `PYTHON get_avatar.py <GITHUB_USERNAME>`. 
import sys, json
# PARSE COMMAND LINE ARGUMENTS
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(  'username')
ARGS = parser.parse_args()
# CALL THE GITHUB API AND GET USER INFO
RequestUrl = 'https://api.github.com/users/' + ARGS.username
import requests
RESULT = requests.get( RequestUrl )
if RESULT.ok :
    user_info = json.loads(RESULT.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write( "Error fetching user information for {0}; exiting now, sorry...\n".format(ARGS.username) )
    sys.exit()
# DOWNLOAD AND SAVE IMAGE FILE
I = requests.get(avatarURL , stream=True)
if I.ok:
    import shutil
    with open(ARGS.username + '.png' , 'wb') as OuTfIle:
        shutil.copyfileobj( I.raw,  OuTfIle )
