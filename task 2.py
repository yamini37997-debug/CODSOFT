from enum import Enum

class Mark(Enum):
    X = "X"
    O = "O"

class Grid:
    def __init__(self):
        self.cells = [" "] * 9

    def place_mark(self, index, mark):
        if self.cells[index] == " ":
            self.cells[index] = mark.value
            return True
        return False

 class GameState:
    def __init__(self, grid, current_player):
        self.grid = grid
        self.current_player = current_player

    def check_winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.grid.cells[a] == self.grid.cells[b] == self.grid.cells[c] != " ":
                return self.grid.cells[a]
        if " " not in self.grid.cells:
            return "Tie"
        return None
def minimax(state, depth, is_maximizing):
    winner = state.check_winner()
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Tie": return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if state.grid.cells[i] == " ":
                state.grid.cells[i] = "O"
                score = minimax(state, depth+1, False)
                state.grid.cells[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if state.grid.cells[i] == " ":
                state.grid.cells[i] = "X"
                score = minimax(state, depth+1, True)
                state.grid.cells[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(state):
    move = None
    best_score = -float("inf")
    for i in range(9):
        if state.grid.cells[i] == " ":
            state.grid.cells[i] = "O"
            score = minimax(state, 0, False)
            state.grid.cells[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def render(grid):
    print("\n")
    for i in range(0, 9, 3):
        print(grid.cells[i:i+3])
    print("\n")
def play():
    grid = Grid()
    state = GameState(grid, "X")

    while True:
        render(grid)
        winner = state.check_winner()
        if winner:
            print("Winner:", winner)
            break

        if state.current_player == "X":
            move = int(input("Enter move (0-8): "))
            if grid.place_mark(move, Mark.X):
                state.current_player = "O"
        else:
            move = best_move(state)
            grid.place_mark(move, Mark.O)
            state.current_player = "X"

play()
