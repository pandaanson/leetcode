class SmallestInfiniteSet:

    def __init__(self):
        self.list=[i for i in range(1,100)]
        self.currentsmallest=100
        self.takenaway: {int} = set()
        

    def popSmallest(self) -> int:
        temp=heapq.heappop(self.list)
        self.takenaway.add(temp)
        if not self.list:
            self.list+=[i for i in range(self.currentsmallest,self.currentsmallest+100)]
            self.currentsmallest+=100
        return temp


    def addBack(self, num: int) -> None:
        if num<self.currentsmallest and num in self.takenaway:
            
            heapq.heappush(self.list,num)
            self.takenaway.remove(num)
        
