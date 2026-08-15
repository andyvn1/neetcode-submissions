class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            cnt_dict[n] = 1 + cnt_dict.get(n, 0)
        
        for n, c in cnt_dict.items():
            freq[c].append(n)
        
        output = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if k > 0:
                    output.append(n)
                    k -= 1
                else:
                    return output
        return output