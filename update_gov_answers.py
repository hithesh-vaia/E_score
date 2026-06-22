import json

answers = {
    "GOV_BRD_Q3": "The highest governance body is the Board of Directors, which is composed of a majority of independent non-executive directors. It includes dedicated sub-committees for Audit, Risk Management, Remuneration, and Sustainability. The Sustainability Committee directly oversees ESG strategies and reports quarterly to the main Board.",
    "GOV_BRD_Q4": "The Nomination Committee oversees the selection process, utilizing a skills matrix to ensure diverse expertise in industry knowledge, financial acumen, and ESG proficiency. Candidates are evaluated for independence, diversity (including gender and background), and their ability to represent stakeholder interests effectively.",
    "GOV_BRD_Q5_SQ1": "The Chair holds an executive management role to ensure swift decision-making and deep operational alignment. To prevent conflicts of interest, a strong Lead Independent Director is appointed, and executive sessions without the Chair are held regularly. Key oversight committees are composed exclusively of independent directors.",
    "GOV_BST_Q1": "The Board of Directors holds ultimate responsibility for approving the sustainability strategy and overarching ESG goals. Senior executives, led by the Chief Sustainability Officer, are responsible for developing these strategies, embedding them into business operations, and presenting annual updates and performance metrics to the Board for review.",
    "GOV_BST_Q2": "The Board delegates day-to-day management of ESG impacts to the Executive Management Team, specifically through the Sustainability Steering Committee. Clear mandates and performance targets are established, and regular progress reports are mandated to ensure accountability at both the operational and executive levels.",
    "GOV_BST_Q3_SQ1": "The Board's Audit and Sustainability Committees conduct a comprehensive review of the annual sustainability report. They ensure alignment with financial reporting, verify data integrity through internal audits, and grant final approval before publication.",
    "GOV_BST_Q3_SQ2": "Responsibility is fully assumed by the Board; however, if delegated, it is due to a specific structural mandate where a specialized executive ESG committee holds final authority, subject to annual retrospective review by the Board.",
    "GOV_GOV_Q1": "A rigorous Conflict of Interest Policy requires annual declarations from all Board members and executives. Any potential conflict must be disclosed immediately, and conflicted individuals are recused from relevant discussions and voting processes.",
    "GOV_GOV_Q2_SQ1": "Critical concerns are escalated to the Board via a formalized risk management framework. The Chief Risk Officer and internal audit teams report directly to the Board's Risk Committee. Additionally, a secure, anonymous whistleblowing mechanism provides a direct channel to the Lead Independent Director.",
    "GOV_GOV_Q2_SQ3": "Critical concerns primarily include significant regulatory compliance breaches, major cybersecurity incidents, systemic operational risks, and severe allegations of ethical misconduct or environmental violations.",
    "GOV_PRM_Q1": "The Board undergoes annual specialized training on emerging ESG trends, climate risk, and human rights. External experts and consultants are frequently invited to brief the Board, ensuring their knowledge remains current with global sustainability standards.",
    "GOV_PRM_Q2": "An annual Board effectiveness review is conducted, incorporating self-assessments and peer evaluations. Every three years, an independent external consultant facilitates a comprehensive review that specifically evaluates the Board's oversight of sustainability and ESG impacts.",
    "GOV_PRM_Q2_SQ3": "Following performance evaluations, we implement targeted training programs, restructure committee memberships to optimize skill alignment, and prioritize specific ESG expertise in our ongoing director succession planning.",
    "GOV_PRM_Q3": "Remuneration is structured to align with long-term corporate strategy and stakeholder interests. It includes a fixed base salary and variable components (bonuses and equity) that are strictly tied to both financial performance and specific ESG targets.",
    "GOV_PRM_Q4": "The independent Remuneration Committee designs the policies using market benchmarking and external compensation consultants. The policies are reviewed annually and submitted to shareholders for an advisory vote to ensure transparency and alignment.",
    "GOV_STR_Q1": "Sustainable development is core to our corporate purpose and long-term value creation. Our leadership is fully committed to integrating robust ESG practices into every aspect of our business, ensuring we deliver positive impacts for our stakeholders and the environment.",
    "GOV_POL_Q1": "Our Code of Conduct and overarching corporate policies explicitly commit to upholding human rights, ensuring fair labor practices, maintaining zero tolerance for corruption, and actively minimizing our environmental footprint across all operations and supply chains.",
    "GOV_POL_Q2": "Policies are embedded through mandatory annual employee training, rigorous supplier due diligence, and integration into performance management systems. Compliance is continuously monitored via internal audits and a robust vendor risk management framework.",
    "GOV_REM_Q1": "We operate accessible, anonymous grievance channels for all stakeholders. Any reported negative impact triggers a formalized investigation protocol. We are committed to providing timely, fair, and transparent remediation, and we actively adjust our processes to prevent recurrence.",
    "GOV_REM_Q2": "Employees and external stakeholders can seek advice or raise concerns via a 24/7 confidential ethics hotline, dedicated compliance officers, or direct escalation to the internal audit department. Retaliation against whistleblowers is strictly prohibited.",
    "GOV_ETH_Q2_SQ4": "Any significant instances of non-compliance are thoroughly investigated and publicly disclosed in our annual sustainability report, detailing the nature of the breach, the financial or regulatory penalties incurred, and the immediate corrective actions implemented.",
    "GOV_STE_Q1": "We are active members of the UN Global Compact, the World Business Council for Sustainable Development (WBCSD), and several industry-specific regulatory task forces, where we hold board or committee leadership positions to drive sector-wide sustainability standards.",
    "GOV_STE_Q2": "We engage stakeholders through a structured, multi-channel approach including annual materiality assessments, regular community town halls, investor roadshows, and ongoing dialogue with NGOs. Feedback is systematically integrated into our strategic planning.",
    "GOV_RPT_Q1": "The sustainability report covers all global subsidiaries, joint ventures, and operational facilities where the organization holds majority ownership or exercises significant operational control.",
    "GOV_RPT_Q2": "The reporting period spans the fiscal year from January 1 to December 31. The report is published annually in April. Inquiries can be directed to the Chief Sustainability Officer via the dedicated contact email provided in the report.",
    "GOV_RPT_Q3": "Any restatements of previously published data due to changes in measurement methodologies, data scope expansions, or error corrections are clearly identified and explained in the methodology section of the current report.",
    "GOV_RPT_Q4_SQ1": "Our Scope 1 and 2 GHG emissions, along with key social metrics, have received limited external assurance in accordance with the ISAE 3000 standard. Limitations are explicitly stated in the independent assurance statement appended to the report.",
    "GOV_RPT_Q4_SQ2": "The assurance provider is an independent, globally recognized auditing firm with no financial or operational ties to the organization, ensuring complete objectivity and adherence to professional independence standards.",
    "GOV_RPT_Q4_SQ3": "Our policy mandates external assurance for all critical ESG data to ensure credibility. The Board's Audit Committee selects the independent assurance provider, reviews the assurance scope and findings, and formally approves the final statement.",
    "UNGC_G1_SQ_001": "Senior management holds bi-weekly sustainability reviews, and ESG performance is a standing agenda item at all quarterly Board meetings, ensuring continuous top-level engagement and strategic alignment.",
    "UNGC_G12_SQ_001": "We actively integrate ESG criteria into our capital allocation and investment decisions. This includes issuing green bonds, utilizing sustainability-linked loans, and applying rigorous environmental and social screens to all potential acquisitions."
}

with open('/tmp/GRI_Governance_Scoring.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, q in data.items():
    if k in answers:
        q['expected_answer'] = answers[k]
    elif q.get('answer_type') in ('text', 'small_text') and 'expected_answer' in q:
        pass

with open('/tmp/GRI_Governance_Scoring.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated /tmp/GRI_Governance_Scoring.json")
