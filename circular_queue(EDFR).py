class Queue:
    def __init__(self, K):
        self.size = 0
        self.capacity = K
        self.array = [None] * K
        self.front = self.rear = -1

    def isempty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.isfull():
            print("Queue is full")
            return
        if self.isempty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = data
        self.size += 1
        print("Element enqueued:", self.array[self.rear])

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        value = self.array[self.front]
        if self.front == self.rear:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print("Deleted element:", value)
        self.size -= 1
        return value

    def fElement(self):
        if self.isempty():
            print("Queue is empty")
            return None
        return self.array[self.front]

    def rElement(self):
        if self.isfull():
            print("Queue is full")
            return None
        return self.array[self.rear]

# Example usage:
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Front element:", q.fElement())
print("Rear element:", q.rElement())
q.dequeue()
q.dequeue()
print("Front element after dequeue:", q.fElement())
q.enqueue(6)
q.dequeue()
print("Rear element after dequeue:", q.rElement())
