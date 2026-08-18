class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            dict_nums[n] = 1 + dict_nums.get(n, 0)
        
        for n, i in dict_nums.items():
            freq[i].append(n)
        
        output = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if k > 0:
                    output.append(n)
                    k -= 1
                else:
                    return output
        return output


