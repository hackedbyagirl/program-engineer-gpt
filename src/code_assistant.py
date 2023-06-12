#!/usr/bin/python3

# imports
import os
from .config import Config
from .utils.colors import Color
from .core.loader import CodeLoader
from .core.embedder import CodeEmbedder

class CodeAssistantGPT(object):
    def __init__(self):
        Color.print("{R}Setting up required configurations...\n")
        Config.init()

    def launch(self):
        self.load_code()

    def load_code(self):
        loader = CodeLoader(Config.repo)
        code_chunks = loader.load_repository()
        embed = CodeEmbedder(code_chunks)
        embed.embed_code()

        