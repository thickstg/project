from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')

    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    api_key = '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'
    api_endpoint = 'https://api.openai.com/v1/engines/davinci/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'prompt': prompt,
        'max_tokens': 100  # Adjust as needed
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        return jsonify(result=response.json()['choices'][0]['text'])
    else:
        return jsonify(error=f"Error: {response.status_code}\n{response.text}")

if __name__ == "__main__":
    app.run(debug=True)
