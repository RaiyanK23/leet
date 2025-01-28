class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            middle_idx = (lower_bound + upper_bound) // 2

            if target == nums[middle_idx]:
                return middle_idx
            
            elif target < nums[middle_idx]:
                upper_bound = middle_idx - 1
            
            else:
                lower_bound = middle_idx + 1

       # [-1, 0, 3, 5, 9 ,12]


        return -1