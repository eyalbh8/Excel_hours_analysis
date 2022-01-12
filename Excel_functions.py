import pandas as pd
import numpy as np

def readFile(file):
    df = pd.read_excel(file)
    return df

def check_type(var):
    if type(var) is str and var != "OutLook לא ידוע" and var != "*":
        return True
    else:
        return False

def Extracting_HoursData(df):
    ColumnsHeadlines = df.columns.ravel()
    meetingsTime = df[ColumnsHeadlines[len(ColumnsHeadlines) - 1]]
    Times = pd.DataFrame(meetingsTime)

    ListOf_MeetingsHours = []
    for row in Times.iterrows():
        if check_type(row[1][0]):
            ListOf_MeetingsHours.append(row)
        else:
            row[1][0] = np.nan
            ListOf_MeetingsHours.append(row[1][0])

    ListOf_MeetingsHours = pd.DataFrame(ListOf_MeetingsHours)

    return ListOf_MeetingsHours


def CustomersNames_List(df):
    ColumnsHeadlines = df.columns.ravel()
    CustomerName = df[ColumnsHeadlines[len(ColumnsHeadlines) - 2]]
    Names = pd.DataFrame(CustomerName)

    ListOf_Names = [row for row in Names.iterrows()]

    return ListOf_Names