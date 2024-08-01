class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        print(costs)
        
        for i in range(len(costs)):
            if (coins - costs[i] >= 0):
                coins -= costs[i]
                cnt += 1
            else:
                break
        
        return cnt