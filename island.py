def islands(grid,queue):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "1" and (i, j) not in visited:

                islands += 1

                queue = []
                queue.append((i, j))
                visited.add((i, j))

                while queue:

                    i, j = queue.pop(0)

                    # up
                    if i-1 >= 0 and grid[i-1][j] == "1" and (i-1, j) not in visited:
                        queue.append((i-1, j))
                        visited.add((i-1, j))

                    # down
                    if i+1 < rows and grid[i+1][j] == "1" and (i+1, j) not in visited:
                        queue.append((i+1, j))
                        visited.add((i+1, j))

                    # left
                    if j-1 >= 0 and grid[i][j-1] == "1" and (i, j-1) not in visited:
                        queue.append((i, j-1))
                        visited.add((i, j-1))

                    # right
                    if j+1 < cols and grid[i][j+1] == "1" and (i, j+1) not in visited:
                        queue.append((i, j+1))
                        visited.add((i, j+1))

    return islands