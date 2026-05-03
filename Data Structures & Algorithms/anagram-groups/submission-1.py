class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        ans = []
        for word in strs:
            sort_word = "".join(sorted(word))
            groups[sort_word].append(word)
        for group in groups.values():
            ans.append(group)
        return ans 