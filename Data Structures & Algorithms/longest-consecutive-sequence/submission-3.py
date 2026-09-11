class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            l = 1
            nums = list(set(nums))
            nums.sort()
            l_max = 1
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] + 1:
                    l += 1
                elif l >= l_max:
                    l_max = l
                    l = 1

            if l >= l_max:
                l_max = l
            return l_max
        return 0
        