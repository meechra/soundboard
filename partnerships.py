from ai_service import generate_response

def find_partnerships(idea):
    prompt = f"Suggest strategic partnerships to scale the following business idea:\n{idea}"
    return generate_response(prompt)
