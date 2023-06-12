#!/usr/bin/env python3

import os

from langchain.document_loaders import TextLoader
from .splitter import CodeSplitter
from ..utils.colors import Color


class CodeLoader:
    def __init__(self, repository):
        self.repository = repository
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

    def load_repository(self):
        """
        Load all Python files from the specified repository.
        """
        if "github.com/" in self.repository or "gitlab.com/" in self.repository:
            # If the repository is a GitHub repository, clone it locally first
            try:
                Color.print("{G}Step 1: {W}Retrieving Code from Online Repository")
                os.system(f"git clone --quiet {self.repository} temp_repo")
                root_dir = "temp_repo"

            except Exception as error:
                raise Exception(f"Failed to clone GitHub repository: {error}")

        elif self.repository == ".":
            # Get code from current directory
            Color.print("{G}Step 1: {W}Retrieving Code from Current Directory")
            root_dir = os.getcwd()

        else:
            # Get code from provided directory
            Color.print("{G}Step 1: {W}Retrieving Code from Local Repository")
            if not os.path.isdir(self.repository):
                raise Exception(f"Invalid local directory: {self.repository}")

            root_dir = self.repository

        # Walk through the directory load all repository files
        try:
            Color.print("{G}Step 2: {W}Loading Code for Indexing and Embedding")
            for dirpath, dirnames, filenames in os.walk(root_dir):
                for file in filenames:
                    if file.split(".")[-1] in self.extensions:
                        loader = TextLoader(os.path.join(dirpath, file))
                        self.code_files.extend(loader.load())

        except Exception as error:
            raise Exception(f"Failed to load code files: {error}")

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
