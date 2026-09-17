class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                acc = target + nums[j] + nums[k]
                if acc < 0:
                    j += 1
                elif acc > 0:
                    k -= 1
                else:
                    res.append([target, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res