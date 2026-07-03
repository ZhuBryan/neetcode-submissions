class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box_ind = (r//3) * 3 + (c//3)
                unit = board[r][c]
                if unit == '.':
                    continue
                if unit in rows[r] or unit in cols[c] or unit in boxes[box_ind]:
                    return False
                rows[r].add(unit)
                cols[c].add(unit)
                boxes[box_ind].add(unit)
        return True