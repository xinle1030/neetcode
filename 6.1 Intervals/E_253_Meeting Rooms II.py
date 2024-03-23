"""
References: https://www.youtube.com/watch?v=FdzJmTCVyJU
"""

# Definition of Interval
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals 
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms (self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # pointers for start and end arr respectively
        s, e = 0, 0

        res, count = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1 # meeting just start
                s += 1
            else:
                e += 1
                count -= 1 # meeting end
            res = max(count, res)
        
        return res

mySol = Solution()
intervals = [
    Interval(0, 30),
    Interval(5, 10),
    Interval(15, 20)
]
print(mySol.minMeetingRooms(intervals))