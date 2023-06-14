#!/usr/bin/env python3 

from .colors import Color

class Display(object):
    
    @staticmethod
    def display_banner():
        design = ('\n'
                '\n'
                '  _________       _________      _______                 _____         _____                 _____ _________________ ________ \n' 
                '  __  ____/______ ______  /_____ ___    |___________________(_)__________  /_______ ________ __  /___  ____/___  __ \___  __/ \n' 
                '  _  /     _  __ \_  __  / _  _ \__  /| |__  ___/__  ___/__  / __  ___/_  __/_  __ `/__  __ \_  __/_  / __  __  /_/ /__  /    \n' 
                '  / /___   / /_/ // /_/ /  /  __/_  ___ |_(__  ) _(__  ) _  /  _(__  ) / /_  / /_/ / _  / / // /_  / /_/ /  _  ____/ _  /     \n'  
                '  \____/   \____/ \__,_/   \___/ /_/  |_|/____/  /____/  /_/   /____/  \__/  \__,_/  /_/ /_/ \__/  \____/   /_/      /_/      \n'
                '\n')
        
        Color.print('{B}' + design)
        header = '{R}                                   @hackedbyagirl {W}| {C} Hack the World\n'
        Color.print(header)

    @staticmethod
    def display_general_description():
        """
        Display basic screen at launch
        """
        Color.print("\n\n\n{B}Welcome to CodeAssistantGPT!")
        Color.print("\n{W}CodeAssistantGPT is an AI tool designed to assist with a variety of coding tasks. Here's what you can do with it:")
        Color.print("\n\t- {L}Analyze a code repository: {W}Understand the structure, dependencies, and other details of a codebase.")
        Color.print("\n\t- {L}Develop a new project: {W}Get assistance in setting up a new coding project, including planning and setup.")
        Color.print("\n\t- {L}Generate Code: {W}Have the AI generate code snippets based on your requirements.")
        Color.print("\n\t- {L}Debug and Improve Code: {W}Get help in debugging your code and suggestions for improvements.\n")
        #Color.print("{Y}Please select a mode to start using the tool's functionality.")

    @staticmethod
    def display_mode_description():
        """
        Display Mode description screen
        """
        Color.print("\n\n{B}Modes of Operation:")
        Color.print("\n{G}1. Analyze Mode:\n")
        Color.print("\t{W}In this mode, CodeAssistantGPT can analyze a code repository. This includes understanding the structure, dependencies, and other details of a codebase.\n")
        Color.print("\t{L}Use Case: {W}You have a large codebase and you want to understand its structure, dependencies, and other details. You can use the 'Analyze' mode to get a comprehensive analysis of the codebase.")
        
        Color.print("\n{G}2. Develop Mode:\n")
        Color.print("\t{W}In this mode, CodeAssistantGPT can assist you in setting up a new coding project. This includes planning the project structure, setting up the development environment, and other setup tasks.\n")
        Color.print("\t{L}Use Case: {W}You are starting a new project and you need assistance in planning the project structure and setting up the development environment. You can use the 'Develop' mode to get assistance with these tasks.")
        
        Color.print("\n{Y}Please select a mode to start using the tool's functionality.\n")

    @staticmethod
    def display_analyze_mode_description():
        Color.print("\n{B}Analyze Mode:")
        Color.print("{W}In the 'Analyze' mode, CodeAssistantGPT can analyze a code repository. This includes understanding the structure, dependencies, and other details of a codebase.\n")
        Color.print("{W}You can provide a codebase in one of the following ways:\n")
        Color.print("\t{W} 1. A URL to an online repository (like GitHub or GitLab)")
        Color.print("\t{W} 2. A local path to a code repository on your machine")
        Color.print("\t{W} 3. Using your current directory\n")
        Color.print("{X}Alternatively, if you already have a codebase indexed using Deeplake, you can provide the required information to your code hub\n")
        Color.print("Once the codebase is provided, CodeAssistantGPT will load and/or retrieve the code. After this is complete, you can enter a chat session with the code, where you can ask questions and get insights about the code.\n")
        Color.print("\n{Y}Please provide the necessary details to start the 'Analyze' mode.")                                                                                  