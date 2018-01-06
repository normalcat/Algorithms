class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def PrintAllVals(self):
        runner = self.head
        self.tail = runner
        while(runner != None):
            print runner.value
            if runner.next:
                self.tail = runner.next
            runner = runner.next
        print "Head:" + self.head.value + " Tail:" + self.tail.value
        return self

    def AddBack(self,val):
        new_node = SLNode(val)
        if self.tail == None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        if self.head == None:
            self.head = new_node
        return self

    def AddFront(self,val):
        new_node = SLNode(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        if self.tail == None:
            self.tail = new_node
        return self

    def InsertBefore(self,nextVal, val):
        if self.head.value == nextVal:
            self.AddFront(val)
        else:
            runner = self.head
            while(runner.next != None and runner.next.value != nextVal):
                runner = runner.next
            new_node = SLNode(val)
            new_node.next = runner.next
            runner.next = new_node
        return self

    def InsertAfter(self,preVal, val):
        runner = self.head
        while(runner != None and runner.value!=preVal):
            runner = runner.next
        new_node = SLNode(val)
        new_node.next = runner.next
        runner.next = new_node
        if runner == self.tail:
            self.tail = new_node
        return self

    def RemoveNode(self,val):
        runner = self.head
        if runner.value == val:
            self.head = runner.next
            return self 

        while(runner.next != self.tail and runner.next.value != val):
            runner = runner.next

        if runner.next == self.tail and runner.next.value == val:
            runner.next = None
            self.tail = runner 
        else:           
            runner.next = runner.next.next
        return self

    def RverseList(self):
        if self.head == self.tail:
            return self
        
        first = self.head
        second = first.next

        while(second.next != None):
            third = second.next
            second.next = first
            if first == self.head:
                first.next = None
                self.tail = first
            first = second
            second = third
        self.head = second
        second.next = first

        return self



list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.PrintAllVals()
print "=============="
list.AddBack('Eli')
list.PrintAllVals()
print "=============="
list.AddFront('BeforeA')
list.PrintAllVals()
print "=============="
list.InsertBefore('BeforeA','BeforeBeforeA')
list.PrintAllVals()
print "=============="
list.InsertBefore('Chad','Bill')
list.PrintAllVals()
print "=============="
list.InsertAfter('Eli','Fruit')
list.PrintAllVals()
print "=============="
list.RemoveNode('BeforeA')
list.PrintAllVals()
print "=============="
list.RverseList()
list.PrintAllVals()

