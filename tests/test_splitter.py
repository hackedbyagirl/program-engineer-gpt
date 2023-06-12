import pytest
from unittest.mock import patch, MagicMock
from src.core.splitter import CodeSplitter

def test_split_code():
    # Mock the CharacterTextSplitter class
    with patch('src.core.splitter.CharacterTextSplitter') as MockCharacterTextSplitter:
        # Create a CodeSplitter object
        splitter = CodeSplitter(["def test(): pass"])

        # Mock the CharacterTextSplitter.split_documents method to return a list of chunks
        mock_splitter = MagicMock()
        MockCharacterTextSplitter.return_value = mock_splitter
        mock_splitter.split_documents.return_value = ["def test(): pass"]

        # Call the split_code method
        chunks = splitter.split_code()

        # Check that the CharacterTextSplitter class was instantiated with the correct arguments
        MockCharacterTextSplitter.assert_called_once_with(chunk_size=1000, chunk_overlap=0)

        # Check that the split_documents method of the CharacterTextSplitter object was called with the correct arguments
        mock_splitter.split_documents.assert_called_once_with(splitter.code_files)

        # Check that the split_code method returned the correct chunks
        assert chunks == ["def test(): pass"]
