class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind_pl = 0
        ind_neg = -1
        result = True
        while result:
            if numbers[ind_pl] + numbers[ind_neg] > target:
                ind_neg -= 1
            elif numbers[ind_pl] + numbers[ind_neg] < target:
                ind_pl += 1
            else:
                ind_pl += 1
                ind_neg = len(numbers) + ind_neg + 1
                result = False


        return [ind_pl, ind_neg]