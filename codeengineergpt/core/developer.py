#!/usr/bin/env python3

# Imports
import os

from codeengineergpt.agents.ai import AIAgent
from codeengineergpt.prompts.intro import INTRO_SYSTEM_PROMPT

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
        # Launch the AI agent and call the start method
        system_prompt = INTRO_SYSTEM_PROMPT
        user_prompt = self.project_description
        self.ai_agent.launch(system_prompt, user_prompt)

    def write_output(self):
        # Save the user project input into the project folder directory
        with open(os.path.join(self.project_folder, 'project_instructions.txt'), 'w') as f:
            f.write(self.project_description)

