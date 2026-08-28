class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one_step_behind, two_steps_behind = 2, 1
        
        for _ in range(3, n + 1):
            current_ways = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current_ways
            
        return one_step_behind