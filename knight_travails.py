from collections import deque

class Board:
    def __init__(self, size):
        """Board with the specified size."""
        self.size = size

    def is_valid_move(self, move):
        x, y = move
        return 0 <= x < self.size and 0 <= y < self.size
    
class Knight:
    def __init__(self):
        self.POSSIBLE_MOVES = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]

def find_shortest_path(start, end):
    board = Board(8)
    knight = Knight()

    queue = deque()
    queue.append((start,[start]))     # Start from specified position
    visited = set()

    while queue:
        current_position, path = queue.popleft()
        if current_position == end:
            return path
        else:
            for move in knight.POSSIBLE_MOVES:
                new_x = current_position[0] + move[0]
                new_y = current_position[1] + move[1]
                if (new_x, new_y) not in visited and board.is_valid_move((new_x, new_y)):
                    queue.append(((new_x, new_y),(path + [(new_x, new_y)])))
                    visited.add((new_x, new_y))

    return path