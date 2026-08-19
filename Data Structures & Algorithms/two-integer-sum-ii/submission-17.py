class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum3 = numbers[l] + numbers[r]

            if sum3 < target:
                l += 1
            elif sum3 > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        