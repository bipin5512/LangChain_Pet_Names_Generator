import requests

api_key = "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"
url = "https://api.openai.com/v1/engines/davinci/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "prompt": "What is a capital of India?'",
    "max_tokens": 10,
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["text"])
else:
    print("Error:", response.status_code, response.text)

