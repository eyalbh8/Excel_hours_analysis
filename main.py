#01.20 Ari < 154 < Gilat < 400
#02.20 Ari < 175 < Gilat < 430
#03.20 Ari < 167 < Gilat < 436

from functions import *

df = readFile("1.20.xlsx")

meetingsList = Extracting_HoursData(df)

names = CustomersNames_List(df)

totalHours_Ari = 0
totalHours_Gilat = 0
totalHours_Emergency = 0

for meeting in meetingsList:
   meetingTime = meeting[1][0]
   meetingLine = int(meeting[0])

   name = names[meetingLine][1][0]

   if meetingLine < 154:
       
      if check_type(name):
         totalHours_Ari = DoctorHours(meetingTime, totalHours_Ari)
      
      else:
         pass
    
   elif 154 < meetingLine < 400:
      if check_type(name):
         totalHours_Gilat = DoctorHours(meetingTime, totalHours_Gilat)
      
      else:
         pass

   else:
      if check_type(name):
         totalHours_Emergency = DoctorHours(meetingTime, totalHours_Emergency)
      
      else:
         pass

print("Ari's hours {} \n Gilat's hours {} \n emergency hours {}"
      .format(totalHours_Ari, totalHours_Gilat, totalHours_Emergency))