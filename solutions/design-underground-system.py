class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [stationName,t,None]
        if not  stationName in self.stations:
            self.stations[stationName] = {}
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_s = self.customers[id][0]
        start_t = self.customers[id][1]
        time_diff = t - start_t
        if stationName in self.stations[start_s]:
            self.stations[start_s][stationName].append(time_diff)
        else:
            self.stations[start_s][stationName] = [time_diff]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot = sum(self.stations[startStation][endStation])
        n = len(self.stations[startStation][endStation])
        return tot/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)