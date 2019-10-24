########### Python 2.7 #############

import httplib, urllib, base64, requests



headers = {
    # Request headers
    'TRN-Api-Key': '4fbe2f49-1452-4167-8bd1-65ab373dcdb5',
}


params = {'platform': '2',
          'player_id': 'King_Canuck8'}


try:
    r = requests.get('https://cod-api.tracker.gg/v1/standard/bo4/profile/{1}/{0}'.format(*params.values()), headers)
    print(r.status_code)
    print(r.content)
except Exception as e:
    print(e)
