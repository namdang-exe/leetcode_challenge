class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        meetings = []
        for s, e in intervals:
            meetings.append((s,"start"))
            meetings.append((e, "end"))
        meetings.sort()
        count = 0
        for meeting in meetings:
            status = meeting[1]
            if status == "start":
                count += 1
            else:
                count -= 1
            if count > 1:
                return False
        return True
