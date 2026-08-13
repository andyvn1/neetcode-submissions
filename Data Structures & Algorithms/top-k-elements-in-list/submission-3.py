class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if k > 0:
                    output.append(n)
                    k -= 1
                else:
                    return output
        return output
                

