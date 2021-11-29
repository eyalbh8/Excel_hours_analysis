import tkinter as tk
from Excel_anlyzing_data import Check_Medicine_index
from Excel_writing import Save_Changes, Save_New_Medicine, Max_Row
from Excel_reading import Extracting_Medicine_Name,Read_File
from GUI_Functions import Print_Executed


def Updating_Data_Base():
    List_of_names = Extracting_Medicine_Name(Read_File("Medicine_inventory.xlsx"))
    Medicine_index =  Check_Medicine_index(Medicine_name.get(), List_of_names)

    if Medicine_index is not False:
        Save_Changes(Medicine_index, Expiration_date.get(), Quantity.get(), Minimum_inventory.get())
        Print_Executed()
    else:
        New_Medicine_Row_num = Max_Row() + 1
        Save_New_Medicine(New_Medicine_Row_num, Medicine_name.get(), 
                          Expiration_date.get(), Quantity.get(), Minimum_inventory.get())
        Print_Executed()

window = tk.Tk()
window.title("עדכון תרופות")

Medicine_name = tk.StringVar(window)
Medicine_name_label = tk.Label(window, text = "שם התרופה", font=('calibre',14, 'bold'))
Medicine_name_label.grid(row=0,column=4)
Medicine_name_entry = tk.Entry(window,textvariable = Medicine_name, font=('calibre',14,'normal'))
Medicine_name_entry.grid(row=1,column=4)

Quantity = tk.IntVar()
Quantity_label = tk.Label(window, text = "כמות", font=('calibre',10, 'bold'))
Quantity_label.grid(row=0,column=3)
Quantity_entry = tk.Entry(window,textvariable = Quantity, font=('calibre',10,'normal'))
Quantity_entry.grid(row=1,column=3)

Minimum_inventory = tk.IntVar()
Minimum_inventory_label = tk.Label(window, text = "כמות מינימום", font=('calibre',10, 'bold'))
Minimum_inventory_label.grid(row=0,column=2)
Minimum_inventory_entry = tk.Entry(window,textvariable = Minimum_inventory, font=('calibre',10,'normal'))
Minimum_inventory_entry.grid(row=1,column=2)

Expiration_date = tk.StringVar(window)
Expiration_date_label = tk.Label(window, text = "תאריך תפוגה", font=('calibre',10, 'bold'))
Expiration_date_label.grid(row=0,column=1)
Expiration_date_entry = tk.Entry(window,textvariable = Expiration_date, font=('calibre',10,'normal'))
Expiration_date_entry.grid(row=1,column=1)

end = tk.Button(window,bg="black", fg="white",text="סיים",command=Updating_Data_Base)
end.grid(row=2,column=2)

window.mainloop()