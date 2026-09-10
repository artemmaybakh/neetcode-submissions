class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq= [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
            
        for v, f in dic.items():
            freq[f].append(v)
        for i in range(-1, -len(freq), -1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    return res