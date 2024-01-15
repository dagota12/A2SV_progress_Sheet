class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        frequency = defaultdict(int)
        l = 0
        min_len = float("inf")
        for r in range(len(cards)):
            frequency[cards[r]] += 1
            while frequency[cards[r]] > 1:
                frequency[cards[l]] -= 1
                min_len = min(min_len,r - l + 1)
                l += 1
        return min_len if min_len != float("inf") else -1
