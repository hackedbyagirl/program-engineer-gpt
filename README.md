<h1 align="center">ProgramEngineerGPT</h1>

<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=400px src="https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/kat.png" alt="Kitty Kitty Meow Moew"></a>
</p>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-green)](https://github.com/hackedbyagirl/ProgramEngineerGPT) 
  [![GitHub Issues](https://img.shields.io/github/issues/hackedbyagirl/ProgramEngineerGPT)](https://github.com/hackedbyagirl/ProgramEngineerGPT/issues)
  [![Twitter Follow](https://img.shields.io/twitter/follow/hackedbyagirl?style=social)](https://twitter.com/hackedbyagirl)

</div>

---

<p align="center">ProgramEngineerGPT is an interactive command line tool that leverages the power of AI to assist developers with code comprehension, exploration, and generation. It serves as a virtual assistant that can analyze codebases, answer queries about code, and even help in setting up new coding projects.
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Examples](#examples)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>
ProgramEngineerGPT is an AI-powered tool designed to assist developers with code comprehension, exploration, and generation. ProgramEngineerGPT can be used as a comprehensive developer's assistant that can understand code at a deep level and can provide valuable insights and assistance. Whether you're trying to understand a complex codebase or starting a new project, ProgramEngineerGPT can be run using two modes of operation
- Analyze Mode
- Develop Mode.

**Analyze Mode**

In the 'Analyze' mode, ProgramEngineerGPT will thoroughly examine a provided code repository. You will be engaged in an interactive chat session where you can pose queries about the codebase. This could include questions about its structure, dependencies, functions, or any other aspect. The AI will respond with insights, helping you gain a deeper understanding of the code repository and how it funtions.

**Develop Mode**

In the 'Develop' mode, ProgramEngineerGPT can assist you in setting up a new coding project. This includes planning the project structure, setting up the development environment, and other setup tasks. You will enter an interactive session where you will provide a project description of the program/project you want to create. After you provide a project description, the AI system will ask further questions to gather more information about your project. Your responses will guide the AI in providing the best assistance for your project.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running for development and testing purposes.

### Prerequisites
- [Deeplake Account](https://app.activeloop.ai/register/)
- [OpenAI Account](https://openai.com/)

### Setup
Instructions on how to get ProgramEngineerGPT configured locally.

Before running, it is important that you have the correct environmental variables set. 
Setup required Environmental Variables. You can either change the `test.env` to `.env` and add the required environmental variables.

If you would like to export them locally, please use the following keys.

Linux or MacOS
```bash
# OpenAI API
export OPENAI_API_KEY="<OPENAI_API_KEY>"

# Deeplake API
export ACTIVELOOP_TOKEN="<ACTIVELOOP_API_KEY>"
export DEEPLAKE_ACCOUNT_NAME="<DEEPLAKE_ACCOUNT_NAME>"
```
Windows

```bash 
# OpenAI API
setx OPENAI_API_KEY <OPENAI_API_KEY>

# Deeplake API
setx ACTIVELOOP_TOKEN <ACTIVELOOP_API_KEY>
setx DEEPLAKE_ACCOUNT_NAME <DEEPLAKE_ACCOUNT_NAME>
```

**pip package**
```bash
pip install pgpt
```

**local package**
Clone the repository
```bash
#Download Repo and Navigate to Directory
git clone https://github.com/hackedbyagirl/ProgramEngineerGPt.git
cd ProgramEngineerGPT
pip install -e .
pgpt
```

**python program**
Clone the repository
```bash
#Download Repo and Navigate to Directory
git clone https://github.com/hackedbyagirl/ProgramEngineerGPt.git
cd ProgramEngineerGPT
```
Install all the required packages
```
python3 -m pip install -r requirements.txt
```


## Usage <a name="usage"></a>
You can start using ProgramEngineerGPT by running the main script and selecting the mode of operation. Depending on the mode, you will be asked to provide further details such as the code repository URL or the project description.

However, this program does depend on API keys so make sure to set them!

```bash
# Python package
pgpt

# Python program
python3 programengineergpt.py 
```

## Examples <a name="examples"></a>
### Program Launch
Main Program Home Screen

![main](https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/pgpt.jpg)

### Analyze Mode
Loading Code of Current Working Directory

![cwd](https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/cwd.jpg)

Engaging in conversation about the code

![chat](https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/chat.jpg)

### Develop Mode
Providing Developer Mode with a Project Description

![dev](https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/dev-launch.jpg)

Engaging with Developer AI Assistant

![dev2](https://github.com/hackedbyagirl/ProgramEngineerGPT/blob/main/imgs/dev-gen.jpg)

## Contributing

Contributions are welcome! Please refer to the contributing guide provided in the repository.

## License

Please refer to the license file provided in the repository.

## Acknowledgements <a name = "acknowledgement"></a>
Inspiration
- [engineer-gpt](https://github.com/AntonOsika/gpt-engineer)