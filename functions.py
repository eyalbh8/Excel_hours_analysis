import pandas as pd
import tkinter as tk

def readFile(file):
    df = pd.read_excel(file)
    return df

def Extracting_HoursData(df):
    ColumnsHeadlines = df.columns.ravel()
    meetingsTime = df[ColumnsHeadlines[6]]
    Times = pd.DataFrame(meetingsTime)

    ListOf_MeetingsHours = [row for row in Times.iterrows()]

    return ListOf_MeetingsHours

def CustomersNames_List(df):
    ColumnsHeadlines = df.columns.ravel()
    CustomerName = df[ColumnsHeadlines[5]]
    Names = pd.DataFrame(CustomerName)

    ListOf_Names = [row for row in Names.iterrows()]

    return ListOf_Names

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

def check_type(var):
    if type(var) is str and var != "OutLook לא ידוע":
        return True
    else:
        return False
        
def DoctorHours(meetingTime, totalHours):
    if check_type(meetingTime):

        hours = meetingHours(meetingTime)
        minutes = meetingMinutes(meetingTime)

        totalHours += CalculateHoursMintues(hours,minutes)
        return totalHours
    
    else:
        return totalHours

def Main(fileName, Ari_LastLine, Gilat_LastLine):

    df = readFile(str(fileName))

    meetingsList = Extracting_HoursData(df)

    names = CustomersNames_List(df)

    totalHours_Ari = 0
    totalHours_Gilat = 0
    totalHours_Emergency = 0

    for meeting in meetingsList:
        meetingTime = meeting[1][0]
        meetingLine = int(meeting[0])

        name = names[meetingLine][1][0]

        if meetingLine < Ari_LastLine:
       
            if check_type(name):
                totalHours_Ari = DoctorHours(meetingTime, totalHours_Ari)
      
            else:
                pass
    
        elif Ari_LastLine < meetingLine < Gilat_LastLine:
            if check_type(name):
                totalHours_Gilat = DoctorHours(meetingTime, totalHours_Gilat)
      
            else:
               pass

        else:
            if check_type(name):
                totalHours_Emergency = DoctorHours(meetingTime, totalHours_Emergency)
      
            else:
                pass

    printResult(totalHours_Ari, totalHours_Gilat, totalHours_Emergency)

def printResult(totalHours_Ari, totalHours_Gilat, totalHours_Emergency):
    window = tk.Tk()
    window.title("GO ILANA!!")

    Result_label = tk.Label(window, text = "Result", font=('calibre',14, 'bold'))
    Result_label.grid(row=0,column=1)

    Ari_label = tk.Label(window, text = "Ari's hours:", font=('calibre',14, 'bold'))
    Ari_label.grid(row=2,column=0)

    AriResult_label = tk.Label(window, text = str(totalHours_Ari), font=('calibre',14, 'bold'))
    AriResult_label.grid(row=2,column=2)

    Gilat_label = tk.Label(window, text = "Gilat's hours:", font=('calibre',14, 'bold'))
    Gilat_label.grid(row=3,column=0)

    GilatResult_label = tk.Label(window, text = str(totalHours_Gilat), font=('calibre',14, 'bold'))
    GilatResult_label.grid(row=3,column=2)

    Emergency_label = tk.Label(window, text = "Emergency room hours:", font=('calibre',14, 'bold'))
    Emergency_label.grid(row=4,column=0)

    AriResult_label = tk.Label(window, text = str(totalHours_Emergency), font=('calibre',14, 'bold'))
    AriResult_label.grid(row=4,column=2)

    window.mainloop()

