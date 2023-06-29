#!/usr/bin/env python3

import os
from programengineergpt.utils.colors import Color


class CodeEmbedder:
    def __init__(self):
        pass

    @staticmethod
    def remove_temp_dir(self):
        """
        Remove 'temp_repo' if a repository was cloned
        """
        if os.path.exists("temp_repo"):
            Color.print('{G}Step 5: {W}Removing "temp_repo" contents')
            os.system("rm -rf temp_repo")
