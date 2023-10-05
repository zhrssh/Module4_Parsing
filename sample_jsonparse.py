import json

with open('sample.json', 'r') as json_file:
    json_data = json.load(json_file)
    print(json.dumps(json_data, indent=2))

    courses = []
    for item in json_data["certifications"]:
        courses.append(item["courses"])
    
    print(json.dumps(courses, indent=2))