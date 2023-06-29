# file_processing.py

# File extensions to consider
extensions_include = [
    "bash",
    "cfg",
    "conf",
    "cpp",
    "cs",
    "css",
    "dockerignore",
    "editorconfig",
    "gitignore",
    "go",
    "html",
    "htm",
    "ini",
    "java",
    "javascript",
    "json",
    "js",
    "markdown",
    "md",
    "php",
    "py",
    "rb",
    "scala",
    "scss",
    "sh",
    "sql",
    "toml",
    "txt",
    "xml",
    "yaml",
    "yml",
]

# File extensions to ignore
extensions_ignore = [
    "*.py[cod]",  # Byte-compiled / optimized / DLL files
    "*$py.class",  # Byte-compiled / optimized / DLL files
    "*.egg",  # Distributions and packaging
    "*.egg-info",  # Distributions and packaging
    "*.chroma",  # Chroma
    "*.env",  # ENV variables
]

# Directories to ignore
dirs_ignore = [
    "__pycache__",  # Byte-compiled / optimized / DLL files
    ".pytest_cache",  # Byte-compiled / optimized / DLL files
    "venv",  # Virtual Environments
    ".Python",  # Distribution / packaging
    "build",  # Distribution / packaging
    "develop-eggs",  # Distribution / packaging
    "dist",  # Distribution / packaging
    "downloads",  # Distribution / packaging
    "eggs",  # Distribution / packaging
    ".eggs",  # Distribution / packaging
    "lib",  # Distribution / packaging
    "lib64",  # Distribution / packaging
    "parts",  # Distribution / packaging
    "sdist",  # Distribution / packaging
    "var",  # Distribution / packaging
    "wheels",  # Distribution / packaging
    "share/python-wheels",  # Distribution / packaging
    "*.egg-info",  # Distribution / packaging
    ".installed.cfg",  # Distribution / packaging
    "MANIFEST",  # Distribution / packaging
    ".chroma",  # Chroma
]