import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self._index = 0

    def add_task(self, name, priority):
        heapq.heappush(self.heap, (-priority, self._index, name))
        self._index += 1

    def run_next(self):
        if self.heap:
            priority, _, name = heapq.heappop(self.heap)
            return name, -priority
        return None

scheduler = TaskScheduler()
scheduler.add_task("Task A", 3)
scheduler.add_task("Task B", 9)
scheduler.add_task("Task C", 5)
scheduler.add_task("Task D", 7)

while True:
    task = scheduler.run_next()
    if not task:
        break
    print(f"Executed: {task[0]} with priority {task[1]}")
