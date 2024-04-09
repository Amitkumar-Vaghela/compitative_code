# 1.Write a program for implementing a MINSTACK which should support 
# operations like push, pop, overflow, underflow, display
# a. Construct a stack of N-capacity
# b. Push elements
# c. Pop elements
# d. Top element
# e. Retrieve the min element from the stack


class Stack:
    def __init__(self):
        self.max = 100
        self.array = []
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.max - 1

    def push(self, data):
        if self.isFull():
            print("stack overflow")
        else:
            self.top += 1
            self.array.append(data)
            print("Elements are:", self.array)

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            a = self.array.pop()
            self.top -= 1
            print("Popped element is:", a)

    def minimum(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.min = self.array[0]
            for i in self.array:
                if self.min > i:
                    self.min = i
            print("Minimum element is:", self.min)  # Print the minimum element

    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            print("Top element is:", self.array[self.top])

# Testing the stack
A = Stack()
A.isEmpty()
A.isFull()
A.push(10)
A.push(20)
A.push(30)
A.push(40)
A.pop()
A.push(50)
A.push(45)
A.minimum()
A.peek()
