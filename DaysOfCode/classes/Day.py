from datetime import date
from typing import List
from DaysOfCode.classes.Link import Link


class Day:
    __slots__ = ['__day', '__date', '__progress', '__thoughts', '__links']

    def __init__(self, day: int, day_date: date, progress: str, thoughts: str, links: List[Link]):
        """
        Constructor
        :param day:
        :param day_date:
        :param progress:
        :param thoughts:
        :param links:
        """
        self.day = day
        self.dates = day_date
        self.progress = progress
        self.thoughts = thoughts
        self.__links = links

    # region Getters / Setters
    @property
    def dates(self) -> date:
        return self.__date

    @dates.setter
    def dates(self, day_date: date):
        if day_date and day_date is not None:
            self.__date = day_date
            return
        current_date = date.today()
        self.__date = current_date

    @property
    def day(self) -> int:
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day

    @property
    def progress(self) -> str:
        return self.__progress

    @progress.setter
    def progress(self, progress: str):
        self.__progress = progress

    @property
    def thoughts(self) -> str:
        return self.__thoughts

    @thoughts.setter
    def thoughts(self, thoughts: str):
        self.__thoughts = thoughts

    @property
    def link(self) -> Link:
        for i in [0, len(self.__links)]:
            yield self.__links[i]

    @link.setter
    def link(self, link: Link):
        self.__links.append(link)
    # endregion
