# Head ends here

def next_move(posr, posc, board):

    # retrieve all dirty cell locations
    dirty_cells_locs = [[i, j] for i, row in enumerate(board) for j, elem in enumerate(row) if elem == "d"] 

    # find distance of each cell w.r.t where the bot is
    dirty_cell_distances = [sum([abs(dirty_loc[0]-posr), abs(dirty_loc[1]-posc)]) for dirty_loc in dirty_cells_locs]

    # sort distances by their absolute value, retrieve best cell to move to
    def argmin(array):
        locs = [i for i in range(len(array))]
        z = list(zip(array, locs))
        z.sort()
        array, locs = list(zip(*z))
        return locs[0]

    best_loc_to_move = dirty_cells_locs[argmin(dirty_cell_distances)]

    # now get difference between best location to move and current loc
    diff_r, diff_c = best_loc_to_move[0] - posr, best_loc_to_move[1] - posc

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
        
        
        

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
