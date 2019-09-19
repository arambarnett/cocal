########### Python 2.7 #############

import httplib, urllib, base64, requests



headers = {
    # Request headers
    'TRN-Api-Key': '4fbe2f49-1452-4167-8bd1-65ab373dcdb5',
}


params = {'platform': 'psn',
          'player_id': 'elkna'}


"""

def req():
    try:
        r = requests.get('https://public-api.tracker.gg/v2/overwatch/standard/profile/{1}/{0}'.format(*params.values()), headers)
        print(r.status_code)
        print(r.content)
    except Exception as e:
        print(e)

"""
"""
params2 = urllib.urlencode({
    # Request parameters
    'seasonId': '{string}',
})
"""
def req():
    try:
        conn = httplib.HTTPSConnection('public-api.tracker.gg')
        conn.request("GET", "/v2/overwatch/standard/profile/{1}/{0}".format(*params.values()), 'body', headers=headers)
        response = conn.getresponse()
        if response.status >= 200 & response.status < 400:
            data = response.read()
            print(data)
            conn.close()
            return response
    except Exception as e:
        print(e)
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
