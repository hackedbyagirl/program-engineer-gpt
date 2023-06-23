def get_project_description():
    lines = []
    print("Please enter your project descrition")
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    results = '\n'.join(lines)
    print(results)

get_project_description()