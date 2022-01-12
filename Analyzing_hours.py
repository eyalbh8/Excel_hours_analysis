def meetingHours(meeting):
    meetingList = meeting.split("-")
    meetings_BeginList = meetingList[0].split(":")
    meetings_EndsList = meetingList[1].split(":")

    if int(meetings_BeginList[0]) < 8:
        return False

    elif int(meetings_BeginList[0]) < int(meetings_EndsList[0]):
        calculateHours = int(meetings_EndsList[0]) - int(meetings_BeginList[0])
        return int(calculateHours)
    
    else:
        return 0
       
    
def meetingMinutes(meeting):
    meetingList = meeting.split("-")
    meetings_EndsList = meetingList[1].split(":")
    meetings_BeginList = meetingList[0].split(":")

    calculateMinutes = int(meetings_EndsList[1]) - int(meetings_BeginList[1])
    return int(calculateMinutes)

def CalculateHoursMintues(hours=0, minutes=0, totalHours=0):
    if minutes < 0:
        hours -= 1
        minutes = 60 + minutes
      
    totalHours = hours + minutes/60
    return(totalHours)
    