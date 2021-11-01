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
