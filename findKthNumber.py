class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(curr):
            res = 0
            next = curr + 1
            while curr <= n:
                res += min(next, n + 1) - curr
                curr *= 10
                next *= 10
            return res

        curr = 1
        k -= 1 

        while k > 0:
            steps = count(curr)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
