class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countdict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            countdict[tuple(count)].append(word)
        return list(countdict.values())