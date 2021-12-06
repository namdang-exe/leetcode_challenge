class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def change_pos(pos, cur_dir):
            if cur_dir == 0: pos[1] += 1
            elif cur_dir == 1: pos[0] += 1
            elif cur_dir == 2: pos[1] -= 1
            else: pos[0] -= 1
            return pos
        
        def change_dir(cur_dir, d):
            if d == "L":
                if cur_dir == 0:
                    cur_dir = 3
                else:
                    cur_dir -= 1
            if d == "R":
                if cur_dir == 3:
                    cur_dir = 0
                else:
                    cur_dir += 1
            return cur_dir
        
        cur_pos = [0,0]  # (x,y)
        cur_dir = 0
        # carry out instructions
        for i in instructions:
            if i == "G":
                cur_pos = change_pos(cur_pos, cur_dir)
            else:
                cur_dir = change_dir(cur_dir, i)
        # check if it's a cycle
        if cur_pos == [0,0]:
            return True
        else:
            if cur_dir != 0:
                return True
        return False
