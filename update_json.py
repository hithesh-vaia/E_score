import json

answers = {
    "SOC_HNS_Q5_SQ3": "The OHS management system covers all employees, temporary workers, and contractors across all operational sites, including office, manufacturing, and remote locations. It encompasses all standard work activities as well as high-risk operations, aligning with our comprehensive health and safety policy.",
    "SOC_HNS_Q6": "Hazards are identified through regular workplace inspections, job hazard analyses, and incident reporting. Risks are assessed based on likelihood and severity. The hierarchy of controls is strictly applied, prioritizing elimination and substitution, followed by engineering controls, administrative controls, and PPE. Risk assessments are reviewed annually and after any significant incident to ensure continuous improvement.",
    "SOC_HNS_Q7": "Occupational health services include on-site first aid, access to occupational health nurses, regular health screenings, and an Employee Assistance Program (EAP) for mental health support. The company ensures these services are easily accessible to all workers and strictly maintains confidentiality and quality of care.",
    "SOC_HNS_Q8": "Workers actively participate in the OHS management system through joint health and safety committees, regular safety meetings, and anonymous hazard reporting channels. Employees are consulted on safety policies, risk assessments, and incident investigations to ensure comprehensive input.",
    "SOC_HNS_Q8_SQ2": "The joint health and safety committees meet monthly. They are responsible for reviewing incident reports, conducting safety audits, and evaluating the effectiveness of safety programs. The committee has the authority to make binding recommendations to management regarding safety improvements.",
    "SOC_HNS_Q9": "All workers, including contractors, undergo mandatory OHS induction training upon joining. Role-specific training is provided for hazardous activities such as working at heights or handling chemicals. Refresher courses are conducted annually, and training effectiveness is evaluated regularly.",
    "SOC_HNS_Q10": "The company offers comprehensive wellness programs, including subsidized gym memberships, nutritional counseling, mental health workshops, and smoking cessation programs. These voluntary services aim to address major non-work-related health risks and promote overall employee well-being.",
    "SOC_HNS_Q11": "We conduct rigorous OHS assessments of all suppliers and business partners. High-risk operations within our value chain are subject to regular safety audits. We require partners to adhere to our supplier code of conduct, which mandates strict OHS standards, and we provide capability-building support to mitigate identified risks.",
    "SOC_TRN_Q2": "We offer continuous learning opportunities through internal training academies, tuition reimbursement, and leadership development programs to upskill our workforce. For employees transitioning out due to retirement or restructuring, we provide career counseling, severance packages, and job placement assistance.",
    "SOC_NDC_Q1_SQ1": "All reported incidents of discrimination were thoroughly investigated by an independent ethics committee. Substantiated cases resulted in disciplinary action, including termination where necessary. Remediation plans, such as targeted diversity training and policy updates, were implemented and completed for all affected departments.",
    "SOC_FOA_Q1": "Our supply chain screening identified certain operations in high-risk geographic areas where freedom of association may be restricted by local laws. We closely monitor these regions and prioritize suppliers that demonstrate alternative means of worker representation and dialogue.",
    "SOC_FOA_Q1_SQ1": "We actively engaged with suppliers in high-risk areas to establish parallel means of worker representation, such as worker councils and grievance mechanisms. We also conducted training on labor rights for factory management and workers to ensure open communication channels.",
    "SOC_CHL_Q1": "We continuously assess our supply chain for child labor risks, focusing particularly on raw material sourcing in developing regions. Our risk matrix considers both the type of operation, such as agriculture or mining, and the geopolitical context of the sourcing country.",
    "SOC_CHL_Q1_SQ1": "We enforced a strict zero-tolerance policy for child labor across our supply chain. Measures included unannounced third-party audits, age-verification protocol checks, and community development programs designed to support education and improve local livelihoods.",
    "SOC_FRL_Q1": "Risk assessments identified potential exposure to forced labor primarily within deeper tiers of our supply chain, particularly in sectors relying heavily on migrant labor or in regions with weak labor protections.",
    "SOC_FRL_Q1_SQ1": "We implemented comprehensive due diligence processes, including the 'Employer Pays Principle' to prevent recruitment fees. We conducted specialized audits for forced labor indicators, provided supplier training, and established accessible, anonymous grievance mechanisms for migrant workers.",
    "SOC_IND_Q1_SQ1": "Any incidents involving the rights of indigenous peoples were immediately escalated for review. We engaged in culturally appropriate, good faith consultations with affected communities. Actions taken included project modifications to avoid impacts, fair compensation, and the establishment of ongoing collaborative monitoring agreements.",
    "SOC_COM_Q2": "For operations with potential environmental or social impacts on local communities, we conducted comprehensive Environmental and Social Impact Assessments (ESIA). We implemented robust mitigation hierarchies, ensuring continuous community engagement and the operation of accessible grievance mechanisms to address any concerns promptly."
}

with open('/tmp/GRI_Social_Scoring.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, q in data.items():
    if k in answers:
        q['expected_answer'] = answers[k]
    elif q.get('answer_type') == 'text' and 'expected_answer' in q:
        # Provide a generic fallback just in case
        pass

with open('/tmp/GRI_Social_Scoring.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated /tmp/GRI_Social_Scoring.json")
