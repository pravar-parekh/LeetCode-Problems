class HitCounter:

    def __init__(self):
        self.queue = []
        self.hits = 0

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        self.hits += 1
        while(self.queue[-1] - self.queue[0] > 300):
            self.queue.pop(0)
            self.hits -= 1
        
    def getHits(self, timestamp: int) -> int:
        if self.queue == []:
            return self.hits
        
        while(self.queue and timestamp - self.queue[0] >= 300):
            self.queue.pop(0)
            self.hits -= 1

        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)