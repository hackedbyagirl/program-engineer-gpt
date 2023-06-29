#!/usr/bin/python3

# Imports
import re
import questionary

from questionary import Style, ValidationError, Validator

from programengineergpt.utils.input import get_project_description
from programengineergpt.utils.colors import Color

## CLI Styler
custom_style = Style(
    [
        ("separator", "fg:#6C6C6C"),
        ("qmark", "fg:#FF9D00 bold"),
        ("question", "bold"),
        ("selected", "fg:#5F819D"),
        ("pointer", "fg:#FF9D00 bold"),
        ("choice", "fg:#FF9D00 bold"),
        ("answer", "fg:#5F819D bold"),
    ]
)


class CLI(object):
    """
    Initial CLI
    """

    def __init__(self):
        """Init Class"""
        self.mode = ""

    def launc_main_cli(self):
        """Launch main CLI"""

        while True:
            self.mode = questionary.rawselect(
                "Select Mode:",
                choices=["Analyze", "Develop", "Exit"],
                style=custom_style,
            ).ask()

            if self.mode == "Exit":
                break

            if self.mode == "Analyze":
                self.handle_analyze_mode()

            elif self.mode == "Develop":
                self.handle_develop_mode()

    def handle_analyze_mode(self):
        """
        Handles required parameters for this Analyze Mode
        """
        from programengineergpt.utils.display import Display

        Display.display_analyze_mode_description()
        method = questionary.rawselect(
            "Please select a method for how you would like to provide your code:",
            choices=["URL", "Directory Path", "Current directory", "Back"],
            style=custom_style,
        ).ask()

        if method == "Back":
            return

        # Handle the selected method
        if method == "URL":
            self.handle_url()

        elif method == "Directory Path":
            self.handle_path()

        elif method == "Current directory":
            self.handle_cwd()

        # elif method == "Local Index":
        #    self.handle_existing()

    def handle_develop_mode(self):
        """
        Handles the Develop New Program mode
        """
        from programengineergpt.utils.display import Display
        from programengineergpt.core.developer import Developer

        Display.display_develop_mode_description()  # Display the description

        # Get Project Name
        Color.print("\n{B}Step 1: {W}Please provide folder name for your project")
        project_name = input("Project Folder: ")

        # Get project Description
        Color.print(
            "\n{B}Step 2: {W}Please provide a description for your new project. Feel free to provide as much detail as possible about your project.You are able to enter multiple lines using the 'ENTER' button."
        )
        Color.print("{Y}NOTE: {W}Use Ctrl-D (or Ctrl-Z on Windows) when finished.")
        Color.print("\n\n{P}Project Description:\n")
        project_description = get_project_description()

        # Initialize Developer
        Developer(project_description, project_name)

    def handle_url(self):
        """
        Gets URL and sends to loader

        Args:
            self : Argument

        """
        from programengineergpt.agents.chatbot import ChatBot
        from programengineergpt.core.loader import CodeLoader

        repo_url = questionary.text(
            "Please provide a link to an online code repository",
            instruction="\n  Please use the following format\n  https://github.com/username/repo\n\n  URL: ",
            validate=URLValidator,
            style=custom_style,
        ).ask()

        loader = CodeLoader()
        vector_store = loader.load_online_repo(repo_url)
        chatbot = ChatBot(vector_store)
        chatbot.interact()

    def handle_path(self):
        """
        Gets Code Directory Path and sends to loader
        """

        from programengineergpt.agents.chatbot import ChatBot
        from programengineergpt.core.loader import CodeLoader

        dir_path = questionary.path(
            "Please provide the path to the code directory",
            only_directories=True,
            style=custom_style,
        ).ask()

        loader = CodeLoader()
        vector_store = loader.load_directory(dir_path)
        chatbot = ChatBot(vector_store)
        chatbot.interact()

    def handle_cwd(self):
        """
        Launches loader that handles current directory
        """
        from programengineergpt.agents.chatbot import ChatBot
        from programengineergpt.core.loader import CodeLoader

        loader = CodeLoader()
        vector_store = loader.load_current_directory()
        chatbot = ChatBot(vector_store)
        chatbot.interact()

    def handle_existing(self):
        """
        Handles and loads existing code index from deeplake
        """
        from programengineergpt.agents.chatbot import ChatBot
        from programengineergpt.core.retriever import Retriever

        Color.print("\n{Y}Please enter collection name for code base: ")
        col_name = input("Collection Name: ")

        index_retriever = Retriever(col_name)
        vector_store = index_retriever.retrive_code_index()
        chatbot = ChatBot(vector_store)
        chatbot.interact()


class URLValidator(Validator):
    """
    Validate URL for Input
    """

    def validate(self, document):
        """
        Args:
            self : Argument
            document : Argument

        """
        url_pattern = re.compile(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        )
        if not url_pattern.match(document.text):
            raise ValidationError(
                message="Please enter a valid URL", cursor_position=len(document.text)
            )  # Move cursor to end
