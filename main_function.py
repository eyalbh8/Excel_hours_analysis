import tkinter as tk
from Analyzing_hours import *
from Excel_functions import *
        
def DoctorHours(meetingTime, totalHours):
    if check_type(meetingTime):

        hours = meetingHours(meetingTime)
        minutes = meetingMinutes(meetingTime)

        if hours is False:
            return totalHours
        
        else:
            totalHours += CalculateHoursMintues(hours,minutes)
            return totalHours
    
    else:
        return totalHours

def Main(fileName, Ari_Days, Gilat_Days):

    df = readFile(str(fileName))

    Meetings_Hours_List = Extracting_HoursData(df)

    names = CustomersNames_List(df)

    totalHours_Ari = 0
    totalHours_Gilat = 0
    totalHours_Emergency = 0
    count_days = 0

    for meeting in Meetings_Hours_List.iterrows():
        try:
            meetingTime = meeting[1][1][0]
            meetingLine = int(meeting[1][0])
            name = names[meetingLine][1][0]
        
        except:
            count_days += 1
            meetingTime = 0
            meetingLine = np.nan 
            name = 0
   
        if count_days < Ari_Days:
       
            if check_type(name):
                totalHours_Ari = DoctorHours(meetingTime, totalHours_Ari)
      
            else:
                pass
    
        elif Ari_Days <= count_days < Gilat_Days + Ari_Days:
            if count_days == Ari_Days:
                print(meeting, name)

            if check_type(name):
                totalHours_Gilat = DoctorHours(meetingTime, totalHours_Gilat)
      
            else:
               pass

        else:
            if count_days == Gilat_Days + Ari_Days:
                print(meeting, name)

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