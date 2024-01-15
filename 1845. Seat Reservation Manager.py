class SeatManager:

    def __init__(self, n: int):
        self.avseat=[i for i in range(1,n+1)]


    def reserve(self) -> int:
        return  heapq.heappop(self.avseat)


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.avseat,seatNumber)
