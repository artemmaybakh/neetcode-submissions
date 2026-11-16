class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:       
            
        d = {position[i]: (target - position[i]) / speed[i] for i in range(len(position))}
        
        times = [d[k] for k in sorted(d)][::-1]
        
        
        
        
        
        maxi = 0
        group = 0
        
        for i in range(len(times)):
            if times[i] > maxi:
                group += 1
                maxi = times[i]
            
        return group
        