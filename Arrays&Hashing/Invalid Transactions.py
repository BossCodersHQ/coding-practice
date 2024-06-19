from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        from collections import defaultdict

        transactions = [[ix] + t.split(",") for ix, t in enumerate(transactions)]
        transactions.sort(key=lambda t: int(t[2]))
        ledger = defaultdict(dict)
        invalid = set()
        for t in transactions:
            ix, name, time, amount, city = t
            slim_t = (time, amount, ix)
            # Checking 1st requirement
            if int(amount) > 1000:
                invalid.add((ix, name, time, amount, city))
            # Checking 2nd requirement
            for c in ledger[name]:
                if c == city:
                    continue  # Doesn't matter if it's in the same city
                prev_ts = ledger[name].get(c, [])
                # Loop through to find any invalid
                for i in range(len(prev_ts) - 1, -1, -1):
                    prev_time, prev_amount, prev_ix = prev_ts[i]

                    if int(prev_time) < int(time) - 60:
                        break
                    invalid.add((ix, name, time, amount, city))
                    invalid.add((prev_ix, name, prev_time, prev_amount, c))
            ledger[name][city] = ledger[name].get(city, []) + [slim_t]
        return [f"{t[1]},{t[2]},{t[3]},{t[4]}" for t in invalid]
