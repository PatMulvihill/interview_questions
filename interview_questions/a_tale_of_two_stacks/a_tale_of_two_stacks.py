class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        try:
            if self.first:
                return self.first[-1]
        except IndexError:
            pass
        
    def pop(self):
        if self.first:
            return self.first.pop()
        
    def put(self, value):
        if self.first:
            for count in range(len(self.first)):
                self.second.append(self.first.pop())
            self.second.append(value)
            for count in range(len(self.second)):
                self.first.append(self.second.pop())
        else:
            self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
