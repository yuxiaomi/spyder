import queue
q=queue.Queue()
q.put('123')

val=q.get()
print(val)
try:
    val=q.get(timeout=3)
    print(val)
except queue.Empty:
    print('没有信息')
