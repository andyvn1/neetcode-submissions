class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            calc = numbers[l] + numbers[r]

            if calc < target:
                l += 1
            elif calc > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        