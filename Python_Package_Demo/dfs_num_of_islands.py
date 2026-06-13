def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += dfs(grid, i, j)

    return count

def dfs(grid, r, c) -> int:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
        return 0
    
    grid[r][c] = '0'
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)

    return 1


if __name__ == "__main__":
    grid = [
        ["1","1","0","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","1"],
        ["0","0","0","1","1"]
    ]

    print(num_islands(grid))