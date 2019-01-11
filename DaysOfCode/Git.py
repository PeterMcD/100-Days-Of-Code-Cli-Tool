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
        subprocess.call(['git', 'clone', url, '--work-tree', self._path, ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    def push(self, repository: str) -> None:
        path = os.path.join(self._path, repository)
        if not os.path.exists(path):
            raise GitException('Given repository is not available')
        subprocess.call(['git', 'push', '--work-tree', path, ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    def add_file(self, repository: str) -> None:
        path = os.path.join(self._path, repository)
        if not os.path.exists(path):
            raise GitException('Given repository is not available')
        subprocess.call(['git', 'add', '--work-tree', path, ],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    def commit(self, repository: str, message: str = '') -> None:
        path = os.path.join(self._path, repository)
        if not os.path.exists(path):
            raise GitException('Given repository is not available')
        subprocess.call(['git', 'commit', '-m', message, '--work-tree', path, ],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
