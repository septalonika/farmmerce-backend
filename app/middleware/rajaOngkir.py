import http.client
import json


def get_province(keywords: str):
    print('get province', keywords)
    # conn = http.client.HTTPSConnection("api.rajaongkir.com")
    conn = http.client.HTTPSConnection("api-sandbox.collaborator.komerce.id")
    headers = { 'x-api-key': "ZooOuYl8a685dce11f8ec67d1Ey3TLi1" }
    conn.request("GET", f"/tariff/api/v1/destination/search?keyword={keywords}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print('cugud data', data)
    return json.loads(data.decode('utf-8'))

def get_cost(payload):
    print('get cost', payload)
    # conn = http.client.HTTPSConnection("api.rajaongkir.com")
    conn = http.client.HTTPSConnection("api-sandbox.collaborator.komerce.id")
    headers = { 'x-api-key': "ZooOuYl8a685dce11f8ec67d1Ey3TLi1" }
    conn.request("GET", f"/tariff/api/v1/cost", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print('cugud data', data)
    return json.loads(data.decode('utf-8'))

