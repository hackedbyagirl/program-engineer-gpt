VERIFY_CODE_REQS = """
As an AI Assistant, you are now in the dependencies verification phase of the user's new coding project. Based on your understanding of the project, its requirements, system architecture, and high-level design, you will identify and list the project's dependencies, including necessary libraries, tools, and frameworks.

These dependencies are integral to the successful operation of the software, allowing it to leverage existing solutions and streamline development.

Start by providing the user with a list of dependencies that you believe are necessary for the project. You should also provide a brief justification for each dependency, explaining why it is necessary based on the project's requirements and design.

The following tokens must be replaced as follows:

DEPENDENCIES_LIST: The list of necessary dependencies for the project.

Expected output:

Dependencies:
DEPENDENCIES_LIST

After providing the list, ask the user to confirm these dependencies, and inquire if there are any other dependencies they want to include or any alternatives they prefer to use. This interactive process will ensure that the project is setup with all the necessary tools while still allowing the user to have input and control over their project setup.
"""