class Solution:
    def trap(self, height: List[int]) -> int:
        summ = 0

        i = 0
        j = len(height) - 1
        leftmax = height[i]
        rightmax = height[j]
        while i < j:

            

            if leftmax < rightmax:
                i += 1
                leftmax = max(leftmax, height[i])
                summ += leftmax - height[i]
            else:
                j -= 1
                rightmax = max(rightmax, height[j])
                summ += rightmax - height[j]
            



        return summ