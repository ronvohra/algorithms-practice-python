def minimum_days(rows, columns, grid):  # BFS - a 2d grid of cell towers all servers need to be updated
    # WRITE YOUR CODE HERE
    if not rows or not columns:
        return 0
    # Get co-ordinate pairs of the initial state where val is 1
    ones = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j]]
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # Up, down, left, right
    days = 0
    
    while True:
        new_coords = []
        for [i, j] in ones:
            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < rows and 0 <= new_j < columns and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1
                    new_coords.append([new_i, new_j])
        ones = new_coords
        if not ones:
            break
        days += 1
        
    return days


def count_islands(rows, columns, grid):  # DFS count islands
    # WRITE YOUR CODE HERE
    if not rows or not columns:
        return 0
    count = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                dfs(rows, columns, grid, i, j)
                count += 1
    return count
    pass


def dfs(row_count, col_count, grid, x, y):
    if not grid[x][y]:
        return
    grid[x][y] = 0
    
    if x:
        dfs(row_count, col_count, grid, x-1, y)
    if x != row_count - 1:
        dfs(row_count, col_count, grid, x+1, y)
    if y:
        dfs(row_count, col_count, grid, x, y-1)
    if y != col_count - 1:
        dfs(row_count, col_count, grid, x, y+1)
