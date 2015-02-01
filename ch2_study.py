# linked list problems

# 2.5 (2.6 in 5th edition)

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addToFirst(self, data = None):
        curr = Node(data)
        curr.next = self.head
        self.head = curr
    
    def addToLast(self, data = None):
        curr = self.head
        if not curr:
            # append here
            self.head = Node(data)
        else:
            prev = curr
            curr = curr.next
            while curr.next:
                prev = curr
                curr = curr.next
        curr.next = Node(data)

    def printList(self):
        curr = self.head
        while curr:
            print curr.data
            curr = curr.next

    def printLR(self,node):
        if not node:
            return
        print node.data
        self.printLR(node.next)

    def printListRec(self):
        curr = self.head
        self.printLR(curr)
    
    def revList(self, node):
        if not node.next:
            self.head = node
        revList(node.next)
           
    def reverseList(self):
        #self.revList(self.head)        
        prevNode = None
        currNode = self.head
        nextNode = None 
        
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode   

def main():
    myList = LinkedList()
    myList.addToFirst(4)
    myList.addToFirst(3)
    myList.addToFirst(2)
    myList.addToFirst(1)
    
    myList.printListRec()
    print 'now append to last'
    myList.addToLast(5)
    myList.addToLast(6)
    myList.addToLast(7)
    print 'print the list'
    myList.printListRec()   
    print 'Reverse the list and print'
    myList.reverseList()   
    myList.printListRec()   

if __name__ == '__main__':
    main()
         
