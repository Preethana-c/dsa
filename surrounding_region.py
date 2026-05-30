def surrounding_region(grid):
    rows=len(grid)
    cols=len(grid[0])
    visited = set()
    queue
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "0" and (i, j) not in visited:
                queue = [(i, j)]
                visited.add((i, j))
                while queue:
                    