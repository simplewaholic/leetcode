from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_i = 0
        cookie_i = 0
        while child_i < len(g) and cookie_i < len(s):
            if g[child_i] <= s[cookie_i]:
                child_i += 1
            cookie_i += 1
        return child_i

if __name__ == "__main__":
    # Test case
    cookies = [1,2,3]
    children = [1,1]
    # Create an instance of the Solution class
    solution = Solution()
    print(solution.findContentChildren(cookies, children))  # Output: 64