from ai_service import generate_response

def analyze_business_idea(idea):
    prompt = f"Provide a SWOT analysis for the following business idea:\n{idea}"
    return generate_response(prompt)
