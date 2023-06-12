#!/usr/bin/python3

# imports
import os
from .config import Config
from .utils.colors import Color
from .core.loader import CodeLoader
from src import __app_name__
from src.code_assistant import CodeAssistantGPT

try:
    from .config import Config
except (ValueError, ImportError) as e:
    raise Exception(
        "You may need to run this from the root directory (which includes README.md)",
        e,
    )

########################################################################
def run():
    ca_gpt = CodeAssistantGPT()
    ca_gpt.launch()

if __name__ == "__main__":
    run()