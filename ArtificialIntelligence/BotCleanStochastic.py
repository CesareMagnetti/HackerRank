import random

def next_move(posx, posy, board):
    # check if there is a dirt cell in the visible environment
    visible_locs = [[x, y] for x, row in enumerate(board) for y, elem in enumerate(row) if elem != "o"]
    visible_dirt = [loc for loc in visible_locs if board[loc[0]][loc[1]] == "d"]
    
    if len(visible_dirt)>0:
        # get to the closest dirt spot
        d = [sum([abs(loc[0]-posx), abs(loc[1]-posy)]) for loc in visible_dirt]
        # sort dirt location based on how far they are
        z = list(zip(d, visible_dirt))
        z.sort() #sorts based on first list d
        d, visible_dirt = list(zip(*z))

        # get the target location
        target = visible_dirt[0]
        
        # choose next move based on difference of coordinates (similar to previous exercises)
        diff_r, diff_c = target[0] - posx, target[1] - posy
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
    else:
        # there is no visible dirt, what to do?
        # some options: 1) move randomly until you find some dirt (did not work for 3/4 environments, really random                              outcome, sometimes it works other times not)
        #               2) more intelligent options would require some sort of memory/value-function
        #                  to be shared throughout function calls, exercise does not allow for that
        actions = ["UP", "DOWN", "LEFT", "RIGHT"]
        if posx == 0:
            actions.remove("UP")
        elif posx == len(board)-1:
            actions.remove("DOWN")
        if posy == 0:
            actions.remove("LEFT")
        elif posy == len(board[0])-1:
            actions.remove("RIGHT")
        
        # randomize action shuffling possible actions
        random.shuffle(actions)
        return actions[0]
            
                


if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    print(next_move(pos[0], pos[1], board))
