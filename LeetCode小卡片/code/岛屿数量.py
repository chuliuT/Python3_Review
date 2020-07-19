# grid=[
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
grid=[["0","1","0"],["1","0","1"],["0","1","0"]]

# 两种解法
def numIslands(grid):
    def bfs(i, j):
        queue = [[i, j]]# 构建一个队列 存放当前点的 坐标
        while queue:# 找陆地 循环遍历
            [i, j] = queue.pop(0)# 出队 坐标
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":#边界判断和 陆地判断
                grid[i][j] = "0"# 访问过的陆地值变为 0
                queue += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]# 将上下左右的值添加进去

    ans = 0#记录岛屿的数量
    for i in range(len(grid)):#遍历每一个点
        for j in range(len(grid[0])):
            if grid[i][j] == "0":#如果是水则跳过
                continue
            bfs(i, j)# 执行一次 bfs  找到上下左右的 1 并变成 0 当bfs执行完  那么 上下左右 没有陆地1 则找到一个 岛屿
            ans += 1
    return ans

def numIslands2(grid):
    def dfs(i, j):
        queue = [[i, j]]# 构建一个队列 存放当前点的 坐标
        while queue:# 找陆地 循环遍历
            [i, j] = queue.pop()# 出队 坐标
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":#边界判断和 陆地判断
                grid[i][j] = "0"# 访问过的陆地值变为 0
                queue += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]# 将上下左右的值添加进去

    ans = 0#记录岛屿的数量
    for i in range(len(grid)):#遍历每一个点
        for j in range(len(grid[0])):
            if grid[i][j] == "0":#如果是水则跳过
                continue
            dfs(i, j)# 执行一次 bfs  找到上下左右的 1 并变成 0 当bfs执行完  那么 上下左右 没有陆地1 则找到一个 岛屿
            ans += 1
    return ans

ans=numIslands2(grid)
print(ans)