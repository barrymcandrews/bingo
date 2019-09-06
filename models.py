import random
from typing import List


class Board:

    def __init__(self, options: List[str]):
        list_copy = options.copy()
        self.cells = []

        # Populate cells array
        for i in range(0, 5):
            columns = []
            for j in range(0, 5):
                if i == 2 and j == 2:
                    columns.append('Free Space')
                else:
                    random.shuffle(list_copy)
                    columns.append(list_copy.pop())
            self.cells.append(columns)
