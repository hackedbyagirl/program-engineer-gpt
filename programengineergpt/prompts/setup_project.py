# Project Setup Prompt

PROJECT_SETUP = """
You will now begin code generation for the project. Based on the description of the project, you will think step by step and reason yourself to the right decisions of building this program to get it right. You will follow best practices for the requested languages in terms of describing the code written as a defined package/project.

You will first lay out the names of the core classes, functions, methods that will be necessary, as well as a quick comment on their purpose.
Then you will output the content of each file including ALL code. Each file must strictly follow a markdown code block format.
The following tokens must be replaced as follows.

FILENAME will be the filename in all lowercasem including the file extension
LANG will be the markup code block language for the code's language
CODE will be the code

Expected output:

FILENAME
```LANG
CODE
```

The code should be fully functional and contain no placeholders.

You will begin with the "entrypoint" file, then you will go to the ones that are imported by that file, and so on.
You will ensure to use best practice for file naming conventions based on the language and framework.
Ensure that all files are compatible with each other and contain all imports, types, etc. required.
Before you finish, double check that all parts of the architecture are present in the files to ensure that the user has a solid foundation to start their new project.
"""
