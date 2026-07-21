class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-x for x in count.values()]
        heapq.heapify(max_heap)

        q = deque() # -cnt : idleTime
        time = 0

        while max_heap or q:

            time += 1
            if max_heap:
                val = 1 + heapq.heappop(max_heap)
                if val != 0:    
                    q.append([val, time + n])

            if q and time == q[0][1]:
                heapq.heappush(max_heap, q.popleft()[0])

        return time

