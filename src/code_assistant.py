#!/usr/bin/python3

# imports
from .config import Config
from .utils.colors import Color
from .core.loader import CodeLoader
from .core.embedder import CodeEmbedder
from .core.analyzer import AnalyzeCode


class CodeAssistantGPT(object):
    def __init__(self):
        from .utils.banner import banner

        banner()

        Color.print("{P}Setting up required configurations...\n")
        Config.init()

    def launch(self):
        if Config.module == "load":
            self.load_code()
        elif Config.module == "analyze":
            self.analyze_code()

    def load_code(self):
        loader = CodeLoader(Config.repo)
        code_chunks = loader.load_repository()
        embed = CodeEmbedder(Config.index_name, Config.activeloop_username, code_chunks)
        embed.embed_code()

    def analyze_code(self):
        analyzer = AnalyzeCode(Config.activeloop_username, Config.dataset, Config.model)
        Color.print("{G}Please enter your question (or 'exit' to stop): ")
        while True:
            Color.print("{G}Question: ")
            question = input()
            if question.lower() == "exit":
                break
            answer = analyzer.ask_question(question)
            Color.print("{B}Answer: {W}" + answer)
