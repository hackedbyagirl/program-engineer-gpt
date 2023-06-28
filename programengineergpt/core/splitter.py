#!/usr/bin/env python3

from langchain.text_splitter import CharacterTextSplitter


class CodeSplitter:
    '''
    Splits and chunks code
    '''
    def __init__(self):
        self.chunk_size = 1000  # Config.chunk_size
        self.chunk_overlap = 0  # Config.chunk_overlap

    def split_code(self):
        """
        Split the loaded code files into chunks by function or class.
        """
        texts = [self.code_files[i:i+self.chunk_size] for i in range(0, len(self.code_files), self.chunk_size)]
        #text_splitter = CharacterTextSplitter(
        #    chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        #)
        #texts = text_splitter.split_documents(self.code_files)

        return texts
    
    def split_file(self, code):
        """Split the code into chunks."""
        return [code[i:i+self.chunk_size] for i in range(0, len(code), self.chunk_size)]
