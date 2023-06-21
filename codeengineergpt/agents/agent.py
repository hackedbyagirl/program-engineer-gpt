class CustomAgent:
    def __init__(self, model, conversation_chain, prompt_template, output_parser):
        self.model = model
        self.conversation_chain = conversation_chain
        self.prompt_template = prompt_template
        self.output_parser = output_parser

    def ask_question(self, question):
        # Use the conversation chain to find relevant parts of the conversation
        relevant_parts = self.conversation_chain.find_relevant_parts(question)

        # Format the question and relevant parts into a prompt for the model
        prompt = self.prompt_template.format_prompt(question, relevant_parts)

        # Use the model to generate a response to the prompt
        response = self.model.generate_response(prompt)

        # Parse the model's output using the output parser
        parsed_output = self.output_parser.parse(response)

        return parsed_output
