import requests

response = requests.get('http://naver.com').text
print(response)