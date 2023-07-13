import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.minsize(width=80,height=80)

window.geometry("500x100")

masterframe = tk.Frame(master=window,relief=tk.RAISED)
masterframe.rowconfigure([0,1], weight=1, minsize=50)
masterframe.columnconfigure([0,1,2,3], weight=1, minsize=50)
def celciusToFahr():
    def get_Click1(event):
        txt = fld1.get()
        if txt != "":
            val = int(txt)
            fahr = (val * 9/5)+32
            ans_lbl["text"] = str(fahr)+"°F"
    fld1 = tk.Entry(master=masterframe)
    tempName = tk.Label(text="°C",master=masterframe)
    ans_lbl = tk.Label(text="32.0°F",master=masterframe)
    convert_bttn = tk.Button(master=masterframe, text="->", command=lambda: get_Click1(None))
    fld1.grid(row=0,column=0,sticky="ew")
    tempName.grid(row=0,column=1,stick="w")
    convert_bttn.grid(row=0,column=2,padx=5, sticky="nesw")
    ans_lbl.grid(row=0,column=3,sticky="e")
    fld1.bind("<Return>",lambda event: get_Click1(event))
    
def fahrToCelcius():
    def get_Click2(event):
        txt = fld2.get()
        if txt != "":
            val = int(txt)
            cel = (val-32)*5/9
            fin_val["text"] = str(cel)
    pass
    fld2 = tk.Entry(master=masterframe)
    tempName = tk.Label(master=masterframe, text="°F")
    btn = tk.Button(master=masterframe, text="->", command=lambda event: get_Click2(event))
    fin_val = tk.Label(master=masterframe,text=f"{-32*(5/9)}")
    fld2.grid(row=1,column=0,sticky="ew")
    tempName.grid(row=1,column=1,stick="w")
    btn.grid(row=1,column=2,padx=5, sticky="nesw")
    fin_val.grid(row=1,column=3,sticky="e")
    fld2.bind("<Return>",lambda event: get_Click2(event))
    


celciusToFahr()
fahrToCelcius()

masterframe.pack(expand=True,fill=tk.BOTH)


window.mainloop()
