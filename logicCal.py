### ESG Answer Evaluation class


class ESGAnswerEval():
    def __init__(self):
        from sentence_transformers import CrossEncoder
        self.model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        pass

    def score(self,question:str,answer:str):
        self.model.predict([()])

            


        