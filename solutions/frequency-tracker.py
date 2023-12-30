class FrequencyTracker:

    def __init__(self):
        """
        initialize the class by setting a numbers frequency counter 
        and frequency counter
        
        """
        self.nums_frequncy = defaultdict(int)
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:
        oldf = self.nums_frequncy[number] # old fequency before update
        # update the frequncy were number was
        self.frequencies[oldf] -= 1 
        # increment the  frequency
        self.nums_frequncy[number] += 1
        # increment the frecuency count where number is now in
        newf = self.nums_frequncy[number]
        self.frequencies[newf] += 1

    def deleteOne(self, number: int) -> None:
        # check if <number> appeare at least once  
        if  number in self.nums_frequncy and self.nums_frequncy[number] > 0:
            oldf = self.nums_frequncy[number]
            self.frequencies[oldf] -= 1
            
            self.nums_frequncy[number] -= 1
            
            newf = self.nums_frequncy[number]
            self.frequencies[newf] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)