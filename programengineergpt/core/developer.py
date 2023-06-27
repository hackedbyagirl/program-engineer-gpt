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
        self.write_output(file_name='project_instructions.txt', content=self.project_description)

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
        initial_code = self.write_initial_code(code_structure)
        unit_tests = self.write_unit_tests(initial_code)
        final = self.write_code_documentation(unit_tests)
        self.save_chat_history(messages=final)

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
    
    def write_unit_tests(self, code):
        from programengineergpt.prompts.code_tests import UNIT_TEST_GENERATOR

        system_prompt = UNIT_TEST_GENERATOR
        return self.actions.gen_unit_tests(system_prompt, code)

    def write_code_documentation(self, code):
        from programengineergpt.prompts.project_documentation import DOCUMENTATION_WRITER

        system_prompt = DOCUMENTATION_WRITER
        return self.actions.gen_doumentaion(system_prompt, code)

    def write_output(self, file_name, content):
        # Save the user project input into the project folder directory
        with open(os.path.join(self.project_folder, file_name), 'w') as f:
            f.write(content)

    def save_chat_history(self, messages):
        with open(os.path.join(self.project_folder, 'chat_history.txt'), 'w') as f:
            for message in messages:
                if message['role'] == 'assistant':
                    f.write(f"{message['content']}\n")


