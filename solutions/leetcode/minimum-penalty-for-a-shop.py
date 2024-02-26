class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        yes, no = [0]*(n+1),[0]*(n+1)
        for i,ch in enumerate(customers):
            if ch == "Y":
                yes[i] = 1
            else:
                no[i+1] = 1

        for i in range(1,n+1):
            yes[(n+1) - i - 1] += yes[n - i + 1]
            no[i] += no[i - 1]
        penality = [x + y for x,y in zip(yes,no)]

        idx = 0
        for i in range(n+1):
            if penality[i] < penality[idx]:
                idx = i

        return idx
        