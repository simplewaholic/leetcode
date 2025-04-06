
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums



if __name__ == '__main__':
    # Example usage
    s = Solution()
    t = [1, 2, 3, 4]
    result = s.runningSum(t)
    print(result)  # Output: [1, 3, 6, 10]