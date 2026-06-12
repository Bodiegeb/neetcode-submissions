class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, a - b)
        return 0 if len(maxHeap) == 0 else -heapq.heappop(maxHeap)