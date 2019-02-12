import random
import numpy as np


# Keys store casting possibilities
# First list entry is the cost in lots (how many lots to construct the cast)
# Second list entry is the relative probability
# Purposely omitted: V, ^, N, W, T, L, H, A, [, ]
castings = {
    '|': [1, 1],
    '/': [1, 1],
    '\\': [1, 1],
    '_': [1, 1],
    '-': [1, 1],
    '<': [2, 0.15],
    '>': [2, 0.15],
    '+': [2, 0.1],
    '=': [2, 0.1],
    'X': [2, 0.1],
    'Z': [3, 0.02],
    'Y': [3, 0.02],
    'E': [4, 0.02],
    '#': [4, 0.001],
}

# Normalize probabilities
probabilities = [castings[cast][1] for cast in castings]
probabilities = [i / sum(probabilities) for i in probabilities]


class Lots:
    def __init__(self, num_lots=10):
        if num_lots < 1 or not isinstance(num_lots, int):
            raise ValueError('number of lots must be positive integer')
        self.num_lots = num_lots
        self.neatlots = '|' * num_lots
        print('\n' + self.neatlots + '\n')

    def cast(self):
        self.lots = self._decidelots()
        grid_side = self._gridsize()

        # Add an appropriate number of empty grid slots
        self.lots += [' '] * (grid_side ** 2 - len(self.lots))
        random.shuffle(self.lots)

        # Display the lots
        for i in range(grid_side):
            print("".join(self.lots[(i * grid_side):(i * grid_side + grid_side)]))

    def uncast(self):
        print('\n' + self.neatlots + '\n')

    def _decidelots(self):
        # Decide which lot shapes to use, picking until there are no lots left
        # Returns a list of the chosen lot shapes
        lots = []
        remaining_lots = self.num_lots
        while remaining_lots > 0:
            possible_castings = list(castings.keys())
            cast = np.random.choice(possible_castings, p=probabilities)
            remaining_lots -= castings[cast][0]
            if remaining_lots >= 0:  # Enough lots remaining
                lots.append(cast)
            else:  # Not enough lots remaining
                remaining_lots += castings[cast][0]
        return lots

    def _gridsize(self):
        # Decide how big the (square) grid should be
        # Returns the side length of the grid

        # At least 2/3 of the spaces will be empty
        singleside = int(np.ceil(np.sqrt(self.num_lots * 3)))
        return singleside


if __name__ == '__main__':
    test = Lots(50)
    test.cast()
    test.uncast()
