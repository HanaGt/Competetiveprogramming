class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        count = 0
        heap = [-num for num in nums]
        heapify(heap)

        while k:
            max_num = -heappop(heap)
            count += max_num

            changed = math.ceil(max_num / 3)
            heappush(heap , -changed)

            k -= 1

        return count



       
