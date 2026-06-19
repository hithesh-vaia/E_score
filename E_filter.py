from urllib import response
import json

from ESGeval import ESGAnswerEval

import time



valid_metrics=["expected_answer","text",
"small_text", 
"number",
"emissions"]

Evaluator=ESGAnswerEval()



with open("api.json", "r") as file:
    data = json.load(file)
    api_data=data["responses"]
with open("GRI_Environment_Scoring.json", "r") as file:
    scoring=json.load(file)


k=set()

key=[]

now=time.time()
numerator=0
denominator=0
for a,b in api_data.items():
    if  scoring.get(a):
        cal_set=scoring[a]
        if cal_set.get("answer_type") in valid_metrics:
            score = Evaluator.calculate(cal_set, b)
            print(f"{a}: Score = {score}")
            if score!=None:
                numerator+=score
                denominator+=1

print(numerator/denominator)





        
