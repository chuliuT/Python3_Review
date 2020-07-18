


# - MyCircularQueue(k)`: 构造器，设置队列长度为 k 。
# - `Front`: 从队首获取元素。如果队列为空，返回 -1 。
# - `Rear`: 获取队尾元素。如果队列为空，返回 -1 。
# - `enQueue(value)`: 向循环队列插入一个元素。如果成功插入则返回真。
# - `deQueue()`: 从循环队列中删除一个元素。如果成功删除则返回真。
# - `isEmpty()`: 检查循环队列是否为空。
# - `isFull()`: 检查循环队列是否已满。

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.len=k
        self.queue=[]
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return False
        else:
            return self.queue[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return False
        else:
            return self.queue[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if len(self.queue)==0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if len(self.queue)==self.len else False

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.queue)
param_1 = obj.enQueue(5)
param_1 = obj.enQueue(6)
param_1 = obj.enQueue(7)
print(obj.queue)
param_2 = obj.deQueue()
print(obj.queue)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)