import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def ask_ollama(prompt: str) -> str:
    response = requests.post(
      OLLAMA_URL,
      json={
          "model": MODEL,
          "prompt": prompt,
          "stream": False
      }
    )
    return response.json().get("response", "")
