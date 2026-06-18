import json


with open("GRI__CAL__MATCH.json", "r") as file:
    data = json.load(file)

filtered_data = []
for a in data:
    if "ENV" in a.get("framework", ""):
        filtered_data.append(a)

with open("filtered_response.json", "w") as file:
    json.dump(filtered_data, file, indent=4)
        


