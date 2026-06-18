from winsorizedcal import calc_winsorized_score
from  sentenceMatcht import score_generator 


class ESGAnswerEval():
    def __init__(self):
        from sentence_transformers import CrossEncoder
        self.model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        pass

    

    def logic_score(self,question:str,actual_answer:str,expected_answer:str):
        return score_generator(self.model,question,expected_answer,actual_answer)

    def quantitative_score(self,value:int):
        p5=10
        p95=90
        return calc_winsorized_score(value,p5,p95)

    def scorer_loop():
        for i in dataset:
            logic_score()
            quantitative_score()


            


        