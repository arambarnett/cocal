########### Python 2.7 #############
import http.client
from urllib.parse import urlencode, quote_plus

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '8900cce3660d42b8ab0b0b846f5c0dfe',
}

params = urlencode({
    # Request parameters
    'seasonId': '{string}',
})

try:
    conn = http.client.HTTPSConnection('www.haloapi.com')
    conn.request("GET", "/stats/h5/servicerecords/arena?players={players}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
