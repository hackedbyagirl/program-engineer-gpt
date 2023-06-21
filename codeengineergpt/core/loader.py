#!/usr/bin/env python3

import os

from langchain.document_loaders import TextLoader

from codeengineergpt.core.splitter import CodeSplitter
from codeengineergpt.utils.colors import Color


class CodeLoader:
    def __init__(self):
        self.code_files = []
        self.chunks = []
        self.extensions = [
            "txt",
            "md",
            "markdown",
            "py",
            "js",
            "java",
            "c",
            "cpp",
            "cs",
            "go",
            "rb",
            "php",
            "scala",
            "html",
            "htm",
            "xml",
            "json",
            "yaml",
            "yml",
            "ini",
            "toml",
            "cfg",
            "conf",
            "sh",
            "bash",
            "css",
            "scss",
            "sql",
            "gitignore",
            "dockerignore",
            "editorconfig",
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
        self.load(os.getcwd())
        return self.chunks

       
    def load(self, root_dir):
        """
        Load all code files from the root directory.
        """
        try:
            Color.print("{G}Step 2: {W}Loading Code for Indexing and Embedding")
            for dirpath, dirnames, filenames in os.walk(root_dir):
                for file in filenames:
                    if file.split(".")[-1] in self.extensions:
                        loader = TextLoader(os.path.join(dirpath, file))
                        self.code_files.extend(loader.load())
        except Exception as e:
            Color.print("{R}!!!: {W}Failed to load code files from {Y}" + root_dir)
            Color.p_error(e)

        len_files = str(len(self.code_files))
        Color.print("{Y}Number of Loaded Files: {W}" + len_files)

        Color.print("{G}Step 3: {W}Splitting and Chunking Files")
        self.split_code()
        return self.chunks

    def split_code(self):
        """
        Return the list of loaded code files in a split and chunked format.
        """
        splitter = CodeSplitter(self.code_files)
        self.chunks = splitter.split_code()