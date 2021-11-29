import pandas as pd

def Read_File(file):
    df = pd.read_excel(file)
    return df

def Extracting_Medicine_Name(df):
    ColumnsHeadlines = df.columns.ravel()
    Medicine_Name = df[ColumnsHeadlines[0]]
    Names = pd.DataFrame(Medicine_Name)

    List_of_Names = [str(row[1][0]) for row in Names.iterrows()]

    return List_of_Names


def Extracting_Expiration_Date(df):
    ColumnsHeadlines = df.columns.ravel()
    Expiration_Dates = df[ColumnsHeadlines[1]]
    Dates = pd.DataFrame(Expiration_Dates)

    List_of_Dates = [str(row[1][0]) for row in Dates.iterrows()]

    return List_of_Dates


def Extracting_Quantity(df):
    ColumnsHeadlines = df.columns.ravel()
    Quantity = df[ColumnsHeadlines[2]]
    quantity = pd.DataFrame(Quantity)

    List_of_Quantity = [int(row[1][0]) for row in quantity.iterrows()]

    return List_of_Quantity


def Extracting_Minimum_Iventory(df):
    ColumnsHeadlines = df.columns.ravel()
    Minimum_Iventory = df[ColumnsHeadlines[3]]
    Inventory = pd.DataFrame(Minimum_Iventory)

    List_of_Inventory = [int(row[1][0]) for row in Inventory.iterrows()]

    return List_of_Inventory