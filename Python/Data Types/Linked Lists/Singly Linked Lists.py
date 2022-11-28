from itertools import count
from re import M, S
from sys import displayhook

class Node:  # Node that creates data
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:  # Main Linked List
    def __init__(self):  # Links for the list
        self.head = None
        self.last_node = None

    def append(self, data):  # Add Data
        global count
        count = 0
        if data == 100:
            count = count+1
            
        if self.last_node is None:  # Check if node is empty
            self.head = Node(data)
            self.last_node = self.head
        else:  # Add the data to the node
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):  # Display the items in the node
        current = self.head  # Use current data

        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print("\n")

    def getLength(self):  # Get the length of the
        size = 0  # Size variable for counter
        current = self.head  # Current data when running the program
        while current is not None:  # Checks if it is not empty
            size += 1
            current = current.next
        print("\n")
        return size  # Print out the size of the linked list

    def insert_at(self, newElement, position):  # Insert item with index
        newNode = Node(newElement)
        if (position < 1):  # Checks the position if it is below one
            print("\nposition should be >= 1.")
        elif (position == 1):  # Checks if the number is equal to one, it will place it on the head and move the element at head and move it to the node after self.head
            newNode.next = self.head
            self.head = newNode
        else:  # Else program for if the list is above one
            temp = self.head  # Temporarily stores the the first element
            for i in range(1, position-1):  # runs a loop
                if (temp != None):
                    temp = temp.next

            if (temp != None):  # if the head is nothing
                newNode.next = temp.next
                temp.next = newNode
            else:  # If the head is nothing, say that the node is null
                print("\nThe previous node is null.")

    def remove_from_beggining(self):  # Self Explanatory
        if not self.head:
            return None

        new = self.head
        head = self.head
        new = None
        return head

    def remove_from_end(self):  # Self Explanatory
        if self.head == None:
            return None
        if self.head.next == None:
            head = None
            return None
        beforelast = self.head
        while (beforelast.next.next):
            beforelast = beforelast.next
        beforelast.next = None
        return self.head

    def remove_at(self, position):  # Self Explanatory
        if (position < 1):
            print("\nThe position should be greater than 0")
        elif (position == 1 and self.head != None):
            node_deleted = self.head
            self.head = self.head.next
            node_deleted = None
        else:
            temp = self.head
            for i in range(1, position-1):
                if temp != None:
                    temp = temp.next

        if (temp != None and temp.next != None):
            node_delete = temp.next
            temp.next = temp.next.next
            node_delete = None

        else:
            print("\nThere is nothing in the node")

    def reverse(self):  # Self Explanatory
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    def countMarks(self):
        return count
        print("\n")
MyList = LinkedList()
MyList.append(97)
MyList.append(98)
MyList.append(99)
MyList.append(100)
MyList.append(98)
MyList.append(100)
MyList.append(99)
MyList.display()
MyList.countMarks()