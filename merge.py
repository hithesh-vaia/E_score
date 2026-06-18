import json

with open("GRI_E.json") as f:
    data1 = json.load(f)

with open("mock_response.json") as f:
    data2 = json.load(f)
    print(type(data2))
    data2= data2["responses"]


print(len(data2))

# Create lookup using the key from JSON2
lookup = {
    item["question_ref"].strip().lower(): item
    for item in data2
}
merged=[]
count=0

for item in data1:
    if "framework" in item.keys():
        key = item["framework"].strip().lower()

        if key in lookup:
            merged.append({**item, **lookup[key]})
    else:
        print(item["Question"])
        count += 1   

print(len(merged))
with open("GRI_CAL.json", "w") as file:
    json.dump(merged, file, indent=4)

used = {
    item["framework"].strip().lower()
    for item in data1
    if "framework" in item
}

unused = [
    item["question_ref"]
    for item in data2
    if item["question_ref"].strip().lower() not in used
]

print("Unused API entries:", len(unused))
for q in unused:
    print(repr(q))


print(count)
