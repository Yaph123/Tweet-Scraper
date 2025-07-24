import requests

url = 'https://text-processing.com/api/sentiment/'

# Get user input
user_text = input("Enter some text to send: ")

# Prepare data payload
myobj = {'text': user_text}

# Send POST request
response = requests.post(url, data=myobj)

# Print JSON response
print(response.json())
