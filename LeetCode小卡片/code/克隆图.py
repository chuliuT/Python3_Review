
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        lookup = {}  # 定义一个字典来存放 已经访问过的节点

        def dfs(node):  # DFS
            # print(node.val)
            if not node: return  # 如果node 为None
            if node in lookup:  # 判断node是否已经访问过了
                return lookup[node]  # 已经访问过了，直接返回
            clone = Node(node.val, [])  # 克隆当前的节点
            lookup[node] = clone  # 添加到visited列表里
            for n in node.neighbors:  # DFS的邻居 同时探索 自己的相邻的节点（clone的邻居）
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)