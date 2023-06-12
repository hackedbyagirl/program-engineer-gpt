#!/usr/bin/env python3

from langchain.text_splitter import CharacterTextSplitter
#from ..config import Config

class CodeSplitter:
    def __init__(self, code_files):
        self.code_files = code_files
        self.chunk_size = 1000 #Config.chunk_size
        self.chunk_overlap = 0 #Config.chunk_overlap

    def split_code(self):
        """
        Split the loaded code files into chunks by function or class.
        """
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        texts = text_splitter.split_documents(self.code_files)

        print(f"{len(texts)}")

        return texts

