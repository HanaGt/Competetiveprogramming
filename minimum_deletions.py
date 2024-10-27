class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            if i == "b":
                stack.append(i)
            else:
                if stack and i == "a":
                    stack.pop()
                    count += 1

        return count
        

        
