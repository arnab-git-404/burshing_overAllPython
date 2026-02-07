class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
    
    def print(self):
        if self.head is None:
            print("LL is NULL")
            return
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.data , "->" )
                currentNode = currentNode.next
        
