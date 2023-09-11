from abc import *


class AbstractConnectionCreator(metaclass=ABCMeta):
    @abstractmethod
    def get_connection(self):
        pass
