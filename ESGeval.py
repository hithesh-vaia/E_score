import string
from winsorizedcal import calc_winsorized_score
from  sentenceMatcht import score_generator 
import json


class ESGAnswerEval():
    def __init__(self):
        from sentence_transformers import CrossEncoder
        self.model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

        self.checker={"text":  "expected_answer",
                     "small_text" :"expected_answer",
                     "number" : "range",
                     "emissions": "range"}

    
 
    def index_print(self,num:int):
        pass


    

    def logic_score(self,question:str,actual_answer:str,expected_answer:str):
        return score_generator(self.model,question,expected_answer,actual_answer)

    def quantitative_score(self, range_str: str, value: float) -> int:
        if value is None:
            return 1 # Default score for no data
            
        try:
            parts = range_str.split("-")
            min_val = float(parts[0])
            max_val = float(parts[1])
        except Exception:
            min_val = 0.0
            max_val = 1000000.0

        if value <= min_val:
            return 10
        if value >= max_val:
            return 1
            
        # Linear scale from 10 to 1 based on where it falls in the range
        ratio = (value - min_val) / (max_val - min_val)
        score = 10 - (9 * ratio)
        return max(1, min(10, round(score)))

    def calculate(self, cal_set: dict, actual_data: dict) -> int:
        ans_type = cal_set.get("answer_type", "")
        question = cal_set.get("question", "")
        
        if ans_type in ["text", "small_text"]:
            expected = cal_set.get("expected_answer", "")
            actual = actual_data.get("value_text", "")
            if not actual or str(actual).strip() == "Not applicable.":
                return 1 # Lowest score for missing or N/A answers
                
            # Assumes logic_score returns a 0.0 to 1.0 similarity metric
            raw_score = self.logic_score(question, actual, expected)
            try:
                val = raw_score.item()
            except AttributeError:
                val = raw_score[0] if isinstance(raw_score, (list, tuple)) else raw_score
            return max(1, min(10, round(float(val) * 10)))
            
        elif ans_type in ["number", "emissions"]:
            expected_range = cal_set.get("range", "0-1000000")
            actual = actual_data.get("value_number")
            
            return self.quantitative_score(expected_range, actual)
            
        return 1



test=ESGAnswerEval()

test.index_print(0)


            


        