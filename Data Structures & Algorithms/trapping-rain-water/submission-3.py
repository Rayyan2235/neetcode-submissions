class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        GOAL: Find max area of water
        Pattern: 2 Pointers for best memeory space and time
        Logic: Understand the formula to get the water at specific height[i] shown below
        What tripped me up: Wasnt too sure how to calculate the trapped water, cuz the prev q
            we used area formula, but its irregular. But we realized that we could just the formula below
            as the max_L/max_R can act as the barricade
        ANOTHER THING THAT TRIPPED ME UP: You were confused because you thought trapped water height depends on the immediate bar next to the water,
but in reality it depends on the tallest bar on each side (max_L, max_R), not just the neighbor’s height.

Even if the nearest bar is short, a taller bar farther away still acts as a barricade to hold the water.
        



        '''
        if not height:
            return 0


        l = 0
        r = len(height) - 1
        max_L = height[l]
        max_R = height[r]
        res = 0 # Used to track how many squares of water trapped

        while l < r:
            
            if max_L < max_R:
                l += 1
                max_L = max(max_L, height[l]) # if the max_L doesnt change then it means that there is water trapped 
                #because it means that there is a max_L to its left so thats helping trap water for that vertical bar

                res += max_L - height[l] # This is the formula, its just subtracting the heights of both the places
                #This is basically the area formula as the base always remains 1, but the height is dependent on max_L therefore always x * 1


            else:
                r-= 1
                max_R = max(max_R, height[r])
                res += max_R - height[r]
           
        return res
        