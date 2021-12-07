#01.21 Ari < 187 < Gilat < 419        #01.20 Ari < 154 < Gilat < 400
#02.21 Ari < 161 < Gilat < 375        #02.20 Ari < 175 < Gilat < 430
#03.21 Ari < 161 < Gilat < 428        #03.20 Ari < 167 < Gilat < 436
#04.21 Ari < 169 < Gilat < 407        #04.20 Ari < 100 < Gilat < 360
#05.21 Ari < 173 < Gilat < 419        #05.20 Ari < 154 < Gilat < 398
#06.21 Ari < 154 < Gilat < 414        #06.20 Ari < 222 < Gilat < 517
#07.21 Ari < 192 < Gilat < 450        #07.20 Ari < 189 < Gilat < 406
#08.21 Ari < 188 < Gilat < 495        #08.20 Ari < 171 < Gilat < 393
#09.21 Ari < 156 < Gilat < 383        #09.20 Ari < 162 < Gilat < 391
#10.21 Ari < 214 < Gilat < 488        #10.20 Ari < 163 < Gilat < 371
#11.21 Ari < 186 < Gilat < 403        #11.20 Ari < 213 < Gilat < 474
                                      #12.20 Ari < 193 < Gilat < 406
import tkinter as tk
from functions import *

def Execute():
   fileName = FileName.get()
   Ari_LastLine = Ari_var.get()
   Gilat_LastLine = Gilat_var.get()
   Hours_Column = Hours_Column_var.get()
   Names_Column = Names_Column_var.get()
   Main(fileName, Ari_LastLine, Gilat_LastLine, Hours_Column, Names_Column)

window = tk.Tk()
window.title("בס''ד")


FileName = tk.StringVar()
FileName_label = tk.Label(window, text = "File's name", font=('calibre',16, 'bold'))
FileName_label.grid(row=0,column=1)
FileName_entry = tk.Entry(window,textvariable = FileName, font=('calibre',16,'normal'))
FileName_entry.grid(row=1,column=1)

Ari_var = tk.IntVar()
Ari_label = tk.Label(window, text = "Ari's last line", font=('calibre',16, 'bold'))
Ari_label.grid(row=2,column=1)
Ari_entry = tk.Entry(window,textvariable = Ari_var, font=('calibre',16,'normal'))
Ari_entry.grid(row=3,column=1)

Hours_Column_var = tk.IntVar()
Hours_Column_label = tk.Label(window, text = "Hours column", font=('calibre',16, 'bold'))
Hours_Column_label.grid(row=2,column=2)
Hours_Column_entry = tk.Entry(window,textvariable = Hours_Column_var, font=('calibre',16,'normal'))
Hours_Column_entry.grid(row=3,column=2)

Gilat_var = tk.IntVar()
Gilat_label = tk.Label(window, text = "Gilat's last line", font=('calibre',16, 'bold'))
Gilat_label.grid(row=4,column=1)
Gilat_entry = tk.Entry(window,textvariable = Gilat_var, font=('calibre',16,'normal'))
Gilat_entry.grid(row=5,column=1)

Names_Column_var = tk.IntVar()
Names_Column_label = tk.Label(window, text = "Names column", font=('calibre',16, 'bold'))
Names_Column_label.grid(row=4,column=2)
Names_Column_entry = tk.Entry(window,textvariable = Names_Column_var, font=('calibre',16,'normal'))
Names_Column_entry.grid(row=5,column=2)

end = tk.Button(window,bg="black", fg="white",text="סיים",command=Execute)
end.grid(row=6,column=1)

window.mainloop()
