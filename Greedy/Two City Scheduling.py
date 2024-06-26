from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        total = 0
        numa = numb = 0
        for i in range(len(costs)):
            costa, costb = costs[i]
            if numa == len(costs) / 2:
                final = [cost[1] for cost in costs[i:]]
                total += sum(final)
                break
            if numb == len(costs) / 2:
                final = [cost[0] for cost in costs[i:]]
                total += sum(final)
                break

            if costa < costb:
                numa += 1
                total += costa
            else:
                numb += 1
                total += costb
        return total


if __name__ == "__main__":
    s = Solution()
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    assert s.twoCitySchedCost(costs) == 110
    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    assert s.twoCitySchedCost(costs) == 1859
