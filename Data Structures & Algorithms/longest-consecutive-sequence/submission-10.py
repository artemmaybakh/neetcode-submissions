class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = set(nums)
            l = 1
            max_l = 1
            for el in nums:
                if el - 1 not in nums:
                    
                    while el + l in nums:
                        l += 1
                        
                    max_l = max(max_l, l)
                    l = 1

                    
            return max_l
        return 0


        