class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1 for _ in range(len(nums))]
        pref = 1 
        for i in range(len(nums)-1):
            post[i + 1] = post[i] * nums[i]

        for i in range(len(nums)-1, -1, -1):
            post[i] = pref * post[i]
            pref *= nums[i] 
            

        return post