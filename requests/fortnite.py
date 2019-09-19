########### Python 2.7 #############

import requests
import http.client


headers = {
    # Request headers
    'TRN-Api-Key': '4fbe2f49-1452-4167-8bd1-65ab373dcdb5',
}

"""
params = {'platform': 'psn',
          'player_id': 'zRotation'}
"""

platform = 'gamepad'
player_id = 'zRotation'

def url():
    try:
        print(f'Platform: {platform} \n Player: {player_id}')
        conn = http.client.HTTPSConnection('api.fortnitetracker.com')
        conn.request("GET", "/v2/profile/{platform}/{player_id}", 'body', headers=headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))





def req():
    try:
        r = requests.get(f'https://api.fortnitetracker.com/v1/profile/{platform}/{player_id}', headers)
        print(r.status_code)
        print(r.content)
    except Exception as e:
        print(e)
