#!/usr/bin/python3

# imports
from .utils.colors import Color
from .config import Config
from .utils.display import Display
from .utils.cli import CLI

class CodeAssistantGPT(object):
    """
    An AI-powered tool designed to assist with a variety of coding tasks.
    This includes:
        - Understanding the structure, dependencies, and other details of a codebase.
        - Getting assistance in setting up a new coding project, including planning and setup.
        - Having the AI generate code snippets based on your requirements.
        - Getting help in debugging your code and suggestions for improvements.
    """

    def __init__(self):
        """
        Main Entry point for the code
        """
        Display.display_banner()
        Display.display_general_description()
        Color.print("{Y}Begining Setup ...\n")
        Color.print("{W}1. {P}Setting up required configurations\n")
        
        # Initialize Config
        Config.init()

    def launch(self):
        '''
        Launches the main interactive interface.
        '''
        app = CLI()
        app.launc_main_cli()
