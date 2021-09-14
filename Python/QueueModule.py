'''
queue — 线程安全的 FIFO 队列
queue 模块提供了一个适用于多线程编程的先进先出（FIFO）数据结构。它可以用来安全地在生产者和消费者线程之间传递消息或其他数据。锁是调用者来处理的，所有多个线程能够安全且容易的使用同样的 Queue 实例工作。Queue 的大小（它包含的元素的数量）可能会受到限制，以调节内存的适用或处理。

使用 put() 将元素添加到序列的一端，并适用 get() 从另一端移除。
'''
import queue
import threading
import functools

# FIFO
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

# LIFO
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

# Priority Queue 
# 它内部进行的排序方式是以其数据而定，而不是数据添加到队列中时的顺序。
@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()

workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()

