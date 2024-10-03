class GoBoard:
    def __init__(self, size=19):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.current_player = 'black'

    def place_stone(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player
        captured = self.check_captures(row, col)
        self.remove_captured_stones(captured)

        self.current_player = 'white' if self.current_player == 'black' else 'black'
        return True

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.board[row][col] is not None:
            return False
        # TODO: Implement ko rule and suicide rule
        return True

    def check_captures(self, row, col):
        captured = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size:
                group = self.get_group(r, c)
                if group and all(self.board[i][j] != None for i, j in group):
                    captured.extend(group)
        return captured

    def get_group(self, row, col):
        color = self.board[row][col]
        if color is None:
            return []

        group = set()
        to_check = [(row, col)]

        while to_check:
            r, c = to_check.pop()
            if (r, c) in group:
                continue
            group.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == color:
                    to_check.append((nr, nc))

        return list(group)

    def remove_captured_stones(self, captured):
        for row, col in captured:
            self.board[row][col] = None

    def print_board(self):
        for row in self.board:
            print(' '.join('.' if stone is None else 'B' if stone == 'black' else 'W' for stone in row))
        print()

# Example usage
if __name__ == "__main__":
    board = GoBoard(size=9)  # Create a 9x9 board for this example
    board.place_stone(2, 2)  # Black
    board.place_stone(3, 3)  # White
    board.place_stone(2, 3)  # Black
    board.place_stone(3, 2)  # White
    board.print_board()