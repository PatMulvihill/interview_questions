class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
        
    def queueify(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
    
    def peek(self):
        self.queueify()
        return self.second[-1]

    
    def pop(self):
        self.queueify()
        return self.second.pop()
      
        
    def put(self, value):
        self.first.append(value)

        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
