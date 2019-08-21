########### Python 2.7 #############

import httplib, urllib, base64, requests

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZTFjMjBkMC1hMDU5LTAxMzctOTg3Zi00N2ZiNGVlMjNhYjEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTY1NzQzMTU1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNocmlzLWxld2lzODMxIn0.rAoJb52ml7d-ORY8Mp5MFwy_yABkWRbx67FjtMr1ex0'

#https://documentation.pubg.com/en/making-requests.html#regions

headers = {
    # Request headers
    'Authorization': 'Bearer {}'.format(key),
    'Accept': 'application/vnd.api+json'
}


params = {'platform': 'steam',
          'player_id': 'Rczq'}


def url():
    try:
        conn = httplib.HTTPSConnection('api.pubg.com')
        print('https://api.pubg.com'+"/shards/{1}/players?filter[playerNames]={0}".format(*params.values()))
        conn.request("GET", "/shards/{1}/players?filter[playerNames]={0}".format(*params.values()), 'body', headers=headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))


test_url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Rczq"


def req():
    try:
        r = requests.get(test_url, headers=headers)
        return r
    except Exception as e:
        print(e)

####################################
