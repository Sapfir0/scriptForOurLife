from abc import ABC, abstractmethod


class browser(ABC):
    profilesDir = None

    @abstractmethod
    def findProfilesDir(self):
        pass
