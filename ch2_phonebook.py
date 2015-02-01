# phone book linked list practice

# Entry node: entry to be added to a phone book (linked list)
class nodeEntry:
    def __init__(self):
        self.name = None
        self.number = None
        self.next = None
# Phone book: linked list

class phonebook:
    def __init__(self):
        self.head = None

    def addToFirst(self, nodeEntry):
        nodeEntry.next = self.head
        self.head = nodeEntry

    def addToLast(self, nodeEntry):
        prev = self.head
        if not prev: 
            self.head = nodeEntry 
        else:
            curr = prev.next
            while curr:
                prev = curr
                curr = curr.next
            prev.next=nodeEntry

    def printPhonebook(self):
        curr = self.head
        while curr: 
            print curr.name+': '+curr.number
            curr = curr.next

    def printPBRec(self,node):
        if not node:
            return
        self.printPBRec(node.next)
        print node.name+': '+node.number

    def printPhonebookRec(self):
        curr = self.head
        print 'Printing current entries...'
        self.printPBRec(curr)
        
    def searchEntry(self,str_name):
        curr = self.head
        while curr:
            if curr.name.lower() == str_name.lower():
                return curr.number 
            curr = curr.next
        return None    
        
    def deleteEntry(self,str_name):
        curr = self.head
        while curr:
            if curr.name.lower() == str_name.lower():
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next 
        return None
def getNewEntry(nameIn=None,numberIn=None):
    if not nameIn:
        name = raw_input('Name? (press ENTER to exit): ')
        if not name:
            return None
        number = raw_input('Number?: ')
    else:
        name = nameIn
        number = numberIn 
    entry= nodeEntry()
    entry.name = name
    entry.number = number
    return entry 

def main():
    
    mybook = phonebook()
    newEntry = getNewEntry('Josh','919-279-0638')
    mybook.addToLast(newEntry)
    newEntry = getNewEntry('Karam','919-271-2838')
    mybook.addToLast(newEntry)
    newEntry = getNewEntry('Joseph','-279-0638')
    mybook.addToLast(newEntry)
    newEntry = getNewEntry('home','546-3311')
    mybook.addToLast(newEntry)

    mybook.printPhonebookRec()
    #mybook.printPhonebook()
    mybook.deleteEntry('Joseph')
    mybook.printPhonebookRec()
    while True:
        str_name = raw_input('Look up?: ')
        if not str_name:
            break
        str_num = mybook.searchEntry(str_name)
        if str_num:
            print 'His/her number is: '+str_num
        else:
            print 'Sorry, the entry not found'

if __name__ == '__main__':
    main()    


