#!/usr/bin/env python3

# Imports
import os

from codeengineergpt.agents.ai import AIAgent
from codeengineergpt.agents.actions import Actions
from codeengineergpt.prompts.intro import INTRO_SYSTEM_PROMPT
from codeengineergpt.prompts.setup_project import PROJECT_SETUP
from codeengineergpt.utils.colors import Color
from codeengineergpt.utils.display import Display

class Developer:
    def __init__(self, project_description, project_folder):
        self.project_description = project_description
        self.project_folder = project_folder
        
         # Create an empty folder for the project
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)

        # Save project descrition
        self.write_output()

        # Initialize an AI agent
        self.ai_agent = AIAgent()
        self.start()

    def start(self):
        # Display
        Display.display_interactive_developer_banner()
        
        # Initialize Actions class
        Color.print("\n{L}Analyzing your project...\n")
        actions = Actions(self.ai_agent)

        # Launch the AI agent and call the start method
        system_prompt = INTRO_SYSTEM_PROMPT
        user_prompt = self.project_description
        messages = self.ai_agent.launch(system_prompt, user_prompt)

        # Get user clarification response
        messages = actions.clarify(messages)

        # Move to the first code generation phase
        system_prompt = PROJECT_SETUP
        messages = actions.gen_code(system_prompt, messages)


    def write_output(self):
        # Save the user project input into the project folder directory
        with open(os.path.join(self.project_folder, 'project_instructions.txt'), 'w') as f:
            f.write(self.project_description)

    def first_code_generation_phase(self, messages):
        # Implement the logic for the first code generation phase
        pass

