#!/usr/bin/env python3

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

class AnalyzeCode:
    def __init__(self, username, dataset_name, model_name='gpt-3.5-turbo'):
        self.username = username
        self.dataset_path = f"hub://{self.username}/{dataset_name}"
        self.model_name = model_name
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

    def ask_question(self, question):
        result = self.qa({"question": question, "chat_history": self.chat_history})
        self.chat_history.append((question, result['answer']))
        return result['answer']
