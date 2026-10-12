import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = [[fq, x] for x, fq in Counter(nums).items()]

        heapq.heapify_max(h)

        ans = []
        for i in range(k):
            most = heapq.heappop_max(h)[1]
            ans.append(most)
        
        return ans
