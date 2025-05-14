def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # 9 ô 3x3

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            if val in rows[i]:
                return False
            if val in cols[j]:
                return False
            box_index = (i // 3) * 3 + (j // 3)
            if val in boxes[box_index]:
                return False

            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)
    
    return True


if __name__ == "__main__":
    mboard = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(mboard))
