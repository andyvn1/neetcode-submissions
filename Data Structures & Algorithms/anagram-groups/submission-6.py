class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for n in strs:
            binary_word = [0] * 26
            for c in n:
                binary_word[ord(c) - ord('a')] += 1
            strs_dict[tuple(binary_word)].append(n)

        return list(strs_dict.values())

        