from user import User
from random import random


class SimulationGenerator:
    users = []
    #retention = []
    initial_amount = 1000

    def __init__(self, retention):
        self.retention = retention

        for x in range(0, self.initial_amount):
            new_user = User()
            new_user.idle = random.random() < retention
            self.users.append(new_user)

    def tick(self):
        users_leaving = []

        for user in self.users:
            if user.is_ready_to_leave():
                users_leaving.append(user)

        for user in users_leaving:
            user.idle = True

    def add_random_opponent_to_players(self):

        for user in self.users:
            random_opponents = random.sample[self.users, 8]

            for opponent in random_opponents:
                user.add_opponent(opponent)

    def amount_of_players_active(self):
        amount = 0
        for user in self.users:
            if not user.idle :
                amount +=1

        return amount
