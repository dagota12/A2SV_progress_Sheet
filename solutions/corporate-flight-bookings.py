class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        total_seats = [0]*n
        for l,r,seat in bookings:
            total_seats[l-1] += seat
            if r < n:
                total_seats[r] -= seat
        for i in range(1,n):
            total_seats[i] += total_seats[i-1]
        return total_seats