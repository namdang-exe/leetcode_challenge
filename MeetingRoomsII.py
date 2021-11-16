# Idea:
# calculate how many meetings 
# are going on at the same time
# Tips: draw it out
# check the start and stop of the meeting
# if a meeting already started 
# and then another meeting starts,
# this means we have 2 meetings going at the same time
# create a count to keep track
# create a max count for how many meetings/ max room we need
# for some meetings, the end time = the start time of other meeting
# prioritize the end time
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [(time, start/stop)]
        meetings = []
        for start, stop in intervals:
            # start, stop is time
            meetings.append((start, "start"))
            meetings.append((stop, "end"))
        meetings.sort() # O(nlogn)
        max_count = float('-inf')
        count = 0
        for meeting in meetings:
            status = meeting[1]
            if status == "start":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
            
        return max_count
