class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
sb = Stack()
text = input()
 
for character in text:
    sb.push(character)
 
reversed_text = ''
while not sb.is_empty():
    reversed_text = reversed_text + sb.pop()
 
if text == reversed_text:
    print("YES")
else:
    print("NO")
