from dotenv import load_dotenv
import os
import requests

load_dotenv()

STABILITY_AI_KEY = os.getenv("STABILITY_AI_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/search-and-replace",
    headers={
        "authorization": f"Bearer {STABILITY_AI_KEY}",
        "accept": "image/*"
    },
    files={
        "image": open("./IMG_1984.jpg", "rb")
    },
    data={
        "prompt": "Replace hairstyle with a high quiff",
        "search_prompt": "hair",
    },
)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
else:
    raise Exception(str(response.json()))