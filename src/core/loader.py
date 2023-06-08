#!/usr/bin/env python3

import os

from langchain.document_loaders import TextLoader

class CodeLoader:
    def __init__(self, repository):
        self.repository = repository
        self.code_files = []
        self.extensions = ['txt', 'md', 'markdown', 'py', 'js', 'java', 'c', 'cpp', 'cs', 'go', 'rb', 'php', 'scala', 'html', 'htm', 'xml', 'json', 'yaml', 'yml', 'ini', 'toml', 'cfg', 'conf', 'sh', 'bash', 'css', 'scss', 'sql', 'gitignore', 'dockerignore', 'editorconfig']

    def load_repository(self):
        """
        Load all Python files from the specified repository.
        """
        if "github.com/" in self.repository:
            # If the repository is a GitHub repository, clone it locally first
            try:
                os.system(f"git clone {self.repository} temp_repo")
                root_dir = "temp_repo"
            
            except Exception as e:
                raise Exception(f"Failed to clone GitHub repository: {e}")
        
        else:
            # If the repository is a local directory, use it directly
            if not os.path.isdir(self.repository):
                raise Exception(f"Invalid local directory: {self.repository}")
            
            root_dir = self.repository

        # Walk through the directory load all repository files
        try:
            for dirpath, dirnames, filenames in os.walk(root_dir):
                for file in filenames:
                    if file.split('.')[-1] in self.extensions:
                        loader = TextLoader(os.path.join(dirpath, file))
                        self.code_files.extend(loader.load())

        except Exception as e:
            raise Exception(f"Failed to load code files: {e}")

        print(f'{len(self.code_files)}')

    def get_code(self):
        """
        Return the list of loaded code files.
        """
        self.load_repository()
        return self.code_files
