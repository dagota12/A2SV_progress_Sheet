class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.curr_winner = []
        self.times = times.copy()
        self.vote = collections.defaultdict(int)
        self.current_winner = 0

        for i in range(len(times)):
            self.vote[persons[i]] += 1
            if self.vote[persons[i]] >= self.current_winner:
                self.curr_winner.append(persons[i])
                self.current_winner = self.vote[persons[i]]
            else:
                self.curr_winner.append(self.curr_winner[-1])

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times,t)
        return self.curr_winner[idx-1]