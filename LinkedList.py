class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(data=i)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    #SUM OF ELEMENTS
    def listsum(self):
        s = 0 
        while self.head is not None:
            s+= self.head.data
            self.head = self.head.next
        return s
    #INDEX OF ELEMENT
    def indexof(self,node):
        i=0
        while self.head is not None:
            if self.head.data!=node:
                self.head = self.head.next
                i += 1
            else:
                return i
    #ADD METHODS
    def add_start(self, node):
        newnode=Node(node)
        newnode.next = self.head
        self.head = newnode

    def add_end(self, node):
        newnode=Node(node)
        if self.head is None:
            self.head = newnode
            return
        endnode=self.head
        while endnode.next:
            endnode=endnode.next
        endnode.next=newnode
        
    def add_middle(self,node):
        if self.head is None:
            self.head = Node(node)
        else:
            newnode = Node(node)
            head = self.head
            length = 0
            
            while head is not None:
                head = head.next
                length += 1
            if(length % 2 == 0):
                count = length / 2
            else:
                count = (length + 1) / 2
 
            head = self.head
 
        while(count > 1):
            count -= 1
            head = head.next
 
        newnode.next = head.next
        head.next = newnode
    #DELETE METHODS
    def del_start(self):
        if not self.head: 
            return None
        temp = self.head 
        self.head = self.head.next
        temp = None
        
    def del_end(self):
        if self.head is None: 
            return None
        if self.head.next is None: 
            self.head = None
            return None
        temp = self.head 
        while temp.next.next: 
            temp = temp.next
        temp.next = None
        
    def del_middle(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            del self.head
            return None
        else:
            head = self.head
            copy = head
            length = 0
           
            while head is not None:
                head = head.next
                length += 1
            
            if(length % 2 == 0):
                count = length / 2
            else:
                count = (length - 1) / 2
                
            head=self.head
            
            while(count > 1):
                count -= 1
                head = head.next
            
            head.next = head.next.next
    #REPLACE METHODS
    def rep_start(self,node):
        newnode=Node(node)
        if self.head is None:
            self.head = newnode
        else:
            temp=self.head.next
            self.head = newnode
            newnode.next=temp
    def rep_end(self,node):
        newnode=Node(node)
        if self.head is None:
            self.head = newnode
            return
        head=self.head
        length = 0
        while head is not None:
            head = head.next
            length += 1
        head=self.head
        while(length > 2):
            length -= 1
            head = head.next
        head.next=newnode
    def rep_middle(self,node):
        if self.head is None:
            self.head = Node(node)
        else:
            newnode = Node(node)
            head = self.head
            length = 0
            
            while head is not None:
                head = head.next
                length += 1
            if(length % 2 == 0):
                count = length / 2
            else:
                count = (length - 1) / 2
 
            head = self.head
 
        while(count > 1):
            count -= 1
            head = head.next
        temp=head.next
        head.next = newnode
        newnode.next = temp.next
def main():
    import time
    ll=LinkedList([1,2,3,4,5,6])
    print(ll)
    ftime=time.perf_counter()
    ll.add_start(0)
    ctime=time.perf_counter()
    print("add_start","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.add_end(0)
    ctime=time.perf_counter()
    print("add_end","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.add_middle(0)
    ctime=time.perf_counter()
    print("add_middle","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.del_start()
    ctime=time.perf_counter()
    print("del_start","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.del_end()
    ctime=time.perf_counter()
    print("del_end","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.del_middle()
    ctime=time.perf_counter()
    print("del_middle","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.rep_start(0)
    ctime=time.perf_counter()
    print("rep_start","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.rep_end(0)
    ctime=time.perf_counter()
    print("rep_end","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.rep_middle(0)
    ctime=time.perf_counter()
    print("rep_middle","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ll=LinkedList([1,2,3,4,5,6])
    ftime=time.perf_counter()
    ll.listsum()
    ctime=time.perf_counter()
    print("listsum","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    ftime=time.perf_counter()
    ll.indexof(3)
    ctime=time.perf_counter()
    print("indexof","%0.2f"%((ctime-ftime)*1000000)+" microseconds")
    
if __name__ == "__main__":
    main()
