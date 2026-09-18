class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]* len(height)
        maxRight = [0]* len(height)
        j = len(height) - 1
        for i in range(len(height)):
            if i > 0:
                maxLeft[i] = max(height[i-1], maxLeft[i-1])
            if j < len(height) - 1:
                maxRight[j] = max(height[j+1], maxRight[j+1])
            j -= 1
        minLR = [min(maxLeft[i],  maxRight[i]) - height[i] if (min(maxLeft[i],  maxRight[i]) - height[i] > 0) else 0 for i in range(len(height))]
        return sum(minLR)