import time

distance = 0

maze = [
    ["#", "#", "O", "#"],
    ["#", " ", " ", "#"],
    ["#", " ", "#", "#"],
    ["#", " ", "#", "#"],
    ["#", " ", "#", "#"],
    ["#", " ", "#", "#"],
    ["#", " ", "#", "#"],
    ["#", " ", " ", "#"],
    ["#", "#", "X", "#"]
]

# This function finds the entrance of the maze
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze):
    start = 'O'
    end = 'X'
    current_pos = find_start(maze, start)
    row, col = current_pos
    
# This loop searches for exit from the maze    
    while True:
        global distance
        if maze[row + 1][col] != '#' and row + 1 > 0:
            maze[row][col] = '#'
            row += 1
        elif maze[row - 1][col] != '#' and row > 0:
            maze[row][col] = '#'
            row -= 1
        elif maze[row][col + 1] != '#' and col + 1 < len(maze[0]):
            maze[row][col] = '#'
            col += 1
        elif maze[row][col - 1] != '#' and col > 0:
            maze[row][col] = '#'
            col -= 1
        
        for i in maze:
            print(' '.join(map(str, i)))
        print('\n')
        time.sleep(0.3)
        if maze[row][col] == end:
            distance += 1
            print(f"It took us {distance} blocks to go through the maze!")
            break
        distance += 1

find_path(maze)