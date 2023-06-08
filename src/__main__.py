#!/usr/bin/python3

# imports
import os
from .config import Config
from .utils.colors import Color
from .core.loader import CodeLoader
from src import __app_name__

try:
    from .config import Config
except (ValueError, ImportError) as e:
    raise Exception(
        "You may need to run this from the root directory (which includes README.md)",
        e,
    )

class CodeAssistantGPT(object):
    def __init__(self):
        Config.init()

        Color.print("{R}Setting up required configurations...\n")

    def launch(self):
        self.load_code()

    def load_code(self):
        CodeLoader.load_repository(Config.repo)

########################################################################
def run():
    ca_gpt = CodeAssistantGPT()
    ca_gpt.launch()

if __name__ == "__main__":
    run()