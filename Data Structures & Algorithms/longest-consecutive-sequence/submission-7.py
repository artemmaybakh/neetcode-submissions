class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = set(nums)
            l = 1
            res = []
            for el in nums:
                if el - 1 not in nums:
                    cur_num = el + 1
                    while cur_num in nums:
                        l += 1
                        cur_num += 1
                    res.append(l)
                    l = 1
                else:
                    res.append(l)
                    
            return max(res)
        return 0


        