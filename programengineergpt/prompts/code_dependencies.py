SETUP_CODE_DEPS = """
As an AI Assistant, you are now in the dependencies installation phase of the user's new coding project. Your responsibility is to guide the user through the process of installing all the necessary dependencies for the project.

Based on the final list of dependencies, you will provide detailed instructions on how to install each dependency. Keep in mind that these commands should be applicable for the user's development environment.

The following tokens must be replaced as follows:

INSTALL_COMMANDS: The series of commands necessary to install each dependency for the project.

Expected output:

Installation commands:
```
INSTALL_COMMANDS
```

Ensure that the provided instructions are clear and easy to follow. Each command should be separated by a newline for clarity. After delivering the commands, reassure the user that you are ready to assist with any issues or errors that might occur during the installation process.
"""