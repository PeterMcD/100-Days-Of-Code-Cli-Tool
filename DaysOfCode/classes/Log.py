import re
from datetime import datetime
from DaysOfCode.classes.Day import Day

Title_Regex = r'### (?:Day )([0-9]*)(?::)([^*]*)(?:\s)' \
                  r'(?:\*\*Today\'s Progress\*\*)([^*]*)(?:\s)' \
                  r'(?:\*\*Thoughts\*\*)([^*]*)(?:\s)' \
                  r'(?:\*\*Link to work\*\*)([^#]*)'

Days_Regex = r'### (?:Day )([0-9]*)(?::)([^*]*)(?:\s)' \
                  r'(?:\*\*Today\'s Progress\*\*)([^*]*)(?:\s)' \
                  r'(?:\*\*Thoughts\*\*)([^*]*)(?:\s)' \
                  r'(?:\*\*Link to work\*\*)([^#]*)'


class Log:
    __slots__ = {'__title', '__days', '__log_handler'}

    def __init__(self, logfile: str):
        self.__title = ''
        self.__days = []
        self.__parse_log_file(logfile)
        pass

    def add_day(self, day: Day):
        self.__days[len(self.__days)] = day

    def empty_log(self):
        self.title = ''
        self.__days = []

    def write_log(self):
        self.__log_handler.write(self.__compile_log())

    # region Getters/Setters
    @property
    def days(self) -> str:
        for i in [0, len(self.__days)]:
            yield self.__days[i]

    @property
    def next_day_number(self) -> int:
        return len(self.__days) + 1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str = '100 Days Of Code - Log'):
        self.__title = title

    # endregion

    # region private methods
    def __parse_log_file(self, logfile: str):
        self.__log_handler = open(logfile, mode='w')
        log_content = self.__log_handler.read()
        day_regex_matches = re.findall(Days_Regex, log_content)
        for day_matches in day_regex_matches:
            days_date = datetime.strptime(day_matches[1].rstrip(), '%B %d, %Y')
            day = Day(day=day_matches[0],
                      day_date=days_date.date(),
                      progress=day_matches[2].rstrip(),
                      thoughts=day_matches[3].rstrip(),
                      links=day_matches[4].rstrip(),
                      )
            self.add_day(day)

    def __compile_log(self) -> str:
        content: str = ''
        title: str = '# {}' \
                     ''.format(self.title)
        content += title
        for day in self.__days:
            links = []
            for link in day.link:
                link_details = '[{}]({})'.format(link.title, link.destination)
                links.append(link_details)
            links_details = "" \
                            "* {}".join(links)
            day_details = "" \
                          "" \
                          "### Day {}: {}" \
                          "" \
                          "** Today's Progress**: {}" \
                          "" \
                          "** Thoughts: ** {}" \
                          "" \
                          "** Link to work: ** {}".format(day.day,
                                                          day.date,
                                                          day.progress,
                                                          day.thoughts,
                                                          links_details
                                                          )
            content += day_details
        return content

    def __del__(self):
        self.__log_handler.close()
    # endregion
