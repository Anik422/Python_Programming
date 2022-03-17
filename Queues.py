# from  collections import deque

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.pop(0)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)
if not queue:
    print("Empty")