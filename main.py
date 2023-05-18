#!/usr/bin/env python3

import argparse
import os
import sys

from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
  repo_path = os.getcwd()
  repo_name = os.path.basename(repo_path)
    

if __name__ == "__main__":
    main()
