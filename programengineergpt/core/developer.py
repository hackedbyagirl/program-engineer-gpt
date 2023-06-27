#!/usr/bin/env python3

# Imports
import os

from programengineergpt.agents.actions import Actions
from programengineergpt.agents.ai import AIAgent
from programengineergpt.utils.colors import Color
from programengineergpt.utils.display import Display


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
        self.actions = Actions(self.ai_agent)

        self.start()

    def start(self):
        # Display
        Display.display_interactive_developer_banner()

        # Initialize Actions class
        Color.print("\n{L}Analyzing your project...\n")

        reqs = self.process_project_requirements()
        design = self.process_project_design(reqs)
        code_structure = self.process_code_structure(design)
        self.write_initial_code(code_structure)

    def process_project_requirements(self):
        from programengineergpt.prompts.project_reqs import PROJECT_REQS
        
        system_prompt = PROJECT_REQS
        user_prompt = self.project_description
        messages = self.ai_agent.launch(system_prompt, user_prompt)
        return self.actions.clarify(messages)

    def process_project_design(self, requirements):
        from programengineergpt.prompts.project_design import PROJECT_DESIGN
        
        Display.clear_screen()
        system_prompt = PROJECT_DESIGN
        messages = self.actions.gen_design(system_prompt, requirements)
        return self.actions.clarify(messages)

    def process_code_structure(self, design):
        from programengineergpt.prompts.code_design import CODE_DESIGN
        
        Display.clear_screen()
        system_prompt = CODE_DESIGN
        return self.actions.gen_code_structure(system_prompt, design)

    def write_initial_code(self, structure):
        from programengineergpt.prompts.code_writer import CODE_WRITER
        
        system_prompt = CODE_WRITER
        return self.actions.gen_code_structure(system_prompt, structure)
    

    def write_output(self):
        # Save the user project input into the project folder directory
        with open(os.path.join(self.project_folder, 'project_instructions.txt'), 'w') as f:
            f.write(self.project_description)

