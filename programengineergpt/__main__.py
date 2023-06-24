#!/usr/bin/python3

# imports
from programengineergpt.program_engineer import CodeEngineerGPT


########################################################################
def run():
    """
    Launches App
    """
    ca_gpt = CodeEngineerGPT()
    ca_gpt.launch()


if __name__ == "__main__":
    run()