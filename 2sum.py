class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in map:
                return [map[complement], index]
            
            else:
                map[number] = index

        return []