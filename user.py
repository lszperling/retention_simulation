class User:
    opponents = []
    cap = 8
    idle = False

    def __init__(self):

        self.opponents = []

    def add_opponent(self, opponent):
        if self.can_add_opponent() and self != opponent:
            if opponent.add_opponent_back(self):
                self.opponents.append(opponent)

        else:
            return False

    def add_opponent_back(self, opponent):
        if(self.can_add_opponent() and
               not opponent in self.opponents):
            self.opponents.append(opponent)
            return True
        else:
            return False

    def can_add_opponent(self):
        return self.opponents.__len__() < self.cap

    def set_idle(self, value):
        self.idle = value

    def count_idle_opponents(self):
        i = 0

        for opponent in self.opponents:
            if opponent.idle:
                i += 1

        return i

    def is_ready_to_leave(self):
        idle_opponents = 0
        for opponent in self.opponents:
            if opponent.idle:
                idle_opponents += 1

        return idle_opponents == 8