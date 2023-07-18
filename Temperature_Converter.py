import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.minsize(width=200,height=200)
window.maxsize(700,200)

window.geometry("700x200")

masterframe = tk.Frame(master=window,relief=tk.RAISED)
masterframe.rowconfigure([0,1,2], weight=1, minsize=50)
masterframe.columnconfigure([0,1,2,3], weight=1, minsize=50)
def celciusToFahr():
    def get_Click1(event):
        txt = fld1.get()
        if txt != "":
            val = int(txt)
            fahr = round((val * 9/5)+32, 4)
            ans_lbl["text"] = str(fahr)+"°F"
    name = tk.Label(master=masterframe,text="Celcius to Fahrenheit", font=("Arial",16,"bold"))
    fld1 = tk.Entry(master=masterframe)
    tempName = tk.Label(text="°C",master=masterframe)
    ans_lbl = tk.Label(text="32.0°F",master=masterframe)
    convert_bttn = tk.Button(master=masterframe, text="->", command=lambda: get_Click1(None))
    name.grid(row=0, column=0, sticky='ew')
    fld1.grid(row=0,column=1,sticky="ew")
    tempName.grid(row=0,column=2,stick="w")
    convert_bttn.grid(row=0,column=3,padx=2, sticky="nsew")
    ans_lbl.grid(row=0,column=4,sticky="e")
    fld1.bind("<Return>",lambda event: get_Click1(event))
    
def fahrToCelcius():
    def get_Click2(event):
        txt = fld2.get()
        if txt != "":
            val = int(txt)
            cel = round((val-32)*5/9, 4)
            fin_val["text"] = str(cel)+"°C"
    fld2 = tk.Entry(master=masterframe)
    name = tk.Label(master=masterframe, text="Fahrenheit to Celcius", font=("Arial", 16, "bold"))
    tempName = tk.Label(master=masterframe, text="°F")
    btn = tk.Button(master=masterframe, text="->", command=lambda: get_Click2(None))
    fin_val = tk.Label(master=masterframe,text=f"{round(-32*(5/9),2)}°F")
    name.grid(row=1, column=0, sticky="ew")
    fld2.grid(row=1,column=1,sticky="ew")
    tempName.grid(row=1,column=2,stick="w")
    btn.grid(row=1,column=3,padx=2, sticky="nsew")
    fin_val.grid(row=1,column=4,sticky="e")
    fld2.bind("<Return>",lambda: get_Click2(None))
    
def kelvintoCelcius():
    def get_Click(event):
        txt = fld.get()
        if txt != "":
            val = int(txt)
            cel = round(val-273.15, 2)
            fin_val["text"] = str(cel)+"°C"
    
    fld = tk.Entry(master=masterframe)
    name = tk.Label(master=masterframe, text="Kelvin to Celcius", font=("Arial", 16, "bold"))
    tempName = tk.Label(master=masterframe, text="K")
    btn = tk.Button(master=masterframe, text="->", command=lambda: get_Click(None))
    fin_val = tk.Label(master=masterframe,text=f"-273.15°C")
    name.grid(row=2, column=0, sticky="ew")
    fld.grid(row=2,column=1,sticky="ew")
    tempName.grid(row=2,column=2,stick="w")
    btn.grid(row=2,column=3,padx=2, sticky="nsew")
    fin_val.grid(row=2,column=4,sticky="e")
    fld.bind("<Return>",lambda: get_Click(None))


celciusToFahr()
fahrToCelcius()
kelvintoCelcius()
masterframe.pack(expand=True,fill=tk.BOTH)


window.mainloop()
