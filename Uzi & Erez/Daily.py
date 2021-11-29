from Excel_reading import *
from Excel_anlyzing_data import Check_Expiratin_Date, Check_Minimum_Inventory
from GUI_Functions import Print_Expired, Print_min

def Daily_Check():
    file = Read_File("Medicine_inventory.xlsx")
    Medicine_names = Extracting_Medicine_Name(file)
    Dates = Extracting_Expiration_Date(file)
    Quantity = Extracting_Quantity(file)
    Minimum_inventory = Extracting_Minimum_Iventory(file)

    for date in Dates:
        date_list = date.split("/")
        if Check_Expiratin_Date(date_list):
            continue

        else:
            name = Medicine_names[Dates.index(date)]
            Print_Expired(name)

    for i in range(len(Quantity)):
        if Check_Minimum_Inventory(Quantity[i], Minimum_inventory[i]):
            continue

        else:
            Print_min(Medicine_names[i])

Daily_Check()