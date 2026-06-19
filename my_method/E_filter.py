from urllib import response
import json

import time



valid_metrics=["expected_answer","text",
"small_text", 
"number",
"emissions"]



with open("api.json", "r") as file:
    data = json.load(file)
    api_data=data["responses"]
with open("GRI_Environment_Scoring.json", "r") as file:
    scoring=json.load(file)


k=set()

key=[]

now=time.time()
for a,b in api_data.items():
    if  scoring.get(a):
        cal_set=scoring[a]
        if cal_set["answer_type"] in valid_metrics:





        
