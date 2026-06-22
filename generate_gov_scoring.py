import json

def main():
    try:
        with open('GRI_Questions.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("GRI_Questions.json not found")
        return

    gov_scoring = {}
    
    for item in questions:
        if item.get("category") == "Governance":
            qid = item.get("framework")
            
            # Base node
            node = {
                "question_id": item.get("question_id"),
                "framework": item.get("framework"),
                "framework_codes": item.get("framework_codes", []),
                "index": item.get("index", []),
                "category": item.get("category"),
                "subcategory": item.get("subcategory"),
                "topic": item.get("topic"),
                "question": item.get("question"),
            }
            if "guidance" in item:
                node["guidance"] = item.get("guidance")
                
            ans_type = item.get("answer_type", "text")
            node["answer_type"] = ans_type
            
            if "options" in item:
                node["options"] = item.get("options")
            if "row_labels" in item:
                node["row_labels"] = item.get("row_labels")
            if "columns" in item:
                node["columns"] = item.get("columns")
                
            node["mandatory"] = item.get("mandatory", False)
            
            if "sub_questions" in item:
                node["sub_questions"] = item.get("sub_questions")
                
            if ans_type in ["text", "small_text"]:
                node["expected_answer"] = "TBD"
            elif ans_type == "number":
                node["range"] = "0-1000000"
                
            gov_scoring[qid] = node
            
            # Handle subquestions
            if "sub_questions" in item:
                for sq in item.get("sub_questions"):
                    sq_id = sq.get("framework")
                    sq_node = {
                        "question_id": sq.get("question_id"),
                        "framework": sq.get("framework"),
                        "question": sq.get("question"),
                        "answer_type": sq.get("answer_type", "text")
                    }
                    if "options" in sq:
                        sq_node["options"] = sq.get("options")
                    if "condition" in sq:
                        sq_node["condition"] = sq.get("condition")
                        
                    sq_ans_type = sq.get("answer_type", "text")
                    if sq_ans_type in ["text", "small_text"]:
                        sq_node["expected_answer"] = "TBD"
                    elif sq_ans_type == "number":
                        sq_node["range"] = "0-1000000"
                        
                    gov_scoring[sq_id] = sq_node

    with open('/tmp/GRI_Governance_Scoring.json', 'w', encoding='utf-8') as f:
        json.dump(gov_scoring, f, indent=4)
        
    print(f"Generated /tmp/GRI_Governance_Scoring.json with {len(gov_scoring)} items.")

if __name__ == '__main__':
    main()
