class Robot:

    def __init__(self, width: int, height: int):
        self.dir = 1
        self.dirs = {0:1, 1:1, 2:-1, 3:-1}
        self.width = width
        self.height = height
        self.perim = height*2 + width*2 - 4
        self.pos = [0,0]
        self.dir_names = {0:"North",1:"East",2:"South",3:"West"}
    def step(self, num: int) -> None:
        num = num % self.perim
        if(num == 0):
            num = self.perim
        while(num > 0):
            if self.dir in [1,3]:
                curr_pos = self.pos[0] + self.dirs[self.dir]
                if curr_pos < 0:
                    self.dir = 2
                    continue
                elif curr_pos >= self.width:
                    self.dir = 0
                    continue
                self.pos[0] = curr_pos
            elif self.dir in [0,2]:
                curr_pos = self.pos[1] + self.dirs[self.dir]
                if curr_pos < 0:
                    self.dir = 1
                    continue
                elif curr_pos >= self.height:
                    self.dir = 3
                    continue 
                self.pos[1] = curr_pos           
            num-=1

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir_names[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()