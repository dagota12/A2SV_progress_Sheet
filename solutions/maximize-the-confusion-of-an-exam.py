class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq_t  = defaultdict(int)
        freq_f = defaultdict(int)
        l = 0
        max_ = 1
        for r in range(len(answerKey)):
            freq_t[answerKey[r]] += 1
            while answerKey[r] == 'F' and freq_t[answerKey[r]] > k:
                freq_t[answerKey[l]] -= 1
                l += 1
            max_ = max(max_,r - l + 1)
        l = 0
        for r in range(len(answerKey)):
            freq_f[answerKey[r]] += 1
            while l < len(answerKey) and answerKey[r] == 'T' and freq_f[answerKey[r]] > k:
                freq_f[answerKey[l]] -= 1
                l += 1
            max_ = max(max_,r - l + 1)
        return max_

            