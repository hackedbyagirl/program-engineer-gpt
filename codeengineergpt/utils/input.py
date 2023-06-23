#!/usr/bin/python3

# Imports

def get_project_description():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    results = '\n'.join(lines)
    return results
