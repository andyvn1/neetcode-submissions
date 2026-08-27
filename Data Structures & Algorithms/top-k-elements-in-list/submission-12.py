class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, v in count.items():
            freq[v].append(key)

        output = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if k > 0:
                    k -= 1
                    output.append(n)
                    
        return output

            
        