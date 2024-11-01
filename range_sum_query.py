class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.build(nums, left_child, start, mid)
            self.build(nums, right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            # case 1: if the index is in the left part
            if index <= mid:
                self._update(left_child, start, mid, index, val)
            # case 2: if the index is in the right part
            else:
                self._update(right_child, mid + 1, end, index, val)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)

    def sum_range(self, node, start, end, left, right):
        # case 1: Disjoint
        if left > end or right < start:
            return 0

        # case 2: Fully covered by the range
        if left <= start and end <= right:
            return self.tree[node]

        # case 3: Partially covered
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = self.sum_range(left_child, start, mid, left, right)
        right_sum = self.sum_range(right_child, mid + 1, end, left, right)

        return left_sum + right_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_range(0, 0, self.n - 1, left, right)

# Usage example:
# obj = NumArray(nums)
# obj.update(index, val)
# param_2 = obj.sumRange(left, right)
