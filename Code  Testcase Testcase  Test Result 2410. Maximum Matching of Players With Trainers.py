class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans=pointer=0
        for i in players:
            while pointer<len(trainers) and trainers[pointer]<i:
                pointer+=1
            if pointer==len(trainers):
                return ans
            else:
                ans+=1
                pointer+=1
        return ans
