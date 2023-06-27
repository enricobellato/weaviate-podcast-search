import weaviate
import json

client = weaviate.Client(url = "http://localhost:8080")

nearText = {"concepts": ["ColBERT"]}

response = (
    client.query
    .get("PodClip", ["content", "speaker", "podNum", "summary"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))