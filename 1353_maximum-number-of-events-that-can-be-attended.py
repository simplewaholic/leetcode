import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        day = 1
        i = 0
        n = len(events)
        attended = 0
        last_day = max(end for _, end in events)

        for day in range(1, last_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEvents([[1,2],[2,3],[3,4]]))  # Example usage
    print(sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]))  # Another example