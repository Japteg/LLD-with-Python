from abc import abstractmethod, ABCMeta


class CabSelectionStrategyInterface(metaclass = ABCMeta):
    
    @abstractmethod
    def select_cab(user, cabs):
        pass