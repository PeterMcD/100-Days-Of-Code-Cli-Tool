

class Link:
    __slots__ = ['__title', '__destination']

    def __init__(self, title: str, destination: str):
        self.title = title
        self.destination = destination

    # region Getters / Setters
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def destination(self) -> str:
        return self.__destination

    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination
    # endregion

    def __str__(self):
        return '[{}]({})'.format(self.__title, self.__destination)
