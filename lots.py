import random


possible_castings = ['|', '/', '\\', '_', '-']

class Lots:
    def __init__(self, num_lots=5):
        self.num_lots = num_lots
        self.lots = ['|'] * self.num_lots
    
    def cast(self):
        self.lots = [random.choice(possible_castings) for i in range(self.num_lots)]

    def uncast(self):
        self.lots = ['|'] * self.num_lots

    def print_lots(self):
        print("".join(self.lots))
