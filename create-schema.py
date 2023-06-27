import weaviate
import time

client = weaviate.Client("http://localhost:8080")

schema = {
   "classes": [
       {
           "class": "PodClip",
           "description": "A podcast clip.",
           "moduleConfig": {
               "text2vec-openai": {
                    "model": "ada",
                    "modelVersion": "002",
                    "type": "text"
                }
           },
           "vectorIndexType": "hnsw",
           "vectorizer": "text2vec-openai",
           "properties": [
               {
                   "name": "content",
                   "dataType": ["text"],
                   "description": "The text content of the podcast clip",
                   "moduleConfig": {
                       "text2vec-openai": {
                           "model": "ada",
                           "modelVersion": "002",
                           "type": "text"
                       }
                   }
               },
               {
                "name": "speaker",
                "dataType": ["text"],
                "description": "The speaker in the podcast",
                "moduleConfig": {
                    "text2vec-openai": {
                        "model": "ada",
                        "modelVersion": "002",
                        "type": "text"
                    }
                }
               },
               {
                   "name": "podNum",
                   "dataType": ["int"],
                   "description": "The podcast number.",
                   "moduleConfig": {
                       "text2vec-openai": {
                           "model": "ada",
                           "modelVersion": "002",
                           "type": "text"
                       }
                   }
               },
               {
                   "name": "summary",
                   "dataType": ["text"],
                   "description": "An LLM-generated summary of the podcast clip.",
                   "moduleConfig": {
                       "text2vec-openai": {
                           "model": "ada",
                           "modelVersion": "002",
                           "type": "text"
                       }
                   }
               }
           ]
       }
   ]
}

client.schema.create(schema)