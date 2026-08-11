class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0
        
        while(l < len(arr) - 1):
            max_value = 0
            for r in range(l + 1, len(arr)):
                max_value = max(max_value, arr[r])
            arr[l] = max_value
            l += 1
        arr[l] = -1
        return arr
            

        