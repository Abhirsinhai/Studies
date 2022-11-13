#This is already very explainable, its just above me. Reverse stack reverses the items orders.
stack = [4, 9, 12, 51, 2]
class Stack:
    def push(self, x):
        stack.append(x)
        if len(stack)>10:
            print("stack overflow")
            stack.pop(-1)
        print(stack)
    def pop(self, x):
        if len(stack) == 0:
            print("stack underflow")
        else:
            stack.pop(x)
        print(stack)
    def isFull(self):
        if len(stack) == 10:
            print("stack is full")
        elif len(stack) == 0:
            print("stack is empty")
        else:
            print("stack is not full")
    def peek(self, x):
        print(stack[x])
    def count(self):
        print("length of stack is", len(stack))
    def change(self, x, y):
        stack.insert(x, y)
        print(stack)
    def display(self):
        print(stack)
    def reverseStack(self):
        stack.reverse()
        print(stack)
i = Stack()
i.push(5)
i.reverseStack()