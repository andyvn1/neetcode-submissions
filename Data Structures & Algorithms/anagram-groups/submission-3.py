class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = defaultdict(list)

        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            dict_strs[tuple(cnt)].append(word)
        return list(dict_strs.values())

        