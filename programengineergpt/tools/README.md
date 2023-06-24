# Agent Tools
## Current
1. `CodeLoaderTool`: This tool is responsible for loading code from a given repository. It takes a repository URL or local path as input and returns a list of loaded code files.
2. `CodeAnalyzerTool`: This tool takes a question and the code embeddings as input and uses a language model to generate an answers to the question based on the code.
3. `CodeWriterTool`: This tool takes a coding task or goal as input and use a language model to generate code that accomplishes the task or goal. It could also use the code embeddings as context to generate code that is consistent with the existing codebase.

## Future
1. `CodeTesterTool`: This tool would automatically generate unit tests for the generated code. This would help ensure that the code is functioning as expected.
2. `CodeDocumentationTool`: This tool would automatically generate documentation for the generated code. It could use comments in the code and the structure of the code to generate useful documentation.
3. `CodeDependencyTool`: This tool would analyze the code to determine its dependencies. It could provide information about which libraries and packages the code depends on, and could potentially even automatically install these dependencies.