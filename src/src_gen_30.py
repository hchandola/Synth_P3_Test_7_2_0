from typing import List

def sat300(good_boards: List[str]):
    board_bit_reps = {tuple(sum(1 << i for i in range(9) if b[i] == c) for c in "XO") for b in good_boards}
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]

    def tie(x, o):  # returns True if X has a forced tie/win assuming it's X's turn to move.
        x |= 1 << [i for i in range(9) if (x | (1 << i), o) in board_bit_reps][0]
        return not win[o] and (win[x] or all((x | o) & (1 << i) or tie(x, o | (1 << i)) for i in range(9)))

    return tie(0, 0)
def sol300():
    """
    Compute a strategy for X (first player) in tic-tac-toe that guarantees a tie. That is a strategy for X that,
    no matter what the opponent does, X does not lose.

    A board is represented as a 9-char string like an X in the middle would be "....X...." and a
    move is an integer 0-8. The answer is a list of "good boards" that X aims for, so no matter what O does there
    is always good board that X can get to with a single move.
    """
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]  # 9-bit representation

    good_boards = []

    def x_move(x, o):  # returns True if x wins or ties, x's turn to move
        if win[o]:
            return False
        if x | o == 511:
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and o_move(x | (1 << i), o):
                good_boards.append("".join(".XO"[((x >> j) & 1) + 2 * ((o >> j) & 1) + (i == j)] for j in range(9)))
                return True
        return False  # O wins

    def o_move(x, o):  # returns True if x wins or ties, x's turn to move
        if win[x] or x | o == 511:  # full board
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and not x_move(x, o | (1 << i)):
                return False
        return True  # O wins

    res = x_move(0, 0)
    assert res

    return good_boards
# assert sat300(sol300())

