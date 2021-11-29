import tkinter as tk
from Excel_reading import Extracting_Medicine_Name, Read_File
from GUI_Functions import *
from Excel_anlyzing_data import Check_Medicine_index


def Apply():
    Excel_Workbook = load_workbook(filename = "Medicine_inventory.xlsx")
    sheet = Excel_Workbook["mainSheet"]

    index = Check_Medicine_index(value_inside.get(), List_of_Names)
    Cell_position = "C" + str(index)
    cell = sheet[Cell_position].value
    sheet[Cell_position] = int(cell) - Quantity_var.get()

    if Check_Minimum_Inventory(sheet[Cell_position].value, sheet["D" + str(index)].value):
        pass

    else:
        Print_min(value_inside.get())

    Excel_Workbook.save("Medicine_inventory.xlsx")

    Print_Executed()


def Update_file():
    import Add_Medicine


List_of_Names = Extracting_Medicine_Name(Read_File("Medicine_inventory.xlsx"))
    
window = tk.Tk()
window.title("בס''ד")

value_inside = tk.StringVar(window)
value_inside.set("רשימת תרופות")

option_menu = tk.OptionMenu(window, value_inside, *List_of_Names)
option_menu.grid(row=1,column=1)

Quantity_var = tk.IntVar()
Quantity_label = tk.Label(window, text = "Quantity", font=('calibre',14, 'bold'))
Quantity_label.grid(row=0,column=0)
Quantity_entry = tk.Entry(window,textvariable = Quantity_var, font=('calibre',14,'normal'))
Quantity_entry.grid(row=1,column=0)

submit_button = tk.Button(window, text='סיום', command=Apply)
submit_button.grid(row=2, column=1)

Update_file_button = tk.Button(window, text='עדכון מלאי', command=Update_file)
Update_file_button.grid(row=2, column=0 )

    
window.mainloop()
    