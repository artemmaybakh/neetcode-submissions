class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for el in s:
            ok = True
            cur = el
            res = 1
            if cur - 1 not in s:
                while ok:
                    if cur + 1 in s:
                        res += 1
                        cur += 1
                    else:
                        ok = False
                maxi = max(maxi, res)
        return maxi