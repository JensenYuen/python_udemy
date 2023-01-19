import requests
import random

term = input('Let me tell you a joke! Give me a topic: ')

uri = 'https://icanhazdadjoke.com/search?'

req = requests.get(
    uri,
    headers={"Accept": "application/json"},
    params={"term": term}
)

if req.ok:
    data = req.json()
    results = data['results']
    joke = random.choice(results)
    print(f"I've got {len(results)} jokes about {term}. Here's one:")
    print(f"{joke['joke']}")
