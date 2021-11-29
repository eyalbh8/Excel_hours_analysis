from datetime import date

def Check_Medicine_index(name, List_of_names=[]):
    if str(name) in List_of_names:
        index = List_of_names.index(name)
        return index + 2
    
    else:
        return False


def Check_Minimum_Inventory(Quantity, Minimum):
    if int(Quantity) <= int(Minimum):
        return False

    else:
        return True

def Today_Date():
    today = str(date.today())
    today_List = today.split("-")
    today_List.reverse()
    return today_List
    

def Check_Expiratin_Date(Date):
    if Date == Today_Date():
        return False
    
    else:
        return True
    