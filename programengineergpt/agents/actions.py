#!/usr/bin/env python3

# Imports
import questionary

from programengineergpt.utils.colors import Color


class Actions:
    """AI Actions"""

    def __init__(self, ai_agent):
        self.ai_agent = ai_agent

    def clarify(self, messages):
        """Answer clarification questions"""
        while True:
            # Ask the user if they want to clarify anything
            print("\n")
            user_clarification = questionary.rawselect(
                "How would you like to proceed:",
                choices=["Answer Question", "Skip Question", "End Question Answering"],
            ).ask()

            # Check if the user wants to move on
            if user_clarification == "End Question Answering":
                print("\n")
                break

            #  Get the user's clarification
            if user_clarification == "Skip Question":
                clarification = "Skip"
                print("\n")

            # Get the user's clarification
            else:
                Color.print("\n{B}Please provide answer clarification:")
                clarification = input()

            # Pass the user's clarification to the AI for further processing
            messages = self.ai_agent.next_step(messages, clarification)

        return messages

    def gen_design(self, system_prompt, messages):
        """Launch Project Design Phase"""
        return self.ai_agent.next_step(messages, system_prompt)

    def gen_code_structure(self, system_prompt, messages):
        """Launch Project Code Development Phase"""
        return self.ai_agent.next_step(messages, system_prompt)

    def gen_init_code(self, system_prompt, messages):
        """Generate Initial Code"""
        return self.ai_agent.next_step(messages, system_prompt)

    def gen_unit_tests(self, system_prompt, messages):
        """Generate Unit Tests"""
        return self.ai_agent.next_step(messages, system_prompt)

    def gen_doumentaion(self, system_prompt, messages):
        """Generate Code Documentation"""
        return self.ai_agent.next_step(messages, system_prompt)
