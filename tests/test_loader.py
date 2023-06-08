#!/usr/bin/env python3

import os
import pytest
from src.core.loader import CodeLoader

def test_load_repository_local():
    # Create a temporary directory with a Python file
    os.mkdir("temp_dir")
    with open("temp_dir/test.py", "w") as f:
        f.write("print('Hello, world!')")

    # Load the directory with CodeLoader
    loader = CodeLoader("temp_dir")
    loader.load_repository()

    # Check that the Python file was loaded
    assert "temp_dir/test.py" in loader.get_code_files()

    # Clean up the temporary directory
    os.remove("temp_dir/test.py")
    os.rmdir("temp_dir")

def test_load_repository_invalid():
    # Try to load an invalid directory
    with pytest.raises(Exception) as e:
        loader = CodeLoader("invalid_dir")
        loader.load_repository()
    assert str(e.value) == "Invalid local directory: invalid_dir"

def test_load_repository_github():
    # Try to load a GitHub repository
    # Note: This test requires internet access and the repository to be public
    loader = CodeLoader("https://github.com/githubtraining/hellogitworld")
    loader.load_repository()

    # Check that at least one file was loaded
    assert len(loader.get_code_files()) > 0
