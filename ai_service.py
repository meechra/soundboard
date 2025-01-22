import requests

# Your DeepSeek API key (replace with your actual key)
API_KEY = "sk-503830812d6a4b8895a28a1cc58d6052"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def generate_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
