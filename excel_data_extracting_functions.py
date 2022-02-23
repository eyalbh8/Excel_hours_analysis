"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
Created By  : Eyal Ben-Chaim
Created Date: 11/2021
"""

import pandas as pd
import numpy as np


def read_file(file):
    df = pd.read_excel(file)
    return df


def remove_unnecessary_row(df):
    column_len = len(df.columns) - 1
    if df.columns[column_len] == f"Unnamed: {column_len}":
        return df.drop(0)

    else:
        return df


def check_variable_type(var):
    if type(var) is str and var != "OutLook לא ידוע" and var != "*":
        return True
    else:
        return False


def get_hours_data(df):
    columns_headlines = df.columns.ravel()
    meetings_time = df[columns_headlines[len(columns_headlines) - 1]]
    times = pd.DataFrame(meetings_time)

    list_of_meetings_hours = []
    for row in times.iterrows():
        if check_variable_type(row[1][0]):
            list_of_meetings_hours.append(row)
        else:
            row[1][0] = np.nan
            list_of_meetings_hours.append(row[1][0])

    list_of_meetings_hours = pd.DataFrame(list_of_meetings_hours)

    return list_of_meetings_hours


def get_customers_names_list(df):
    columns_head_lines = df.columns.ravel()
    customer_name = df[columns_head_lines[len(columns_head_lines) - 2]]
    names = pd.DataFrame(customer_name)

    list_of_names = [row for row in names.iterrows()]

    return list_of_names
