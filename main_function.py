import tkinter as tk
from analyzing_hours import *
from excel_functions import *
        
def doctor_hours(meeting_time, total_hours):
    if check_type(meeting_time):

        hours = meeting_hours(meeting_time)
        minutes = meeting_minutes(meeting_time)

        if hours is False:
            return total_hours
        
        else:
            total_hours += calculate_hours_minutes(hours, minutes)
            return total_hours
    
    else:
        return total_hours

def main(file_name, ari_days, gilat_days):

    df = read_file(str(file_name))
    df = remove_unnecessary_row(df)

    meetings_hours_list = extracting_hours_data(df)

    names = customers_names_list(df)

    total_hours_ari = 0
    total_hours_gilat = 0
    total_hours_emergency = 0
    count_days = 0

    for meeting in meetings_hours_list.iterrows():
        try:
            meeting_time = meeting[1][1][0]
            meeting_line = int(meeting[1][0])
            name = names[meeting_line][1][0]
        
        except ValueError:
            count_days += 1
            meeting_time = 0
            name = 0
   
        if count_days < ari_days:
       
            if check_type(name):
                total_hours_ari = doctor_hours(meeting_time, total_hours_ari)
      
            else:
                pass
    
        elif ari_days <= count_days < gilat_days + ari_days:
            if count_days == ari_days:
                print(meeting, name)

            if check_type(name):
                total_hours_gilat = doctor_hours(meeting_time, total_hours_gilat)
      
            else:
               pass

        else:
            if count_days == gilat_days + ari_days:
                print(meeting, name)

            if check_type(name):
                total_hours_emergency = doctor_hours(meeting_time, total_hours_emergency)
      
            else:
                pass
        
    print_result(total_hours_ari, total_hours_gilat, total_hours_emergency)

def print_result(total_hours_ari, total_hours_gilat, total_hours_emergency):
    window = tk.Tk()
    window.title("GO ILANA!!")

    result_label = tk.Label(window, text = "Result", font=('calibre',14, 'bold'))
    result_label.grid(row=0,column=1)

    ari_label = tk.Label(window, text = "Ari's hours:", font=('calibre',14, 'bold'))
    ari_label.grid(row=2,column=0)

    ari_result_label = tk.Label(window, text = str(total_hours_ari), font=('calibre', 14, 'bold'))
    ari_result_label.grid(row=2,column=2)

    gilat_label = tk.Label(window, text = "Gilat's hours:", font=('calibre',14, 'bold'))
    gilat_label.grid(row=3,column=0)

    gilat_result_label = tk.Label(window, text = str(total_hours_gilat), font=('calibre', 14, 'bold'))
    gilat_result_label.grid(row=3,column=2)

    emergency_label = tk.Label(window, text = "Emergency room hours:", font=('calibre',14, 'bold'))
    emergency_label.grid(row=4,column=0)

    ari_result_label = tk.Label(window, text = str(total_hours_emergency), font=('calibre', 14, 'bold'))
    ari_result_label.grid(row=4,column=2)

    window.mainloop()