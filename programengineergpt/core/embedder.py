#!/usr/bin/env python3

import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

from programengineergpt.utils.colors import Color


class CodeEmbedder:
    def __init__(self, index_name, username):
        self.index_name = index_name
        self.username = username

    def embed_and_upload(self, code_chunks):
        """
        Embed the code chunks using OpenAI Embeddings and Upload to DeepLake.
        """
        Color.print("{G}Step 4: {W}Embedding and Uploading files to Deeplake Index")
        embeddings = OpenAIEmbeddings()
        DeepLake.from_documents(
            documents=code_chunks,
            dataset_path=f"hub://{self.username}/{self.index_name}",
            embedding=embeddings,
            overwrite=True,
            public=False,
        )
        self.remove_temp_dir()

    def get_all_embeddings(self):
        pass

    def remove_temp_dir(self):
        """
        Remove 'temp_repo' if a repository was cloned
        """
        if os.path.exists("temp_repo"):
            Color.print('{G}Step 5: {W}Removing "temp_repo" contents')
            os.system("rm -rf temp_repo")
