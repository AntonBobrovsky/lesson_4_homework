class LionStates:
    def __init__(self, state):
        self.action = ""
        if state.lower() == "сытый" or state.lower() == "голодный":
            self.state = state
        else:
            raise ValueError("Неверное состояние !")

    def implementation_fsm(self, symbol):
        if symbol == "антилопа":
            self.__antelope()
        elif symbol == "охотник":
            self.__hunter()
        elif symbol == "дерево":
            self.__tree()

    def __antelope(self):
        if self.state == "сытый":
            self.action = "спать"
            self.state = "голодный"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())
        elif self.state == "голодный":
            self.action = "съесть"
            self.state = "сытый"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

    def __hunter(self):
        if self.state == "сытый":
            self.action = "убежать"
            self.state = "голодный"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())
        elif self.state == "голодный":
            self.action = "убежать"
            self.state = "голодный"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

    def __tree(self):
        if self.state == "сытый":
            self.action = "смотреть"
            self.state = "голодный"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())
        elif self.state == "голодный":
            self.action = "спать"
            self.state = "голодный"
            print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())
