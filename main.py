#!/usr/bin/env python3

import argparse
import os
import sys

from index_repo import load_and_index_files

def main():
  repo_path = os.getcwd()
  load_and_index_files(repo_path)

if __name__ == "__main__":
    main()
