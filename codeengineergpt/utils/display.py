#!/usr/bin/env python3 

# Imports
import os

from codeengineergpt.utils.colors import Color

class Display(object):
    
    @staticmethod
    def display_banner():
        design = ('\n'
                '\n'
                '      ______            __       ______               _                           ______ ____  ______ \n'
                '     / ____/____   ____/ /___   / ____/____   ____ _ (_)____   ___   ___   _____ / ____// __ \/_  __/ \n'
                '    / /    / __ \ / __  // _ \ / __/  / __ \ / __ `// // __ \ / _ \ / _ \ / ___// / __ / /_/ / / /    \n'
                '   / /___ / /_/ // /_/ //  __// /___ / / / // /_/ // // / / //  __//  __// /   / /_/ // ____/ / /     \n'
                '   \____/ \____/ \__,_/ \___//_____//_/ /_/ \__, //_//_/ /_/ \___/ \___//_/    \____//_/     /_/      \n'
                '                                           /____/                                                     \n'
                '\n')
        
        Color.print('{B}' + design)
        header = '{R}                                   @hackedbyagirl {W}| {C} Hack the World\n'
        Color.print(header)

    @staticmethod
    def display_main_description():
        """
        Display main screen at launch
        """
        # Welcome Message
        Color.print("\n\n{B}Welcome to CodeEngineerGPT!")
        Color.print("\n{W}CodeEngineerGPT is an AI tool designed to assist with a variety of coding tasks. Here's how you can use the tool:")

        # Modes of Operation
        Color.print("\n\n{B}Modes of Operation:")
 
        # Mode: Analyze
        Color.print("\n{G}Analyze Mode:")
        Color.print("\n{W}In the 'Analyze' mode, CodeEngineerGPT will thoroughly examine the provided code repository. You will be engaged in an interactive chat session where you can pose queries about the codebase. This could include questions about its structure, dependencies, functions, or any other aspect. The AI will respond with insights, helping you gain a deeper understanding of the code repository.")
        Color.print("\n{L}Use Case: {W}You have a large codebase and you want to understand its structure, dependencies, and other details. You can use the 'Analyze' mode to get a comprehensive analysis of the codebase.")

         # Mode: Develop
        Color.print("\n{G}Develop Mode:")
        Color.print("\n{W}In the 'Develop' mode, CodeEngineerGPT can assist you in setting up a new coding project. This includes planning the project structure, setting up the development environment, and other setup tasks.")
        Color.print("\n{L}Use Case: {W}You are starting a new project and you need assistance in planning the project structure and setting up the development environment. You can use the 'Develop' mode to get assistance with these tasks.")

        Color.print("\n\n{Y}Please select a mode to start using the tool's functionality.\n")

    @staticmethod
    def display_analyze_mode_description():
        Display.clear_screen()
        Color.print("\n{B}*** Welcome to Analyze Mode *** \n")
        Color.print("{W}In this mode, CodeEngineerGPT acts as your personal code assistant. You'll enter an interactive chat where you can ask about the code's structure, dependencies, and more. The AI will provide insightful responses to help you understand your codebase better.")
        Color.print("\n{X}Alternatively, if you already have a codebase indexed using Deeplake, you can provide the required information to your code hub\n")
        Color.print("\n{Y}Please provide the necessary details to start the 'Analyze' mode.")    

    @staticmethod
    def display_develop_mode_description():
        """
        Display Develop Mode description screen
        """
        Display.clear_screen()
        Color.print("\n{B}*** Welcome Develop Mode*** \n")
        Color.print("{W}In this mode, CodeEngineerGPT will assist you in creating a new project. You will enter an interactive session where you will provide a project description of the program/project you want to create.\n")
        Color.print("{W}After you provide a project description, the AI system will ask further questions to gather more information about your project. Your responses will guide the AI in providing the best assistance for your project.\n")

    @staticmethod
    def display_interactive_chat_banner():
        """
        Display welcome banner for interactive chat in Analyze Mode
        """
        Display.clear_screen()
        Color.print("\n{B}Welcome to the Interactive Chat Session in Analyze Mode!\n")
        Color.print("\n{W}You are now in an interactive chat session with CodeEngineerGPT. Feel free to ask any questions about the code repository you provided. The AI will provide insightful responses based on its analysis of the codebase.\n")

        Color.print("\n{B}To Begin: {W}Please enter your question (or 'exit' to stop): ")

    @staticmethod
    def display_interactive_developer_banner():
        """
        Display welcome banner for interactive project developer
        """
        Display.clear_screen()
        Color.print("\n{B}Welcome to the Interactive Project Developer!\n")
        Color.print("\n{W}You are now in an interactive session with CodeEngineerGPT. This mode will assist you in setting up a new coding project, from planning the project structure to setting up the development environment. The AI will provide assistance based on the information you provide.\n")

            
    @staticmethod
    def clear_screen():
        """ Clear Screen """
        os.system('cls' if os.name == 'nt' else 'clear')
                                                                            