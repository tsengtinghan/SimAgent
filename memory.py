# import pinecone
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()
# pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))

class ShortTermMemory:
    def __init__(self, capacity=7):
        self.capacity = capacity
        self.memory = []

    def add(self, item):
        if len(self.memory) >= self.capacity:
            self.memory.pop(0)
        self.memory.append(item)

class LongTermMemory:
    def __init__(self, index_name):
        self.index_name = index_name
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name, metric="cosine", engine_type="hnsw")

    def add_item(self, item_id, embedding):
        pinecone.upsert(index_name=self.index_name, items={item_id: embedding})

    def query(self, query_vector, top_k=5):
        results = pinecone.query(queries=[query_vector], index_name=self.index_name, top_k=top_k)
        return results.ids, results.scores
