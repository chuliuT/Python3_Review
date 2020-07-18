# coding=utf-8

class Myqueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)


if __name__ == '__main__':
    myqueue = Myqueue()
    print(myqueue.is_empty())
    myqueue.enqueue(5)
    myqueue.enqueue(3)
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.is_empty())
