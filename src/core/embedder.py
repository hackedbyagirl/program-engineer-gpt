#!/usr/bin/env python3

from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings
from ..config import Config

class CodeEmbedder:
    def __init__(self, code_chunks):
        self.code_chunks = code_chunks
        self.username = Config.activeloop_username
        self.embeddings = []

    def embed_code(self):
        """
        Embed the code chunks using OpenAI Embeddings.
        """
        embeddings = OpenAIEmbeddings()
        db = DeepLake.from_documents(documents=self.code_chunks, dataset_path=f"hub://{self.username}/langchain-code", embedding=embeddings, overwrite=True, public=False)
       