class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [0 for i in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunks[idKey-1] = value
        chunk = []
        for i in range(self.ptr,len(self.chunks)):
            if  self.chunks[i] == 0:
                break
            chunk.append(self.chunks[i])
            self.ptr += 1
        return chunk


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)