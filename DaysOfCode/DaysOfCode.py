import os
import subprocess
import datetime
import re
import shutil
from .Git import Git

days_of_code_remote = 'https://github.com/kallaway/100-days-of-code'
log_template = """### Day {0}: {1}

**Today's Progress**: {2}

**Thoughts:** {3}

**Link to work:** [{4}]({5})"""


class DaysOfCodeException(Exception):
    pass


class DaysOfCode:
    _path: str = ''

    def __init__(self, path: str):
        self._check_path(path)

    def start(self):
        self._set_existing_path()
        os.chdir(self._path)
        git = Git.Git(self._path)
        git.clone_remote(days_of_code_remote)
        self._clear_log()
        self._write_header_details()
        self._print_message(os.linesep +
                            'Congratulations, you are now ready to start the 100 Days Of Code challenge.' +
                            os.linesep + os.linesep +
                            'Good Luck' +
                            os.linesep
                            )

    def restart(self):
        self._delete_project()
        self.start()

    def new_day(self):
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
        subprocess.call(['git', 'add'],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        subprocess.call(['git', 'commit', '-m', 'Day {} added'.format(day)],
                        shell=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        self._print_message(os.linesep +
                            'Congratulations on completing day ' +
                            str(day) +
                            ' of your 100 Days of code challenge.'+
                            os.linesep
                            )

    def end(self):
        pass

    def _check_path(self, path: str):
        path_input = os.path.expanduser(path)
        while not os.path.exists(path_input):
            path_input = input('The specified path does not exist (' + path_input + '): ')
            path_input = os.path.expanduser(path_input)
        self._path = path_input

    def _write_header_details(self):
        text = '# 100 Days Of Code - Log'
        log_file_path = os.path.join(self._path, '100-days-of-code', 'log.md')
        if not os.path.isfile(log_file_path):
            raise DaysOfCodeException('Log file does not exist.')
        file = open(file=log_file_path, mode='a')
        file.write(text)
        file.close()

    def _get_next_day(self) -> int:
        day = 1
        log_file_path = os.path.join(self._path, '100-days-of-code', 'log.md')
        file = open(log_file_path, 'r')
        log_text = file.read()
        file.close()
        regex = '(?:### Day )([0-9]+)'
        matches = re.findall(regex, log_text)
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

    def _set_existing_path(self):
        os.chdir(os.path.expanduser('~'))
        subprocess.call(['touch', '.100daysofcode'])
        file = open(file='.100daysofcode', mode='w')
        file.write(self._path)
        file.close()

    def _clear_log(self):
        directory = os.path.join(self._path, '100-days-of-code')
        directory_with_file = os.path.join(self._path, '100-days-of-code', 'log.md')
        if not os.path.isfile(directory_with_file) and not os.path.isdir(directory):
            raise DaysOfCodeException('Directory for log file does not exist.')
        elif not os.path.isfile(directory_with_file):
            os.chdir(directory)
            subprocess.call(['touch', 'log.md'])
            return
        os.chdir(directory)
        os.remove('log.md')
        subprocess.call(['touch', 'log.md'], shell=False)

    @staticmethod
    def _print_message(message: str, error: bool = False):
        if error:
            """Do something to change color"""
            pass
        print(message)

    def _delete_project(self):
        directory = os.path.join(self._path, '100-days-of-code')
        shutil.rmtree(directory)
        os.chdir(os.path.expanduser('~'))
        os.remove('.100daysofcode')
