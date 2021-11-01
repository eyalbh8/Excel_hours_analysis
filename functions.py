import pandas as pd

def readFile():
    df = pd.read_excel("chalender.xlsx")
    return df

def ExtractingData(df):
    ColumnsHeadlines = df.columns.ravel()
    meetingsTime = df[ColumnsHeadlines[6]]
    Times = pd.DataFrame(meetingsTime)

    ListOf_MeetingsHours = [row for row in Times.iterrows()]

    return ListOf_MeetingsHours

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
        
    elif hours < 0:
        if minutes < 0:
            if hours == -1:
                if minutes >= -30:
                    totalMinutes += -1 * minutes
                else: 
                    totalMinutes += 60 + minutes
            else:
                hours += (-1 * hours) - 1
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

def check_type(var):
    if type(var) is str:
        return True
    else:
        return False
        
def ArisHours(meetingTime, totalHours_Ari):
    if check_type(meetingTime):

        hours = meetingHours(meetingTime)
        minutes = meetingMinutes(meetingTime)

        totalHours_Ari += CalculateHoursMintues(hours,minutes)
        return totalHours_Ari
    
    else:
        return totalHours_Ari

def GilatsHours(meetingTime, totalHours_Gilat):
    if check_type(meetingTime):

        hours = meetingHours(meetingTime)
        minutes = meetingMinutes(meetingTime)

        totalHours_Gilat += CalculateHoursMintues(hours,minutes)
        return totalHours_Gilat
    
    else:
        return totalHours_Gilat

def EmergencysHours(meetingTime, totalHours_emergency):
    if check_type(meetingTime):

        hours = meetingHours(meetingTime)
        minutes = meetingMinutes(meetingTime)

        totalHours_emergency += CalculateHoursMintues(hours,minutes)
        return totalHours_emergency
    
    else:
        return totalHours_emergency
