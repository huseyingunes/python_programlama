import requests

response = requests.get('https://www.python.org')
if response.status_code == 200:
    #data = response.json()  # JSON yanıtını ayrıştır
    print(response.content)
else:
    print('GET isteği başarısız oldu', response.status_code)
