import requests

resp1 = requests.get('http://example.com')
print('Headers:', resp1.headers)
print(resp1.text)
resp2 = requests.post('http://example.com')
print(resp2)
print(resp2.headers)
