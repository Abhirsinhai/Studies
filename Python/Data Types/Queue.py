queue = ["English", "Hindi", "Coding"]
class Queue: #
    def peek(self): #Print out the first value in the queue
        if len(queue) >= 0:
            print(queue[0])
        else:
            print("Your queue is too short.")
    def enq(self, x): #Add data at the end of the queue
        return queue.append(x)
    def deq(self): #Remove data from the front of the queue
        queue.pop(0)
        return queue
    def reverse(self): #Reverse the order of the data in the queue
        queue.reverse()
        return queue