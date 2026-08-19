class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difference_dict = {}

        for i, n in enumerate(numbers):
            difference = target - n
            if difference in difference_dict and difference_dict[difference] < i:
                return [difference_dict[difference] + 1, i + 1]
            difference_dict[n] = i
        return []
                

        