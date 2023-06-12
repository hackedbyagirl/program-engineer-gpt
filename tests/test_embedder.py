import pytest
from unittest.mock import patch, MagicMock
from src.core.embedder import CodeEmbedder

def test_embed_code():
    # Mock the OpenAIEmbeddings and DeepLake classes
    with patch('src.core.embedder.OpenAIEmbeddings') as MockOpenAIEmbeddings, \
         patch('src.core.embedder.DeepLake') as MockDeepLake:
        # Create a CodeEmbedder object
        embedder = CodeEmbedder(["def test(): pass"])

        # Mock the DeepLake.from_documents method to return a DeepLake object
        mock_deeplake = MagicMock()
        MockDeepLake.from_documents.return_value = mock_deeplake

        # Call the embed_code method
        embedder.embed_code()

        # Check that the OpenAIEmbeddings class was instantiated
        MockOpenAIEmbeddings.assert_called_once()

        # Check that the DeepLake.from_documents method was called with the correct arguments
        MockDeepLake.from_documents.assert_called_once_with(
            dataset_path="hub://hackedbyagirl/langchain-code",
            embedding_function=MockOpenAIEmbeddings.return_value,
            public=False
        )

        # Check that the add_documents method of the DeepLake object was called with the correct arguments
        mock_deeplake.add_documents.assert_called_once_with(embedder.code_chunks)
