import requests

# Your DeepSeek API key
API_KEY = "sk-503830812d6a4b8895a28a1cc58d6052"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def generate_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are an expert business consultant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
        
        # Print the full response for debugging
        print("Full API Response:", response.json())
        
        response_data = response.json()
        
        if response.status_code != 200:
            return f"API Error: {response_data.get('error', 'Unknown error occurred')}"
        
        if 'choices' in response_data and response_data['choices']:
            return response_data['choices'][0]['message']['content']
        else:
            return "No meaningful response received from the AI."
    
    except Exception as e:
        return f"Error communicating with AI: {e}"
