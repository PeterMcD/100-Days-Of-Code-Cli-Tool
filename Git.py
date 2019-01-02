import subprocess
import os


class GitException(Exception):
    pass


class Git:
    _path: str = ''

    def __init__(self, path: str):
        if not os.path.exists(path):
            raise GitException('Given path is not available')
        self._path = path

    def clone_remote(self, url: str):
        os.chdir(self._path)
        subprocess.call(['git', 'clone', url], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    def push(self, repository: str):
        if not os.path.exists(os.path.join(self._path, repository)):
            raise GitException('Given path is not available')
        os.chdir(os.path.join(self._path, repository))
        subprocess.call(['git', 'push', ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
