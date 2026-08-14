class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)
        for n, c in num_count.items():
            freq[c].append(n)

        output = []
        for i in range(len(freq) - 1, -1, -1):
            for f in freq[i]:
                if k > 0:
                    output.append(f)
                    k -= 1
        return output


        

        