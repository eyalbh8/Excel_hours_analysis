import pandas as pd


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