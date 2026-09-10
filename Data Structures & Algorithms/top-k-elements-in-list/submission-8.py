class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq= [[] for i in range(len(nums) + 1)]
        res = []

        for i in range(len(nums)):
                dic.setdefault(nums[i], 0)      
                dic[nums[i]] += 1 

        for v, f in dic.items():
            freq[f].append(v)
        for i in range(-1, -len(freq), -1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    return res