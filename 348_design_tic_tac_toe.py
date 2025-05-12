"""
🔷 LeetCode 348 - Design Tic-Tac-Toe

🧠 Problem Summary:
Design a Tic-Tac-Toe game that can determine the winner efficiently in O(1) time per move.

Rules:
- Players take turns placing their symbol (1 or 2) in an n x n grid.
- The first player to fill a full row, column, or diagonal wins.
- Return 0 if no one has won after a move.

📘 Example:
toe = TicTacToe(3)
toe.move(0, 0, 1) -> 0
toe.move(0, 2, 2) -> 0
toe.move(2, 2, 1) -> 0
toe.move(1, 1, 2) -> 0
toe.move(2, 0, 1) -> 0
toe.move(1, 0, 2) -> 0
toe.move(2, 1, 1) -> 1  # Player 1 wins

📌 Follow-up:
Achieve better than O(n²) per move.
✅ Solution: O(1) per move using count tracking
"""

class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize the board state and counting arrays for both players.
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make a move for player 1 or 2 at the given position.
        Update counts and check for a winning condition.
        
        Returns:
            - 0 if no one wins.
            - 1 if player 1 wins.
            - 2 if player 2 wins.
        """
        # Use +1 for player 1, -1 for player 2
        to_add = 1 if player == 1 else -1

        self.rows[row] += to_add
        self.cols[col] += to_add

        if row == col:
            self.diagonal += to_add
        if row + col == self.n - 1:
            self.anti_diagonal += to_add

        # Check if absolute value hits n => win
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return player

        return 0


# 🔸 Example usage
if __name__ == "__main__":
    toe = TicTacToe(3)
    print(toe.move(0, 0, 1))  # 0
    print(toe.move(0, 2, 2))  # 0
    print(toe.move(2, 2, 1))  # 0
    print(toe.move(1, 1, 2))  # 0
    print(toe.move(2, 0, 1))  # 0
    print(toe.move(1, 0, 2))  # 0
    print(toe.move(2, 1, 1))  # 1 (Player 1 wins)

"""
🧠 Time and Space Complexity:

⏱ Time Complexity: O(1) per move
💾 Space Complexity: O(n) — to store row, col, and diagonal counters
"""

