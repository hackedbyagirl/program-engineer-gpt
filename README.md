# CodeAssistantGPT
CodeAssistantGPT is an AI-powered tool designed to assist developers with enhanced comprehension and exploration capabilities of code repositories. It incorporates several technologies, including VectorStores, LangChains Conversational RetrieverChain, and OpenAI's GPT-4 language model. With these capabilities, CodeAssistantGPT can effectively respond to inquiries about code within a GitHub or local repository and generate new code.

To achieve this, the tool follows a systematic process. Firstly, it loads and thoroughly analyzes the provided code, breaking it down into smaller, manageable sections. Then, it converts these sections into a vector space, enabling semantic analysis. Finally, it employs a language model to generate accurate responses to code-related questions.

## Features
* Load and analyze code from a GitHub or local repository.
* Split code into manageable chunks for analysis.
* Embed code chunks into a vector space for semantic analysis.
* Use OpenAI's GPT language model to answer questions about the code.

## Requirements
TBD

## Installation
```
python3 -m pip install -r requirements.txt
```

## Usage
To use CodeAssistantGPT, there are two modules, `load` and `analyze`. The `load` module takes a code repository and creates an index that can be used to for further analysis. The `analyze` module allows you to ask question about any codebase that you have indexed. 

### Load Module:
Load a codebase repository from githuib or a local repository.

**Example**:
```
python3 ca_gpt.py load --repository <repository_url> --index <index_name>
```
**Arguments**:
* `--repository`: This argument specifies the URL of the GitHub repository or the path of the local repository to analyze.
* `--index`: This argument specifies the name of the Index you want the code to be stored at.
* `--chunk_size`: This argument specifies the size of the chunks to split the code into for analysis. The default value is 1000.
* `--embedding_size`: This argument specifies the size of the embeddings to use for semantic analysis. The default value is 1536.

### Analyze Module:
Have a conversation with your code uploaded to the Deeplake Index

**Example**:
```
python3 ca_gpt.py analyze --dataset <dataset_name>
```
**Arguments**:
* `--dataset`: This argument specifies the name of your dataset index.
* `--model`: This argument specifies the name of the GPT model to use for answering questions. The default value is 'gpt-3.5-turbo'.


## Documentation
For more detailed information about the API, please see documentation located in the `docs` directory.

