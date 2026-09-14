board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
        ]



def print_board(bo):
        for i, r in enumerate(bo):
                if i % 3 == 0 and i != 0:
                        print("-" * 21)
                for j, val in enumerate(r):
                        if j % 3 == 0 and j != 0:
                                print("|", end=" ")
                        print(val, end=" ")
                print()

print_board(board)
print("\n")

def find_empty(bo):
    for i, r in enumerate(bo):
            for j, val in enumerate(r):
                    if val == 0:
                            return i,j
    return None


def is_valid(bo, pos, num):
        row, col = pos
        for i in bo[row]:
                if i == num:
                        return False
        for i in range(len(bo)):
                if bo[i][col] == num:
                        return False
        box_row_start = (row//3) * 3
        box_col_start = (col//3) * 3
        for i in range(3):
                for j in range(3):
                        real_row = box_row_start + i
                        real_col = box_col_start + j
                        if bo[real_row][real_col] == num:
                                return False
        return True

def solve(bo):
        empty = find_empty(bo)
        if empty is None:
                return True
        row, col = empty
        for num in range (1, 10):
                if is_valid(bo, empty, num):
                        bo[row][col] = num
                        if solve(bo):
                                return True
                        bo[row][col] = 0
        return False

solve(board)
print_board(board)