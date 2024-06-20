from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        ptr1 = ptr2 = 0
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            slot1 = slots1[ptr1]
            slot2 = slots2[ptr2]
            # check for intersect
            if slot1[0] <= slot2[1] and slot1[1] >= slot2[0]:
                # find length of cross over
                start = max(slot1[0], slot2[0])
                end = min(slot1[1], slot2[1])
                # check if fulfills requirements
                if end - start >= duration:
                    return [start, start + duration]

            if slot1[1] > slot2[1]:
                ptr2 += 1
            else:
                ptr1 += 1
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.minAvailableDuration(
        [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8
    ) == [60, 68]
    assert (
        s.minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12
        )
        == []
    )
    assert (
        s.minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 15
        )
        == []
    )
    print("All tests passed")
