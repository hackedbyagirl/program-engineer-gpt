#!/usr/bin/env python3

# Imports

import openai

from programengineergpt.config import Config


class AIAgent:
    def __init__(self):
        self.model = Config.model
        self.temperature = 0.1

        try:
            openai.Model.retrieve(self.model)
        except openai.InvalidRequestError:
            print(
                f"Model {self.model} not available for provided API key. Please Update your configuration file")


    def launch(self, system_prompt, user_prompt):
        # Create a list of two dictionaries representing a system role and a user role
        msg = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Send the message to the next method
        return self.next_step(msg)

    def next_step(self, messages: list[dict[str, str]], user_prompt=None):
        # Add user prompt to messages if provided
        if user_prompt:
            messages.append({"role": "user", "content": user_prompt})

        response = openai.ChatCompletion.create(
            messages=messages,
            stream=True,
            model=self.model,
            temperature=self.temperature,
        )

        chat = []
        for chunk in response:
            delta = chunk["choices"][0]["delta"]
            msg = delta.get("content", "")
            print(msg, end="")
            chat.append(msg)
        print()

        messages.append({"role": "assistant", "content": "".join(chat)})

        return messages

    def gen_system_prompt(self, msg):
        return {"role": "system", "content": msg}

    def gen_user_prompt(self, msg):
        return {"role": "user", "content": msg}

    def gen_assistant_prompt(self, msg):
        return {"role": "assistant", "content": msg}

