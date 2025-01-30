class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = Counter(nums)
        result = [[] for i in range(len(nums) + 1)]

        for key, value in count_map.items():
            result[value].append(key)

        res = []

        for i in range(len(result) - 1, 0, -1):
            for n in result[i]:
                res.append(n)
                if(len(res) == k):
                    return res