from abc import abstractmethod

from OTLClasses.Verification.RelatieObject import RelatieObject


class NietDirectioneleRelatie(RelatieObject):
    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)