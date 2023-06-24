#!/usr/bin/env python3

import argparse
import sys

from programengineergpt.utils.colors import Color


class Arguments(object):
    '''Holds arguments used by CodeAssistantGPT'''

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
        '''Returns parser.args() containing all program arguments'''
        parser = argparse.ArgumentParser(
            description="CodeAssistantGPT: An AI tool designed to assist with a variety of coding tasks."
        )

        parser.add_argument(
            "-c",
            "--chunk_size",
            type=int,
            default=1000,
            help="The size of the chunks to split the code into for analysis. Default is 1000.",
        )

        parser.add_argument(
            "-e",
            "--embedding_size",
            type=int,
            default=1536,
            help="The size of the embeddings to use for semantic analysis. Default is 1536.",
        )

        parser.add_argument(
            "-m",
            "--model",
            type=str,
            default="gpt-3.5-turbo-16k",
            help="The name of the GPT model to use for answering questions. Default is 'gpt-3.5-turbo-16k'.",
        )

        return parser.parse_args()


if __name__ == '__main__':
    from programengineergpt.config import Config

    Config.init()
    a = Arguments(Config)
    args = a.args
    for key, value in sorted(args.__dict__.items()):
        Color.pl('{C}%s: {G}%s{W}' % (key.ljust(21), value))
