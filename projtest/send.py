import requests

token_ip = input('Enter Token = \n')

headers = {}
token = token_ip
headers['Authorization'] = 'Bearer ' + token

r = requests.get('http://127.0.0.1:8000/languages/', headers=headers)

print('Output of Operation: \n' + r.text)


'''
- => python3 send.py 
- op:
Enter Token = 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE1NjUwOTYzNzEsImp0aSI6IjJmMmFjNTc1OTlkMjQ2MjY5OGE5Mjg1NWJhZDliMGZiIiwidG9rZW5fdHlwZSI6ImFjY2VzcyJ9.rxhqWHbaZINAqg1eDQEN9P9cv45lVwF0ZNkP-uh3VFs
Output of Operation: 
[{"id":2,"url":"http://127.0.0.1:8000/languages/2/","name":"Python","paradigm":"Awesome library"},{"id":4,"url":"http://127.0.0.1:8000/languages/4/","name":"ROR","paradigm":"Ruby on Rails"},{"id":6,"url":"http://127.0.0.1:8000/languages/6/","name":"GoLang","paradigm":"ConCurrent - Excecution"},{"id":1,"url":"http://127.0.0.1:8000/languages/1/","name":"Java9","paradigm":"OOP piller"}]

'''