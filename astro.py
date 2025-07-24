import requests

#Employ GET Request
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

#Print status code
print(response.status_code)

#Parse people, number, and message keys
people=(data['people'])
number=(data['number'])
message=(data['message'])

#Print first 5 names in people dictionary.
for person in range(5):
  print(people[person]['name'])