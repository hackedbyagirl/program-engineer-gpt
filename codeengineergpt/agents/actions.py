#!/usr/bin/env python3

# Imports
import questionary

from codeengineergpt.utils.colors import Color

class Actions:
    def __init__(self, ai_agent):
        self.ai_agent = ai_agent

    def clarify(self, messages):
        while True:
            # Ask the user if they want to clarify anything
            print("\n")
            user_clarification = questionary.rawselect(
                "Would you like to provide further clarifications:", choices=["Yes", "No"]
                ).ask()

            # Check if the user wants to move on
            if user_clarification == "No":
                print("\n")
                break

            # Get the user's clarification
            Color.print("\n{B}Please provide answer clarification:")
            clarification = input()

            # Pass the user's clarification to the AI for further processing
            messages = self.ai_agent.next_step(messages, clarification)

        return messages
    
    def gen_code(self, system_prompt, messages):
        # Use the messages as the user prompt and the system prompt to call the next_step method of the AI agent
        return self.ai_agent.next_step(messages, system_prompt)