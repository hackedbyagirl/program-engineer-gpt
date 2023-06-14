#!/usr/bin/env python3

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

from ..config import Config
from ..utils.colors import Color

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
        self.model = ChatOpenAI(model_name=self.model_name)
        self.qa = ConversationalRetrievalChain.from_llm(self.model, retriever=self.retriever)
        self.chat_history = []

    def interact(self):
        '''
        Queries an index to allow coversational QA
        '''
        Color.print("{G}Please enter your question (or 'exit' to stop): ")
        while True:
            Color.print("{G}Question: ")
            question = input()
            if question.lower() == "exit":
                break
            answer = self.ask_question(question)
            Color.print("{B}Answer: {W}" + answer)
    
    def ask_question(self, question):
        '''
        Ask Questions about your code
        '''
        result = self.qa({"question": question, "chat_history": self.chat_history})
        self.chat_history.append((question, result['answer']))
        return result['answer']