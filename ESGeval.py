from winsorizedcal import calc_winsorized_score


class ESGAnswerEval():
    def __init__(self):
        from sentence_transformers import CrossEncoder
        self.model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        pass

    

    def logic_score(self,question:str,answer:str):
        self.model.predict([()])

    def quantitative_score(self,value:int):
        p5=10
        p95=90
        return calc_winsorized_score(value,p5,p95)


            


        