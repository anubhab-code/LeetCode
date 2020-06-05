class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs= sorted(costs, key = lambda x:x[0]-x[1])
        cost=0
        for i in range(int(len(costs)/2)):
            cost = cost + costs[i][0]
        for i in range(int(len(costs)/2), len(costs)):
            cost = cost + costs[i][0]
        return cost