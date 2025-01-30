class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
        
        result_map[tuple(count)].append(word)