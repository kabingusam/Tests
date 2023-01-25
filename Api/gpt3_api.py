import requests
from flask import Flask, request, jsonify
from aiohttp import ClientSession
import asyncio
import json

app = Flask(__name__)

# cache
cache = {}

# API endpoint
endpoint = "https://api.openai.com/v1/engines/davinci/completions"

# API key
api_key = "YOUR_API_KEY"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

@app.route("/generate", methods=["POST"])
async def generate():
    input_text = request.json["input_text"]
    generated_text = await fetch_text(input_text)
    return jsonify({"generated_text": generated_text})

async def fetch_text(prompt):
    if prompt in cache:
        return cache[prompt]
    payload = {
        "prompt": prompt,
        "max_tokens": 1000,
        "stop": "."
    }
    async with ClientSession() as session:
        async with session.post(endpoint, json=payload, headers=headers) as resp:
            if resp.status != 200:
                raise ValueError("Failed to generate text")
            json_response = await resp.json()
            generated_text = json_response["choices"][0]["text"]
            cache[prompt] = generated_text
            return generated_text

if __name__ == "__main__":
    app.run(debug=True)
