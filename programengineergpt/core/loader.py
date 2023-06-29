#!/usr/bin/env python3

import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from programengineergpt.utils.colors import Color

class CodeLoader:
    def __init__(self, col_name=None):
        if col_name is None:
            Color.print("\n{Y}Please enter collection name for code base: ")
            col_name = input("Collection Name: ")

        self.embedding_function = OpenAIEmbeddingFunction()
        self.chromadb_client = chromadb.Client()
        self.code_collection = self.chromadb_client.create_collection(name='code_collection', embedding_function=self.embedding_function)

        self.code_files = []
        self.files = []
        self.chunks = []
        self.extensions = [
            "bash",
            "cfg",
            "conf",
            "cpp",
            "cs",
            "css",
            "dockerignore",
            "editorconfig",
            "gitignore",
            "go",
            "html",
            "htm",
            "ini",
            "java",
            "javascript",
            "json",
            "js",
            "markdown",
            "md",
            "php",
            "py",
            "rb",
            "scala",
            "scss",
            "sh",
            "sql",
            "toml",
            "txt",
            "xml",
            "yaml",
            "yml",
        ]

      

        Color.print("\n\n{G}Launching Code Loader...\n")

    def load_online_repo(self, url):
        """
        Load all code files from the specified repository.
        """
        if "github.com/" in url or "gitlab.com/" in url:
            # Clone repository
            try:
                Color.print("{G}Step 1: {W}Retrieving Code from Online Repository")
                os.system(f"git clone --quiet {url} temp_repo")
                self.load("temp_repo")

            except Exception as e:
                Color.print("{R}!!!: {W}Failed to clone GitHub repository from {Y}" + url)
                Color.p_error(e)

        return self.chunks

    def load_directory(self, path):
        """
        Load all code files from a specified directory.
        """
        # Get code from provided directory
        Color.print("{G}Step 1: {W}Retrieving Code from Local Repository")
        if not os.path.isdir(path):
            raise Exception(f"Invalid local directory: {path}")
        self.load(path)
        return self.chunks

    def load_current_directory(self):
        """
        Load all code files from the current directory.
        """
        Color.print("{G}Step 1: {W}Retrieving Code from Current Directory")
        vector_store = self.load(os.getcwd())
        return vector_store
    
        
    def load(self, root_dir):
        """
        Load all code files from the root directory.
        """
        try:
            Color.print("{G}Step 2: {W}Loading Code for Indexing and Embedding")
            for dirpath, dirnames, filenames in os.walk(root_dir):
                for file in filenames:
                    if file.split(".")[-1] in self.extensions:
                        full_path = os.path.join(dirpath, file)
                        with open(full_path, 'r') as f:
                            self.files.append((full_path, f.read()))
                        
        except Exception as e:
            Color.print("{R}!!!: {W}Failed to load code files from {Y}" + root_dir)
            Color.p_error(e)

        len_files = str(len(self.files))
        Color.print("{Y}Number of Loaded Files: {W}" + len_files)

        Color.print("{G}Step 3: {W}Splitting and Chunking Files")
        self.chunks = self.split_code()

        Color.print("{G}Step 4: {W}Embedding and Uploading to ChromaDB")
        batch_size = 100
        for i in range(0, len(self.chunks), batch_size):
            batch = self.chunks[i:i+batch_size]
            documents = []
            ids = []
            metadatas = []
            for full_path, chunks in batch:
                for j, chunk in enumerate(chunks):
                    documents.append(chunk)
                    ids.append(f"{full_path}_{j}")
                    metadatas.append({'filename': full_path})
            self.code_collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )

        return self.code_collection
    
    def split_code(self):
        """Split the code of all files into chunks."""
        all_chunks = []
        for filename, code in self.files:
            chunks = [code[i:i+1000] for i in range(0, len(code), 1000)]
            all_chunks.append((filename, chunks))
        return all_chunks