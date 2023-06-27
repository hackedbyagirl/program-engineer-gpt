#!/usr/bin/env python3

# Imports
import os

from programengineergpt.agents.actions import Actions
from programengineergpt.agents.ai import AIAgent
from programengineergpt.prompts.intro import INTRO_SYSTEM_PROMPT
from programengineergpt.prompts.setup_project import PROJECT_SETUP
from programengineergpt.prompts.project_reqs import PROJECT_REQS
from programengineergpt.prompts.project_design import PROJECT_DESIGN
from programengineergpt.prompts.code_design import CODE_DESIGN
from programengineergpt.prompts.code_writer import CODE_WRITER
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
        self.start()

    def start(self):
        # Display
        Display.display_interactive_developer_banner()

        # Initialize Actions class
        Color.print("\n{L}Analyzing your project...\n")
        actions = Actions(self.ai_agent)

        # Launch the AI agent and begin project requirements
        system_prompt = PROJECT_REQS
        user_prompt = self.project_description
        messages = self.ai_agent.launch(system_prompt, user_prompt)

        # Get user clarification response
        messages = actions.clarify(messages)

        # Get Project requirements
        Display.clear_screen()
        system_prompt = PROJECT_DESIGN
        messages = actions.gen_design(system_prompt, messages)
        messages = actions.clarify(messages)

        # Move to the code strucuture setup
        Display.clear_screen()
        system_prompt = CODE_DESIGN
        messages = actions.gen_code_structure(system_prompt, messages)

        # Write Initial Code
        #Display.clear_screen()
        system_prompt = CODE_WRITER
        messages = actions.gen_code_structure(system_prompt, messages)

    def write_output(self):
        # Save the user project input into the project folder directory
        with open(os.path.join(self.project_folder, 'project_instructions.txt'), 'w') as f:
            f.write(self.project_description)

    def first_code_generation_phase(self, messages):
        # Implement the logic for the first code generation phase
        pass

