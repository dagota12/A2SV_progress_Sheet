class Bitset:

    def __init__(self, size: int):
        self.bits = ['0']*size
        self.inv = ['1']*size
        self.size = size
        self.ones = 0
        self.zeros = size

    def fix(self, idx: int) -> None:
        if self.bits[idx] == '0':
            
            self.bits[idx] = '1'
            self.inv[idx] = '0'
            
            self.ones+=1
            self.zeros-=1
            



    def unfix(self, idx: int) -> None:
        if self.bits[idx] == '1':
           
            self.bits[idx] = '0'
            self.inv[idx] = '1'
            
            self.zeros+=1
            self.ones-=1
            


    def flip(self) -> None:
        self.inv,self.bits = self.bits,self.inv
        
        temp = self.ones
        self.ones = self.zeros
        self.zeros = temp
       


    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()