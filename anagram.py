class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_str_s = Counter(s)
        map_str_t = Counter(t)

        for key, value in map_str_s.items():
            if key not in map_str_t:
                return False
            
            elif map_str_t[key] != value:
                return False
        
        return True