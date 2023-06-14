#!/usr/bin/env python3

import os

class Config(object):
    ''' Stores configuration variables and functions for CodeAssistantGPT '''
    initialized = False
    verbose = 0

    @classmethod
    def init(cls):
        '''
            Sets up default initial configuration values.
            Also sets config values based on command-line arguments.
        '''

        if cls.initialized:
            return
        cls.initialized = True

        cls.verbose = 0

        # Environmental Variable
        cls.openai_key = None
        cls.activeloop_key = None
        cls.activeloop_username = None

        # Arguments
        cls.model = 'gpt-3.5-turbo-16k' #gpt-4 if you have the access
        cls.chunk_size = 1000
        cls.chunk_overlap = 0
        cls.embedded_size = 1536
        
        # Will overwrite provided args    
        cls.load_args()
        cls.load_env()

############################################

    @classmethod
    def load_args(cls):
        ''' Sets configuration values based on Argument.args object '''
        from .args import Arguments
        
        args = Arguments(cls).args
               
        #get options
        cls.load_ops(args)

    @classmethod
    def load_ops(cls, args):
        ''' Sets configuration values based on parsed command-line arguments '''
        cls.module = args.module

        if args.module == 'load':
            cls.repo = args.repository if args.repository else cls.repo
            cls.index_name = args.index if args.index else cls.index_name
            cls.chunk_size = args.chunk_size if args.chunk_size else cls.chunk_size
            cls.embedded_size = args.embedding_size if args.embedding_size else cls.embedded_size
        elif args.module == 'analyze':
            cls.dataset = args.dataset if args.dataset else cls.dataset
            cls.model = args.model if args.model else cls.model

    @classmethod
    def load_env(cls):
        ''' Gets Environmental Variables '''
        from dotenv import load_dotenv

        # Get Environmental Variable
        load_dotenv()
        
        cls.openai_key = os.getenv('OPENAI_API_KEY')
        cls.activeloop_key = os.getenv('ACTIVELOOP_TOKEN')
        cls.activeloop_username = os.getenv('DEEPLAKE_ACCOUNT_NAME')

    @classmethod
    def exit(cls, code=0):
        print('Stopping program')

        exit(code)

###############################################################

if __name__ == '__main__':
    Config.init()