# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked, free, freq = [], list(range(n)), defaultdict(int)
        meetings.sort()

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)
            
            if free:
                room = heappop(free)
                heappush(booked, (end, room))
            else:
                release, room = heappop(booked)
                heappush(booked, (release + (end - start), room))
            
            freq[room] += 1

        return max(freq, key=freq.get)

