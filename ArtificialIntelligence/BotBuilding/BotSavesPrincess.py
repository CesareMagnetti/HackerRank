def displayPathtoPrincess(n,grid):
    
    #get positions
    p_i,p_j,m_i,m_j = None,None,None,None
    for i, g in enumerate(grid):
        for j, gg in enumerate(g):
            if gg == "p":
                p_i,p_j = i,j
            elif gg == "m":
                m_i,m_j = i,j
            else:
                continue
    
    #total n of steps in vertical and horizontal directions
    n_v = p_i-m_i # if negative princes is above (need to go UP)
    n_h = p_j-m_j # if negative need to go LEFT
    
    if n_v<0:
        steps_v = ["UP",]*(-n_v)
    else:
        steps_v = ["DOWN",]*n_v
    
    if n_h<0:
        steps_h = ["LEFT",]*(-n_h)
    else:
        steps_h = ["RIGHT",]*n_h
        
    #interlace elements of arrays
    steps = [0,]*(len(steps_h)+len(steps_v))
    
    if len(steps_h)>len(steps_v):
        steps[0::2] = steps_h
        steps[1::2] = steps_v
    else:
        steps[0::2] = steps_v
        steps[1::2] = steps_h
        
    for step in steps:
        print(step)
    
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
