#!/usr/bin/env python3

import argparse, sys
from .utils.colors import Color

class Arguments(object):
    ''' Holds arguments used by CodeAssistantGPT '''

    def __init__(self, configuration):
        self.verbose = '-v' in sys.argv or '-hv' in sys.argv or '-vh' in sys.argv
        self.config = configuration
        self.args = self.get_arguments()

    def _verbose(self, msg):
        if self.verbose:
            return Color.s(msg)
        else:
            return argparse.SUPPRESS 

    def get_arguments(self):
        ''' Returns parser.args() containing all program arguments '''
        
        parser = argparse.ArgumentParser(description="CodeAssistantGPT: Explore and ask questions about a GitHub code repository or local code repository using OpenAI's GPT language model.")

        parser.add_argument(
            "--repository",
            type=str,
            required=True,
            help="The URL of the GitHub repository or the path of the local repository to analyze.",
        )

        parser.add_argument(
            "--question",
            type=str,
            required=True,
            help="The question to ask about the repository.",
        )

        parser.add_argument(
            "--model",
            type=str,
            default="gpt-3.5-turbo",
            help="The name of the GPT model to use for answering questions. Default is 'gpt-3.5-turbo'.",
        )

        parser.add_argument(
            "--chunk_size",
            type=int,
            default=1000,
            help="The size of the chunks to split the code into for analysis. Default is 1000.",
        )

        parser.add_argument(
            "--embedding_size",
            type=int,
            default=1536,
            help="The size of the embeddings to use for semantic analysis. Default is 1536.",
        )

        return parser.parse_args()
    
if __name__ == '__main__':
    from .utils.colors import Color
    from .config import Config
    Config.init(False)
    a = Arguments(Config)
    args = a.args
    for (key,value) in sorted(args.__dict__.items()):
        Color.pl('{C}%s: {G}%s{W}' % (key.ljust(21),value))
