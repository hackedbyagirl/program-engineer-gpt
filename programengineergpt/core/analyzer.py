#!/usr/bin/env python3

from openai import ChatCompletion
from chromadb import Client
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from programengineergpt.config import Config
from programengineergpt.utils.colors import Color
from programengineergpt.utils.display import Display


class AnalyzeCode:
    '''
    Analyze code
    '''
    def __init__(self, code_collection):
        self.code_collection = code_collection
        self.openai_api = ChatCompletion()
        
    def build_prompt_with_context(self, question, context):
        return [{'role': 'system', 'content': "You are interacting with a codebase. Ask any question about the codebase and I will try to provide a relevant piece of code."},
                {'role': 'user', 'content': f""""
    The context is the following:

    {' '.join(context)}

    Question:
    {question}

    Answer:
    """}]

    def interact(self):
        '''
        Queries an index to allow conversational QA
        '''
        Display.display_interactive_chat_banner()
        while True:
            Color.print("\n{G}Question: ")
            question = input()
            if question.lower() == "exit":
                break
            Color.print("\n{B}Answer:\n")
            print(self.ask_question(question))
            #self.ask_question(question)
            #Color.print("{W}" + answer)

    def ask_question(self, question):
        '''
        Ask Questions about your code
        '''
        context = self.retrieve_code(question)
        if not context:
            return "I couldn't find any relevant code."
        
        response = self.openai_api.create(model="gpt-3.5-turbo-16k", messages=self.build_prompt_with_context(question=question, context=context))

        return response['choices'][0]['message']['content']
    

    def retrieve_code(self, query):
        """ Use ChromaDB to retrieve relevant code based on the query """
        results = self.code_collection.query(query_texts=[query], include=['documents', 'distances'], n_results=3)
        if results:
            print(results)
            return results
        else:
            return None  