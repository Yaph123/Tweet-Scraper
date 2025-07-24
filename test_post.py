# WRITE YOUR CODE HERE

import requests


import requests

url = 'https://httpbin.org/post'
response = requests.post(url)

print(response.json())
