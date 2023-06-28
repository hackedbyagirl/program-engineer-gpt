import chromadb
from chromadb.config import Settings
import openai

from time import sleep

from programengineergpt.utils.colors import Color
from programengineergpt.utils.display import Display

class ChatBot:
    def __init__(self, code_collection):
        self.code_collection = code_collection

        self.openai_api = openai.ChatCompletion()
        self.chat_history = []

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
            self.ask_question(question)

    def ask_question(self, question):
        conversation = [{'role': 'user', 'content': question}]
        response = self.chatbot(conversation)
        print(response)

    def retrieve_code(self, query):
        results = self.code_collection.query(query_texts=[query], include=['documents', 'distances'], n_results=3)
        if results:
            return [result.documents for result in results]
        else:
            return None

    def chatbot(self, messages, model="gpt-4", temperature=0):
        max_retry = 7
        retry = 0
        while True:
            try:
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, temperature=temperature)
                text = response['choices'][0]['message']['content']
                return text
            except Exception as oops:
                print(f'\n\nError communicating with OpenAI: "{oops}"')
                if 'maximum context length' in str(oops):
                    messages.pop(0)
                    print('\n\n DEBUG: Trimming oldest message')
                    continue
                retry += 1
                if retry >= max_retry:
                    print(f"\n\nExiting due to excessive errors in API: {oops}")
                    exit(1)
                print(f'\n\nRetrying in {2 ** (retry - 1) * 5} seconds...')
                sleep(2 ** (retry - 1) * 5)
