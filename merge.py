import json

with open("GRI_E_MATCH.json") as f:
    data1 = json.load(f)

with open("OUR_API_FILTERED.json") as f:
    data2 = json.load(f)

# Create lookup using the key from JSON2
lookup = {item["question_ref"]: item for item in data2}

merged = []

for item in data1:
    # new_item = item.copy()

    # Match Question with query₹
    if item["framework"] in lookup:
        # print(lookup[item["framework"]])
        merged.append({**item,**lookup[item["framework"]]})
        # new_item.update(lookup[item["framework"]])


print(json.dumps(merged, indent=4))