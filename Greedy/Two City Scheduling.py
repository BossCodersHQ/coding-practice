from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        print(costs)
        total = 0
        numa = numb = 0
        for i in range(len(costs)):
            costa, costb = costs[i]
            if numa == len(costs) / 2:
                final = [cost[1] for cost in costs[i:]]
                print("filling b", final)
                total += sum(final)
                break
            if numb == len(costs) / 2:
                final = [cost[0] for cost in costs[i:]]
                print("filling a", final)
                total += sum(final)
                break

            if costa < costb:
                numa += 1
                total += costa
                print("a", numa, costa, total)
            else:
                numb += 1
                total += costb
                print("b", numb, costb, total)
        return total
