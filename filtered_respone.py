import json


with open("mock_response.json", "r") as file:
    data = json.load(file)

data= data["responses"]
filtered_data = []
for a in data:
    if "ENV" in a["question_ref"]:
        filtered_data.append(a)

with open("filtered_response.json", "w") as file:
    json.dump(filtered_data, file, indent=4)
        


