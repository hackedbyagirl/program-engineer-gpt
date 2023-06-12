#!/usr/bin/env python3

from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

class CodeEmbedder:
    def __init__(self, index_name, username, code_chunks):
        self.code_chunks = code_chunks
        self.index_name = index_name
        self.username = username

    def embed_code(self):
        """
        Embed the code chunks using OpenAI Embeddings.
        """
        embeddings = OpenAIEmbeddings()
        db = DeepLake.from_documents(documents=self.code_chunks, dataset_path=f"hub://{self.username}/{self.index_name}", embedding=embeddings, overwrite=True, public=False)
        


       