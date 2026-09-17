class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        max_area = 0
        num = 0
        while i < j:
            #print(heights[j], heights[i])
            if (j - i) * min(heights[j], heights[i]) > max_area:
                max_area = (j - i) * min(heights[j], heights[i])
            if heights[j] < heights[i]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
            else:
                if heights[j-1] > heights[i+1]:
                    j -= 1
                else:
                    i += 1

        return max_area