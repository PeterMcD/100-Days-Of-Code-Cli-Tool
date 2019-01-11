import os
import subprocess
import datetime
import re
import shutil
import contextlib
from .Git import Git

days_of_code_remote = 'https://github.com/kallaway/100-days-of-code'
log_template = """### Day {0}: {1}

**Today's Progress** {2}

**Thoughts** {3}

**Link to work** [{4}]({5})"""


class DaysOfCodeException(Exception):
    pass


class DaysOfCode:
    __slots__ = ['_path', '_git']

    def __init__(self, path: str) -> None:
        self._check_path(path)
        self._git = Git(self._path)

    def start(self) -> None:
        self._set_existing_path()
        os.chdir(self._path)
        self._git.clone_remote(days_of_code_remote)
        self._clear_log()
        self._write_header_details()
        self._print_message(os.linesep +
                            'Congratulations, you are now ready to start the 100 Days Of Code challenge.' +
                            os.linesep + os.linesep +
                            'Good Luck' +
                            os.linesep
                            )

    def restart(self) -> None:
        self._delete_project()
        self.start()

    def new_day(self) -> None:
        log_file_path = os.path.join(self._path, '100-days-of-code', 'log.md')
        if not os.path.isfile(log_file_path):
            raise DaysOfCodeException('Log file does not exist.')
        current_date = datetime.datetime.now()
        day = self._get_next_day()
        date = '{}'.format(current_date.strftime('%B %d, %Y'))
        progress = input('What progress have you made today? ')
        while progress == '':
            progress = input('Please ensure you log your progress, no point keeping a journal otherwise: ')
        thoughts = input('What were the highlights (good or bad)? ')
        if thoughts == '':
            thoughts = input('No thoughts today? '
                             'Logging your thoughts can help identify what you need to work on at a later date: ')

        project_name = input('What is the name of the project you have been working on? ')
        while project_name == '':
            project_name = input('Your project needs a name, how else will you remember what you were working on? ')
        project_url = input('What is the URI for the project? ')
        if project_url == "":
            project_url = '#'
        log_entry = log_template.format(day, date, progress, thoughts, project_name, project_url)
        file = open(log_file_path, 'a')
        file.write('\r\n\r\n{}'.format(log_entry))
        file.close()
        os.chdir(os.path.join(self._path, '100-days-of-code'))
        self._git.add_file(repository='100-days-of-code')
        self._git.commit(repository='100-days-of-code', message='Day {} added'.format(day))
        self._print_message(os.linesep +
                            'Congratulations on completing day ' +
                            str(day) +
                            ' of your 100 Days of code challenge.' +
                            os.linesep
                            )

    def display_day(self, day: int = 0) -> None:
        regex_parse_day = r'### (?:Day )([0-9]*)(?::)([^*]*)(?:\s)' \
                          r'(?:\*\*Today\'s Progress\*\*)([^*]*)(?:\s)' \
                          r'(?:\*\*Thoughts\*\*)([^*]*)(?:\s)' \
                          r'(?:\*\*Link to work\*\*)([^#]*)'
        if day != 0:
            regex_parse_day = r'### (?:Day )({})(?::)([^*]*)' \
                              r'(?:\s)(?:\*\*Today\'s Progress\*\*)([^*]*)(?:\s)' \
                              r'(?:\*\*Thoughts\*\*)([^*]*)(?:\s)' \
                              r'(?:\*\*Link to work\*\*)([^#]*)'.format(day)
        days_matches = re.findall(regex_parse_day, self._get_log_content())
        for day_matches in days_matches:
            print('###### DAY {} ######'.format(day_matches[0]))
            print('Date: {}'.format(day_matches[1].rstrip()))
            print('Progress: {}'.format(day_matches[2].rstrip()))
            print('Thoughts: {}'.format(day_matches[3].rstrip()))
            print('Link to work: {}'.format(day_matches[4].rstrip()))
            print('')

    def edit_day(self, day) -> None:

        pass

    def end(self) -> None:
        pass

    def _check_path(self, path: str) -> None:
        path_input = os.path.expanduser(path)
        while not os.path.exists(path_input):
            path_input = input('The specified path does not exist (' + path_input + '): ')
            path_input = os.path.expanduser(path_input)
        self._path = path_input

    def _write_header_details(self) -> None:
        text = '# 100 Days Of Code - Log'
        log_file_path = os.path.join(self._path, '100-days-of-code', 'log.md')
        if not os.path.isfile(log_file_path):
            raise DaysOfCodeException('Log file does not exist.')
        file = open(file=log_file_path, mode='a')
        file.write(text)
        file.close()

    def _get_next_day(self) -> int:
        day = 1
        regex = r'(?:### Day )([0-9]+)'
        matches = re.findall(regex, self._get_log_content())
        if matches:
            day = int(matches[-1]) + 1
        return day

    @staticmethod
    def _get_existing_path() -> str:
        os.chdir(os.path.expanduser('~'))
        if not os.path.isfile('.100daysofcode'):
            raise DaysOfCodeException('No path identified. Have you started yet?')
        file = open(file='.100daysofcode', mode='r')
        path = file.read()
        file.close()
        return path

    def _set_existing_path(self) -> None:
        os.chdir(os.path.expanduser('~'))
        file = open(file='.100daysofcode', mode='a')
        file.write(self._path)
        file.close()

    def _clear_log(self) -> None:
        directory = os.path.join(self._path, '100-days-of-code')
        directory_with_file = os.path.join(self._path, '100-days-of-code', 'log.md')
        if not os.path.isfile(directory_with_file) and not os.path.isdir(directory):
            raise DaysOfCodeException('Directory for log file does not exist.')
        elif not os.path.isfile(directory_with_file):
            os.chdir(directory)
            subprocess.call(['touch', 'log.md'])
            return
        os.chdir(directory)
        with contextlib.suppress(FileNotFoundError):
            os.remove('log.md')
        subprocess.call(['touch', 'log.md'], shell=False)

    @staticmethod
    def _print_message(message: str, error: bool = False) -> None:
        if error:
            """Do something to change color"""
            pass
        print(message)

    def _delete_project(self) -> None:
        directory = os.path.join(self._path, '100-days-of-code')
        shutil.rmtree(directory)
        os.chdir(os.path.expanduser('~'))
        with contextlib.suppress(FileNotFoundError):
            os.remove('.100daysofcode')

    def _get_log_content(self) -> str:
        log_file_path = os.path.join(self._path, '100-days-of-code', 'log.md')
        file = open(log_file_path, 'r')
        log_text = file.read()
        file.close()
        return log_text
