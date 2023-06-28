#!/usr/bin/env python3

import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

#from langchain.vectorstores import DeepLake

from programengineergpt.utils.colors import Color

EMBEDDING_MODEL = "text-embedding-ada-002"
BATCH_SIZE = 1000 


class CodeEmbedder:
    """ Embed Code using AI and Upload to ChromaDB"""
    def __init__(self):
        self.vectordb = None

    def embed_code(self, code_chunks):
        embeddings = []
        for batch_start in range(0, len(code_chunks), BATCH_SIZE):
            batch_end = batch_start + BATCH_SIZE
            batch = code_chunks[batch_start:batch_end]
            print(f"Batch {batch_start} to {batch_end-1}")
            response = openai.Embedding.create(model=EMBEDDING_MODEL, input=batch)
            for i, be in enumerate(response["data"]):
                assert i == be["index"]  # double check embeddings are in same order as input
            batch_embeddings = [e["embedding"] for e in response["data"]]
            embeddings.extend(batch_embeddings)

            return embeddings

    
    def embed_and_upload(self, code_chunks):
        """
        Embed the code chunks using OpenAI Embeddings and Upload to DeepLake.
        """
        Color.print("{G}Step 4: {W}Embedding and Uploading files to ChromaDB")
        embeddings = OpenAIEmbeddings()
        self.vectordb = Chroma.from_documents(
            documents=code_chunks,
            embedding=embeddings,
        )
        self.remove_temp_dir()


    def remove_temp_dir(self):
        """
        Remove 'temp_repo' if a repository was cloned
        """
        if os.path.exists("temp_repo"):
            Color.print('{G}Step 5: {W}Removing "temp_repo" contents')
            os.system("rm -rf temp_repo")
