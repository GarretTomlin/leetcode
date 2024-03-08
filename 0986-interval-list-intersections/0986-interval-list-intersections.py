from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, start, end = 0, 0, 0, 1
        results = []

        while i < len(firstList) and j < len(secondList):
            overlapFirstList = (firstList[i][start] >= secondList[j][start] and
                                firstList[i][start] <= secondList[j][end])

            overlapSecondList = (secondList[j][start] >= firstList[i][start] and
                                 secondList[j][start] <= firstList[i][end])

            if overlapFirstList or overlapSecondList:
                results.append([max(firstList[i][start], secondList[j][start]),
                                min(firstList[i][end], secondList[j][end])])

            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1

        return results
