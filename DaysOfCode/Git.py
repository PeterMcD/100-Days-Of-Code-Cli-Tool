import subprocess
import os


class GitException(Exception):
    pass


class Git:
    __slots__ = ['_path']

    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            raise GitException('Given path is not available')
        self._path = path

    def clone_remote(self, url: str) -> None:
        os.chdir(self._path)
        subprocess.call(['git', 'clone', url], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    def push(self, repository: str) -> None:
        if not os.path.exists(os.path.join(self._path, repository)):
            raise GitException('Given path is not available')
        os.chdir(os.path.join(self._path, repository))
        subprocess.call(['git', 'push', ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    def add_file(self, repository: str) -> None:
        os.chdir(os.path.join(self._path, repository))
        subprocess.call(['git', 'add'],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    def commit(self, repository: str, message: str = '') -> None:
        os.chdir(os.path.join(self._path, repository))
        subprocess.call(['git', 'commit', '-m', message],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
