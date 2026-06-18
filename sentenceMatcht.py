from sentence_transformers import CrossEncoder
import time

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

model.predict(["pair","ddd"])


start=time.time()

def answer_matcher(question,expected_answer):
    return ""

    


question = "Describe how the organisation integrates biodiversity and climate action synergies?."

expected_answer = """
We integrate biodiversity and climate considerations into data-centre development, renewable-energy projects and water-stewardship programs. Site assessments identify sensitive habitats, protected areas, water-stressed regions and potential land-use impacts before project approval.
Where appropriate, we support watershed restoration, native vegetation planting, wetland rehabilitation and reforestation projects that improve habitat while increasing carbon sequestration and climate resilience. We prioritize native species and monitor outcomes such as restored area, water replenishment, habitat condition and estimated carbon benefits.
Implementation is strongest at major sites, while consistent supplier-level biodiversity data and long-term ecological monitoring are still being expanded.
"""

actual_answer = """
In line with GRI reporting, the organization describes the material topic, actual and potential impacts, management approach, responsibilities and how effectiveness is assessed. The company describes stakeholder engagement with clear ownership, scope, implementation activities, monitoring evidence and actions taken during the reporting period.
The response includes enough context to assess coverage and effectiveness without claiming full maturity. The approach is implemented for material operations and reviewed periodically, with some remaining scope to improve supplier/site-level coverage, external assurance, automation or longer trend history.
"""



def score_generator(model,question:str,expected_answer:str,actual_answer:str):
    start=time.time()
    score = model.predict([
        (
            f"Question: {question}\n Answer: {expected_answer}",
            f"Question: {question}\n Answer: {actual_answer}"
        )])
    end=time.time()
    print(end-start)
    return score