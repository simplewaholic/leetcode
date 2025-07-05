import heapq
from numbers import Number
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        lucky_numbers = [num for num, freq in count.items() if num == freq]
        
        return max(lucky_numbers) if lucky_numbers else -1


if __name__ == '__main__':
    s = Solution()
    t = [2, 2, 3, 4]
    result = s.findLucky(t)
    print(result)  # Output: -1
    t = [1, 2, 2, 3, 3, 3]
    result = s.findLucky(t)
    print(result)  # Output: 3
    t = [5, 5, 5, 5]
    result = s.findLucky(t)
    print(result)  # Output: -1