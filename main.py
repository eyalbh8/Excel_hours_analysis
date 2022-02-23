from main_function import *

def execute():
   file_name = FileName.get()
   ari_days = ari_var.get()
   gilat_days = gilat_var.get()
   main(file_name, ari_days, gilat_days)

window = tk.Tk()
window.title("בס''ד")

FileName = tk.StringVar()
FileName_label = tk.Label(window, text = "File's name", font=('calibre',16, 'bold'))
FileName_label.grid(row=0,column=1)
FileName_entry = tk.Entry(window,textvariable = FileName, font=('calibre',16,'normal'))
FileName_entry.grid(row=1,column=1)

ari_var = tk.IntVar()
ari_label = tk.Label(window, text ="Ari's days", font=('calibre', 16, 'bold'))
ari_label.grid(row=2, column=1)
ari_entry = tk.Entry(window, textvariable = ari_var, font=('calibre', 16, 'normal'))
ari_entry.grid(row=3, column=1)

gilat_var = tk.IntVar()
gilat_label = tk.Label(window, text ="Gilat's days", font=('calibre', 16, 'bold'))
gilat_label.grid(row=4, column=1)
gilat_entry = tk.Entry(window, textvariable = gilat_var, font=('calibre', 16, 'normal'))
gilat_entry.grid(row=5, column=1)

end = tk.Button(window,bg="black", fg="white",text="סיים",command=execute)
end.grid(row=6,column=1)

window.mainloop()