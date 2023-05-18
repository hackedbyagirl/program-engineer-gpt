from langchain.document_loaders import DirectoryLoader

def load_and_index_files(repo_path):
    extensions = ['txt', 'md', 'markdown', 'py', 'js', 'java', 'c', 'cpp', 'cs', 'go', 'rb', 'php', 'scala', 'html', 'htm', 'xml', 'json', 'yaml', 'yml', 'ini', 'toml', 'cfg', 'conf', 'sh', 'bash', 'css', 'scss', 'sql', 'gitignore', 'dockerignore', 'editorconfig']

    file_type_counts = {}
    documents_dict = {}

    for ext in extensions:
        glob_pattern = f'**/*.{ext}'
        loader = DirectoryLoader(repo_path, glob=glob_pattern)
        docs = loader.load()
        print(ext)
        print(len(docs))
            
            
            
