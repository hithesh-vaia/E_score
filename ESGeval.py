from winsorizedcal import calc_winsorized_score
from  sentenceMatcht import score_generator 
import json


class ESGAnswerEval():
    def __init__(self):
        #from sentence_transformers import CrossEncoder
        #self.model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        with open("GRI_CAL.json") as f:
            self.cal_data=json.load(f)

        pass
 
    def index_print(self,num:int):

        print(self.cal_data[num]["Question Quantification Rule ID"],
               self.cal_data[num]["Pillar"],
               self.cal_data[num]["Question Quantification Rule"],
               self.cal_data[num]["Expected Answer"],
               self.cal_data[num]["Low Risk Anchor"],
                self.cal_data[num]["High Risk Anchor"],
                self.cal_data[num]["Anchor Direction"],
                self.cal_data[num]["Anchor Unit"],
                self.cal_data[num]["Question"],
                self.cal_data[num]["Low Risk Score"],
                self.cal_data[num]["High Risk Score"],
                
                
        )

    

    def logic_score(self,question:str,actual_answer:str,expected_answer:str):
        return score_generator(self.model,question,expected_answer,actual_answer)

    def quantitative_score(self,value:int):
        p5=10
        p95=90
        return calc_winsorized_score(value,p5,p95)

    # def scorer_loop():
    #     for i in dataset:
    #         logic_score()
    #         quantitative_score()


test=ESGAnswerEval()

test.index_print(0)


            


        