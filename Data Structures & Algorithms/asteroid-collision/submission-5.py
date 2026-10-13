class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Process collisions until no more can happen
            while stack and stack[-1] > 0 and asteroid < 0:
                # Compare current asteroid with the one on top of stack
                if stack[-1] < abs(asteroid):
                    # Top asteroid is destroyed, pop it and continue
                    stack.pop()
                    # Keep the while loop going to check next asteroid
                elif stack[-1] == abs(asteroid):
                    # Both are destroyed
                    stack.pop()
                    asteroid = None  # Mark current as destroyed
                    break
                else:  # stack[-1] > abs(asteroid)
                    # Current asteroid is destroyed
                    asteroid = None
                    break
            
            # If current asteroid survived all collisions, add it to stack
            if asteroid is not None:
                stack.append(asteroid)
        
        return stack