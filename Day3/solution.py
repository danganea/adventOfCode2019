import numpy as np
with open("input.txt","r") as f:
    lines = f.readlines()
    line_A = lines[0].rstrip().split(',')
    line_B = lines[1].rstrip().split(',')
    path_dict = { 'U' : (0, 1) , 'D' : (0, -1), 'R' : (1, 0) , 'L' : (-1, 0)}
    lineA_dict = {}
    current_position = np.array([0, 0])
    walked_steps = 0
    for path in line_A:
        way = path_dict[path[0]]
        steps = int(path[1:])
        for step_i in range(1, steps + 1):
            walked_steps += 1
            current_position += way
            lineA_dict[tuple(current_position)] = walked_steps 
    
    intersections = []
    current_position = np.array([0, 0])
    walked_steps = 0
    for path in line_B:
        way = path_dict[path[0]]
        steps = int(path[1:])
        for step_i in range(1, steps + 1):
            walked_steps += 1
            current_position += way
            if tuple(current_position) in lineA_dict:
                intersections.append(walked_steps + lineA_dict[tuple(current_position)])


    val = min(intersections)
    print(f'{val}')
       

