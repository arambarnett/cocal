########### Python 2.7 #############

import http.client, requests

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZTFjMjBkMC1hMDU5LTAxMzctOTg3Zi00N2ZiNGVlMjNhYjEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTY1NzQzMTU1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNocmlzLWxld2lzODMxIn0.rAoJb52ml7d-ORY8Mp5MFwy_yABkWRbx67FjtMr1ex0'

#https://documentation.pubg.com/en/making-requests.html#regions

headers = {
    # Request headers
    'Authorization': 'Bearer {}'.format(key),
    'Accept': 'application/vnd.api+json'
}


params = {'platform': 'steam',
          'player_id': 'Rczq'}

platform = 'steam'
player_id = 'Rczq'


def url():
    try:
        conn = http.client.HTTPSConnection('api.pubg.com')
        print(f"/shards/{platform}/players?filter[playerNames]={player_id}")
        conn.request("GET", f"/shards/{platform}/players?filter[playerNames]={player_id}",'body', headers=headers)
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
        r = requests.get(f"https://api.pubg.com/shards/{platform}/players?filter[playerNames]={player_id}", headers=headers)
        return r
    except Exception as e:
        print(e)

####################################
