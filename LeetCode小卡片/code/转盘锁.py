# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:37:09 2020

@author: TT
"""
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)#转为 set 保证唯一
        if '0000' in deadends:  return -1 # 初始的值不能为 deadends
        # BFS
        queue=[('0000',0)]#初始位置，放在队列中 用一个元组（0000，扭动次数）
        while queue:
            # cnt=1
            node,step= queue.pop(0)#取出队列的队首的位置
            for i in range(4):#遍历密码锁上的 四个位置
                for add in (1, -1):# 扭动一下，当前的值  注意是进位的原因，那么下一位则要减去1
                    cur = node[:i] + str((int(node[i]) + add) % 10) + node[i + 1:]#当前密码锁的状态
                    # print(cur)
                    if cur == target:# 如果是 等于target的值
                        return step+1
                    if not cur in deadends:#不在死亡数字里，
                        queue.append((cur,step+1))#则往队列里添加
                        deadends.add(cur)#为了不重复
        return -1


obj=Solution()
deadends = ["8888"]
target = "0009"
ans=obj.openLock(deadends, target)
print(ans)