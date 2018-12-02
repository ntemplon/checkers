import abc


class Controller:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def select_move(self, board, team, allowable_moves):
        pass


class PlayerController(Controller):
    def __init__(self):
        super().__init__()

    def select_move(self, board, team, allowable_moves):
        return None


class AIController(Controller):
    def __init__(self):
        super().__init__()

    def select_move(self, board, team, allowable_moves):
        return None
