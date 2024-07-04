from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        accepted = {str(i) for i in range(1, 10)}
        height = width = 9

        def isValid(lst: list) -> bool:
            digits = set()
            for val in lst:
                if val == ".":
                    continue
                if val not in accepted:
                    return False
                if val in digits:
                    return False
                digits.add(val)
            return True

        # Loop through rows
        for i in range(height):
            row = board[i]
            if not isValid(row):
                # print("row",row)
                return False

        # Loop through columns
        for i in range(width):
            col = [board[j][i] for j in range(height)]
            if not isValid(col):
                # print("col",col)
                return False

        # Loop through 3 x3 sub boxes
        def getSubBox(r, c):
            values = [
                board[r][c],
                board[r][c + 1],
                board[r][c + 2],
                board[r + 1][c],
                board[r + 1][c + 1],
                board[r + 1][c + 2],
                board[r + 2][c],
                board[r + 2][c + 1],
                board[r + 2][c + 2],
            ]
            return values

        for r in range(0, height, 3):
            for c in range(0, width, 3):
                box = getSubBox(r, c)
                if not isValid(box):
                    # print("box",box)
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    # Example 1
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(board) == True

    # Example 2
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(board) == False

    print("PASSED")
