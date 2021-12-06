class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        dx,dy = 0, 1
        # carry out instructions
        for d in instructions:
            if d == "G":
                x, y = x + dx, y + dy
            elif d == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        # check if it's a cycle
        if x == 0 and y == 0:
            return True
        else:
            if dx != 0 or dy != 1:
                return True
        return False
