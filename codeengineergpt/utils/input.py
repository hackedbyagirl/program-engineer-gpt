#!/usr/bin/python3

# Imports

def get_project_description():
    lines = []
    print("Please enter your project description. You can enter multiple lines. When you're done, press Ctrl-D (or Ctrl-Z on Windows).")
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    results = '\n'.join(lines)
    return results
