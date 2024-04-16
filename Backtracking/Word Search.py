from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        visited = set()

        def dfs(i: int, j: int, currWord: str, hasWord: List[bool]):
            if i >= width or i < 0 or j >= height or j < 0:
                return
            if hasWord[0]:
                return
            if currWord and board[j][i] != currWord[0]:
                return

            if not currWord:
                hasWord[0] = True
                return
            if (i, j) in visited:
                return

            visited.add((i, j))
            print(f"dfs {i}, {j}, currWord={currWord}, hasWord={hasWord}")
            currWord = currWord[1:]
            dfs(i + 1, j, currWord, ret)
            dfs(i - 1, j, currWord, ret)
            dfs(i, j + 1, currWord, ret)
            dfs(i, j - 1, currWord, ret)
            dfs(i, j, currWord, ret)
            visited.remove((i, j))

        ret = [False]
        for j in range(height):
            for i in range(width):
                if board[j][i] == word[0]:
                    dfs(i, j, word, ret)

        return ret[0]
