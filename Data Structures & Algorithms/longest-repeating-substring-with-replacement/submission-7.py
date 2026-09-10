class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        caracter_count = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            character = s[r]
            caracter_count[character] = 1 + caracter_count.get(character, 0)

            while (r - l + 1) - max(caracter_count.values()) > k:
                caracter_count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
                

        