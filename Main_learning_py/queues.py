import queue
"""
q = queue.Queue()

numbers = [10,20,30,40,50,60,70]

for num in numbers:
    q.put(num)

print(q.get())
print(q.get())
print("")
"""

q2 = queue.LifoQueue()
numbers2 = [10,20,30,40,50,60,70]

for num in numbers2:
    q2.put(num)

print(q2.get())
print(q2.get())
print("\n")

qp = queue.PriorityQueue()
qp.put((1,"Max Priority")) #Must be tuple to extract val.
qp.put((2,"Good Priority"))
qp.put((3,"Low Priority"))

while not qp.empty():
    print(qp.get()[1])

