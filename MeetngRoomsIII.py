class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = list(range(n))
        heapify(rooms)
        arr = []
        count = [0] * n
        
        for start, end in meetings:
            while arr and arr[0][0] <= start:
                time, room_num = heappop(arr)
                heappush(rooms, room_num)
            
            if rooms:
                room = heappop(rooms)
                heappush(arr, (end, room))
                count[room] += 1
            else:
                min_time, room = heappop(arr)
                new_time = min_time + (end - start)
                heappush(arr, (new_time, room))
                count[room] += 1
        
        return count.index(max(count))
