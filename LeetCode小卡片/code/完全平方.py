# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:42:47 2020

@author: TT
"""
class Solution:
    def numSquares(self, n: int) -> int:
        q=[[n,0]]#队列
        visited=[False for _ in range(n+1)]#是否已经访问了
        visited[n]=True#访问的第一个值

        while q:
            i=1#用于分解的 基数
            num,step=q.pop(0)#取出队首的 第一个值
            tnum=num-i**2# 计算平方数
            while tnum>=0:#当这个值大于0
                if tnum==0: return step+1#满足平方的条件
                if not visited[tnum]:#没有访问过的值
                    q.append((tnum,step+1))
                    visited[tnum]=True#
                i+=1#基数向后找
                tnum=num-i**2
        return step
