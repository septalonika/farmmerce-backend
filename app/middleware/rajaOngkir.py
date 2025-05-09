import http.client
import json
from app.settings import settings


def get_province(keywords: str):
    print('get province', keywords)
    conn = http.client.HTTPSConnection("api-sandbox.collaborator.komerce.id")
    headers = { 'x-api-key': settings.RAJA_ONGKIR_API_KEY }
    conn.request("GET", f"/tariff/api/v1/destination/search?keyword={keywords}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print('cugud data', data)
    return json.loads(data.decode('utf-8'))

def get_cost(payload):
    print('get cost', payload)
    conn = http.client.HTTPSConnection("api-sandbox.collaborator.komerce.id")
    headers = { 'x-api-key': settings.RAJA_ONGKIR_API_KEY}
    conn.request("GET", f"/tariff/api/v1/cost", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print('cugud data', data)
    return json.loads(data.decode('utf-8'))

