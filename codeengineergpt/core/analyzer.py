#!/usr/bin/env python3

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

from codeengineergpt.config import Config
from codeengineergpt.utils.colors import Color
from codeengineergpt.utils.display import Display



class AnalyzeCode:
    '''
    Analyze code
    '''
    def __init__(self, username, dataset_name):
        self.username = username
        self.dataset_path = f"hub://{self.username}/{dataset_name}"
        self.model_name = Config.model
        self.embeddings = OpenAIEmbeddings()
        self.db = DeepLake(dataset_path=self.dataset_path, read_only=True, embedding_function=self.embeddings)
        self.retriever = self.db.as_retriever()
        self.retriever.search_kwargs['distance_metric'] = 'cos'
        self.retriever.search_kwargs['fetch_k'] = 100
        self.retriever.search_kwargs['maximal_marginal_relevance'] = True
        self.retriever.search_kwargs['k'] = 10
        self.model = ChatOpenAI(model_name=self.model_name, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
        self.qa = ConversationalRetrievalChain.from_llm(self.model, retriever=self.retriever)
        self.chat_history = []

    def interact(self):
        '''
        Queries an index to allow coversational QA
        '''
        Display.display_interactive_chat_banner()
        while True:
            Color.print("\n{G}Question: ")
            question = input()
            if question.lower() == "exit":
                break
            Color.print("\n{B}Answer:\n")
            answer = self.ask_question(question)
            Color.print("{W}" + answer)
    
    def ask_question(self, question):
        '''
        Ask Questions about your code
        '''
        result = self.qa({"question": question, "chat_history": self.chat_history})
        self.chat_history.append((question, result['answer']))
        return result['answer']