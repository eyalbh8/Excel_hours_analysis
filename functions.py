import tkinter as tk
from Excel_functions import *
from Analyzing_hours import *


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
