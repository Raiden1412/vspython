import json
import requests
from package1.model_car import car

items = json.loads(
    '[{"id":"1", "text": "item:1"}, {"id":"2", "text": "item:2"}]')
for item in items:
    print(item['text'])

r = requests.get('http://www.google.com')

print(r.status_code)

c = car()
print(str(c.wheel) + ' : ' + str(c.door))

name = input("name is: ")
print(name + 'hello')