import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        # sorted list of (enqueue, process, index) instead of dict
        starts = sorted((enq, proc, i) for i, (enq, proc) in enumerate(tasks))
        n = len(starts)

        i = 0          # pointer into starts: first task not yet enqueued
        q = []
        ans = []

        while i < n or q:
            # idle: jump time forward instead of ticking
            if not q:
                time = max(time, starts[i][0])

            # enqueue everything with start <= time
            while i < n and starts[i][0] <= time:
                enq, proc, idx = starts[i]
                heapq.heappush(q, (proc, idx))
                i += 1

            # run shortest task to completion, jumping time
            proc, idx = heapq.heappop(q)
            time += proc
            ans.append(idx)

        return ans