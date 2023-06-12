import os
import pytest
from unittest.mock import patch, MagicMock
from src.config import Config

def test_init():
    # Call the init method
    Config.init()

    # Check that the initialized attribute is set to True
    assert Config.initialized == True

    # Check that the default values are set correctly
    assert Config.verbose == 0
    assert Config.openai_key != None
    assert Config.activeloop_key != None
    assert Config.activeloop_username != None
    assert Config.repo == None
    assert Config.model == 'gpt-3.5-turbo'
    assert Config.question == None
    assert Config.chunk_size == 1000
    assert Config.chunk_overlap == 0
    assert Config.embedded_size == 1536