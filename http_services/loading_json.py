import json

text_json = '''{
    "demo": "Processing JSON in Python",
    "instructor": "Michael",
    "duration": 5.0
}'''

print(text_json)

data = json.loads(text_json)

print(data)

instructor = data.get('instructor', 'SUBSTITUTE')
print(f"Your instructor is {instructor}")

data['instructor'] = 'Jeff'
new_json = json.dumps(data)

print(new_json)