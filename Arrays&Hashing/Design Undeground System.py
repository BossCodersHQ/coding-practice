from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.journey_map = {}
        self.duration_map = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        assert id not in self.journey_map
        self.journey_map[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        assert id in self.journey_map
        startStation, startTime = self.journey_map.pop(id)
        duration = endTime - startTime
        self.duration_map[(startStation, endStation)].append(duration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.duration_map[(startStation, endStation)]
        averageTime = sum(times) / len(times)
        return averageTime


# journey_map = {45:(Leyton,3), 32:(Paradise,8), 27:(Leyton,10)}
# duration_map = {(Leyton, Waterloo):[15]}

# When you see id that is already in journey map
# calculate duration and add to the duration map
# make sure to dlete journey from the journey map


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
