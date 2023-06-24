from src.config import Config


def test_init():
    # Call the init method
    Config.init()

    # Check that the initialized attribute is set to True
    assert Config.initialized is True

    # Check that the default values are set correctly
    assert Config.verbose == 0
    assert Config.openai_key is not None
    assert Config.activeloop_key is not None
    assert Config.activeloop_username is not None
    assert Config.repo is None
    assert Config.model == 'gpt-3.5-turbo'
    assert Config.question is None
    assert Config.chunk_size == 1000
    assert Config.chunk_overlap == 0
    assert Config.embedded_size == 1536
