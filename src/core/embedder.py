#!/usr/bin/env python3

import os
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings
from ..utils.colors import Color


class CodeEmbedder:
    def __init__(self, index_name, username, code_chunks):
        self.code_chunks = code_chunks
        self.index_name = index_name
        self.username = username

    def embed_code(self):
        """
        Embed the code chunks using OpenAI Embeddings.
        """
        Color.print("{G}Step 4: {W}Embedding and Uploading files to Deeplake Index")
        embeddings = OpenAIEmbeddings()
        db = DeepLake.from_documents(
            documents=self.code_chunks,
            dataset_path=f"hub://{self.username}/{self.index_name}",
            embedding=embeddings,
            overwrite=True,
            public=False,
        )
        self.remove_temp_dir()
        Color.print("{Y}To analyze this data, please run the following command:\n")
        Color.print("{GR}python3 ca_gpt.py analyze --dataset " + self.index_name)

    def remove_temp_dir(self):
        """
        Remove 'temp_repo' if a repository was cloned
        """
        if os.path.exists("temp_repo"):
            Color.print('{G}Step 5: {W}Removing "temp_repo" contents')
            os.system("rm -rf temp_repo")
