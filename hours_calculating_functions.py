"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
Created By  : Eyal Ben-Chaim
Created Date: 11/2021
"""

import tkinter as tk
from analyzing_hours import *
from excel_data_extracting_functions import *


def calculating_meetings_total_length(meeting_time, total_hours):
    if check_variable_type(meeting_time):

        hours = calculate_meeting_hours(meeting_time)
        minutes = calculate_meeting_minutes(meeting_time)

        if hours is False:
            print(total_hours)
            return total_hours

        else:
            total_hours += calculate_meeting_length(hours, minutes)
            print((calculate_meeting_length(hours, minutes)))
            print(total_hours)
            return total_hours

    else:
        print(total_hours)
        return total_hours


def calculating_each_doctor_hours(file_name, ari_days, gilat_days):
    df = read_file(str(file_name))
    df = remove_unnecessary_row(df)

    meetings_hours_list = get_hours_data(df)

    names = get_customers_names_list(df)

    total_hours_ari = 0
    total_hours_gilat = 0
    total_hours_emergency = 0
    count_days = 0

    for meeting in meetings_hours_list.iterrows():
        try:
            meeting_time = meeting[1][1][0]
            meeting_line = int(meeting[1][0])
            name = names[meeting_line][1][0]

        except:
            count_days += 1
            meeting_time = 0
            name = 0


        if count_days < ari_days:

            if check_variable_type(name):
                total_hours_ari = calculating_meetings_total_length(meeting_time, total_hours_ari)

            else:
                pass

        elif ari_days <= count_days < gilat_days + ari_days:
            if check_variable_type(name):
                total_hours_gilat = calculating_meetings_total_length(meeting_time, total_hours_gilat)

            else:
                pass

        else:
            if check_variable_type(name):
                total_hours_emergency = calculating_meetings_total_length(meeting_time, total_hours_emergency)

            else:
                pass

    print_result(total_hours_ari, total_hours_gilat, total_hours_emergency)
    return total_hours_ari, total_hours_gilat, total_hours_emergency




def print_result(total_hours_ari, total_hours_gilat, total_hours_emergency):
    window = tk.Tk()
    window.title("GO ILANA!!")

    result_label = tk.Label(window, text="Result", font=('calibre', 14, 'bold'))
    result_label.grid(row=0, column=1)

    ari_label = tk.Label(window, text="Ari's hours:", font=('calibre', 14, 'bold'))
    ari_label.grid(row=2, column=0)

    ari_result_label = tk.Label(window, text=str(total_hours_ari), font=('calibre', 14, 'bold'))
    ari_result_label.grid(row=2, column=2)

    gilat_label = tk.Label(window, text="Gilat's hours:", font=('calibre', 14, 'bold'))
    gilat_label.grid(row=3, column=0)

    gilat_result_label = tk.Label(window, text=str(total_hours_gilat), font=('calibre', 14, 'bold'))
    gilat_result_label.grid(row=3, column=2)

    emergency_label = tk.Label(window, text="Emergency room hours:", font=('calibre', 14, 'bold'))
    emergency_label.grid(row=4, column=0)

    ari_result_label = tk.Label(window, text=str(total_hours_emergency), font=('calibre', 14, 'bold'))
    ari_result_label.grid(row=4, column=2)

    window.mainloop()
