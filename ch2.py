# Linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

def printPhonebook(node):
    if not node:
        return
    print node.data[0]+': '+node.data[1]
    printPhonebook(node.next)

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data = None):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def size(self):
        counter = 0
        current_node = self.head
        while current_node != None:
            counter += 1
            current_node = current_node.next
        return counter
    
    def sizeRec(self):
        
        if not self.head:
            return 0
        return 1 + self.next.sizeRec()
#def printList(mylist):
    #if 
def printList(myList):
    curr = myList.head
    while True:
        if not curr:
            return
        print curr.data
        curr = curr.next 
        
def printListRec(curr):
    if not curr:
        return
    printListRec(curr.next)
    print curr.data
         
def main():
    start = None
    """while (True):
        temp = []
        name = raw_input('Name?(Hit enter to exit): ')
        if not name:
            print '\n'
            break
        temp.append(name)
        
        phone_number = raw_input('Number?: ')
        temp.append(phone_number)
        new_entry = Node(temp)
        new_entry.next = start
        start = new_entry

    printPhonebook(start)
    """
    mylist = UnorderedList()
    print mylist.isEmpty()
    mylist.add('Josh')
    mylist.add('Karam')
    mylist.add('Ken')
    mylist.add('George')
    mylist.add('Xuan')
    print mylist.isEmpty()
    print 'List size is '+str(mylist.size()) 
    printListRec(mylist.head)


if __name__ == '__main__':
    main()
