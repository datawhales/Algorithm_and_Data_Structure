# queue 라이브러리 존재
# Queue(), LifoQueue(), PriorityQueue() 제공

import queue
data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())

print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for idx in range(10):
    enqueue(idx)

print(queue_list)
print(len(queue_list))

print(dequeue())
print(queue_list)
print(len(queue_list))