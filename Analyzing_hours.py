def meetingHours(meeting):

    meetingList = meeting.split("-")
    meetings_BeginList = meetingList[0].split(":")
    meetings_EndsList = meetingList[1].split(":")

    calculateHours = int(meetings_EndsList[0]) - int(meetings_BeginList[0])

    return int(calculateHours)
    
def meetingMinutes(meeting):

    meetingList = meeting.split("-")
    meetings_EndsList = meetingList[1].split(":")
    meetings_BeginList = meetingList[0].split(":")

    calculateMinutes = int(meetings_EndsList[1]) - int(meetings_BeginList[1])

    return int(calculateMinutes)

def CalculateHoursMintues(hours=0, minutes=0, totalHours=0, totalMinutes=0):

    if minutes < 0 and hours == 0:
        if minutes >= -30:
            totalMinutes += -1 * minutes
        else:
            totalMinutes += 60 + minutes
        
    elif minutes < 0 and hours > 0:
        if minutes >= -30:
            totalMinutes += -1 * minutes
        else:
            totalMinutes += 60 + minutes
            totalHours = hours -1
        
    elif hours < 0:
        if minutes < 0:
            if hours == -1:
                if minutes >= -30:
                    totalMinutes += -1 * minutes
                else: 
                    totalMinutes += 60 + minutes
            else:
                totalHours += (-1 * hours) - 1
                if minutes >= -30:
                    totalMinutes += -1 * minutes
                else: 
                    totalMinutes += 60 + minutes

        else:
            pass
            
    else:
        totalHours = hours
        totalMinutes += minutes

    totalMinutes = totalMinutes/60
    totalHours += totalMinutes
    return totalHours