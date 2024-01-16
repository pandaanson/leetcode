class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)

        unitCount = 0

        for boxCount, unitsPerBox in boxTypes:
            count = min (truckSize, boxCount)
            unitCount += count * unitsPerBox
            truckSize -= count
            if truckSize == 0:
                break

        return unitCount
