#!/usr/bin/python3

# imports
from .config import Config
from .utils.colors import Color
from .utils.banner import banner
from .core.loader import CodeLoader
from .core.embedder import CodeEmbedder
from .core.analyzer import AnalyzeCode


class CodeAssistantGPT(object):
    """
    An AI-powered tool for enhanced comprehension and exploration of code repositories. 
    CodeAssistantGPT can be used to load and analyze code from a GitHub or local repository, 
    split code into manageable chunks for analysis, embed code chunks into a vector space for 
    semantic analysis, and use OpenAI's GPT language model to answer questions about the code. 

    Methods:
        __init__(): Initializes and sets up required configurations for the CodeAssistantGPT class. 
        launch(): Launches the appropriate module for the CodeAssistantGPT.
        load_code(): Loads a codebase repository from GitHub or a local repository.
        analyze_code(): Queries an index to allow coversational QA
    """
    def __init__(self):
        banner()

        Color.print("{P}Setting up required configurations...\n")
        Config.init()

    def launch(self):
        '''
        Launches the appropriate module for the CodeAssistantGPT class (either 'load' or 'analyze').
        '''
        if Config.module == "load":
            self.load_code()
        elif Config.module == "analyze":
            self.analyze_code()

    def load_code(self):
        '''
        Loads a codebase repository from GitHub or a local repository.
        '''
        loader = CodeLoader(Config.repo)
        code_chunks = loader.load_repository()
        embed = CodeEmbedder(Config.index_name, Config.activeloop_username, code_chunks)
        embed.embed_code()

    def analyze_code(self):
        '''
        Queries an index to allow coversational QA
        '''
        analyzer = AnalyzeCode(Config.activeloop_username, Config.dataset, Config.model)
        Color.print("{G}Please enter your question (or 'exit' to stop): ")
        while True:
            Color.print("{G}Question: ")
            question = input()
            if question.lower() == "exit":
                break
            answer = analyzer.ask_question(question)
            Color.print("{B}Answer: {W}" + answer)
