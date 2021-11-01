from functions import *

df = readFile()

meetingsList = ExtractingData(df)

totalHours_Ari = 0
totalHours_Gilat = 0
totalHours_Emergency = 0

for meeting in meetingsList:
    meetingTime = meeting[1][0]
    meetingLine = int(meeting[0])

    if meetingLine < 211:
       totalHours_Ari = ArisHours(meetingTime, totalHours_Ari)
    
    elif 211 < meetingLine < 480:
       totalHours_Gilat = GilatsHours(meetingTime, totalHours_Gilat)

    else:
        totalHours_Emergency = EmergencysHours(meetingTime, totalHours_Emergency)

print("Ari's hours {} \n Gilat's hours {} \n emergency hours {}".format(totalHours_Ari, totalHours_Gilat, totalHours_Emergency))