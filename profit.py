from ai_service import generate_response

def profitability_analysis(idea):
    prompt = f"Analyze potential revenue streams and cost structures for the following business idea:\n{idea}"
    return generate_response(prompt)
