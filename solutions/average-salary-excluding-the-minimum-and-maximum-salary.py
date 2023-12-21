class Solution:
    def average(self, salary: List[int]) -> float:
        mx = max(salary)
        mi = min(salary)
        l = len(salary)-2
        tot = sum(salary) - mx - mi
        avg = tot/l
        return avg