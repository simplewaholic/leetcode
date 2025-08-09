class Solution:
    def makeFancyString(self, s: str) -> str:
        rs = ""
        count = 0
        for v in s:
            if rs == "":
                rs += v
                count += 1
            elif rs[-1] != v:
                rs += v
                count = 1
            elif rs[-1] == v and count == 1:
                rs += v
                count += 1
        return rs
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.makeFancyString("leeetcode"))  # Example usage
    print(sol.makeFancyString("aaabaaaa"))   # Another example
    print(sol.makeFancyString("aab"))        # Yet another example