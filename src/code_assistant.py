#!/usr/bin/python3

# imports
import os
from .config import Config
from .utils.colors import Color
from .core.loader import CodeLoader

class CodeAssistantGPT(object):
    def __init__(self):
        Config.init()

        Color.print("{R}Setting up required configurations...\n")

    def launch(self):
        self.load_code()

    def load_code(self):
        files = CodeLoader.get_code(Config.repo)