def next_move(posr, posc, board):

    # retrieve dirty cell location
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == "d":
                dirt_r, dirt_c = i,j
                break 

    # get difference between dirt location to move and current loc
    diff_r, diff_c = dirt_r - posr, dirt_c - posc

    # move accordingly to get closer to the dirty cell, clean if we are on it (zero distances)
    if diff_r == 0 and diff_c == 0:
        return "CLEAN"
    elif abs(diff_r)>=abs(diff_c):
        if diff_r > 0:
            return "DOWN"
        else:
            return "UP"
    else:
        if diff_c > 0:
            return "RIGHT"
        else:
            return "LEFT"

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
