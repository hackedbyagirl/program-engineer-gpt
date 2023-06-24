# ProgramEngineerGPT
ProgramEngineerGPT is an AI-powered tool designed to assist developers with code comprehension, exploration, and generation. It provides two main modes of operation: Analyze Mode and Develop Mode.

## Modes of Operation

### Analyze Mode

In the 'Analyze' mode, ProgramEngineerGPT will thoroughly examine a provided code repository. You will be engaged in an interactive chat session where you can pose queries about the codebase. This could include questions about its structure, dependencies, functions, or any other aspect. The AI will respond with insights, helping you gain a deeper understanding of the code repository.

### Develop Mode

In the 'Develop' mode, ProgramEngineerGPT can assist you in setting up a new coding project. This includes planning the project structure, setting up the development environment, and other setup tasks. You will enter an interactive session where you will provide a project description of the program/project you want to create. After you provide a project description, the AI system will ask further questions to gather more information about your project. Your responses will guide the AI in providing the best assistance for your project.

## Requirements
- [Deeplake Account](https://app.activeloop.ai/register/)
- [OpenAI Account](https://openai.com/)

## Installation
Install all the required packages
```
python3 -m pip install -r requirements.txt
```

## Usage

You can start using ProgramEngineerGPT by running the main script and selecting the mode of operation. Depending on the mode, you will be asked to provide further details such as the code repository URL or the project description.

However, this program does depend on API keys. You can set these API keys using environmental variables

### ENV Variable
First, change the `test.env` to `.env` and add the required environmental variables. If you would like to export them locally, please use the following keys.

```bash
export OPENAI_API_KEY="<OPENAI_API_KEY>"
export ACTIVELOOP_TOKEN="<ACTIVELOOP_API_KEY>"
export DEEPLAKE_ACCOUNT_NAME="<DEEPLAKE_ACCOUNT_NAME>"
```

### Launch
```bash
python3 programengineergpt.py 
```

## Contributing

Contributions are welcome! Please refer to the contributing guide provided in the repository.

## License

Please refer to the license file provided in the repository.
