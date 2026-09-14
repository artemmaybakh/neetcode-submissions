class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind_pl = 0
        ind_neg = len(numbers) - 1
        while ind_pl < ind_neg:
            if numbers[ind_pl] + numbers[ind_neg] > target:
                ind_neg -= 1
            elif numbers[ind_pl] + numbers[ind_neg] < target:
                ind_pl += 1
            else:
                ind_pl += 1
                ind_neg = ind_neg + 1
                return [ind_pl, ind_neg]


        