from glob import glob
import random
import tkinter as tk
from tkinter.font import NORMAL

def deleteText():
    textLabel.destroy()
    generate_button['state'] = tk.NORMAL
    delete_button['state'] = tk.DISABLED

def showText():
    global textLabel
    orig = ["VTCT", "VTCH", "VTCC", "VTCN", "VTCL", "VTCP", "VTUL", "VTUD", "VTUI", "VTUW", "VTUU", "VTUO", "VTUK", "VTPP", "VTBD", "VTBS", "VTBU", "VTSE", "VTSR", "VTSM", "VTSB", "VTSF", "VTSG", "VTSP", "VTST", "VTSS", "VTSC"]
    dest = ["VTCT", "VTCH", "VTCC", "VTCN", "VTCL", "VTCP", "VTUL", "VTUD", "VTUI", "VTUW", "VTUU", "VTUO", "VTUK", "VTPP", "VTBD", "VTBS", "VTBU", "VTSE", "VTSR", "VTSM", "VTSB", "VTSF", "VTSG", "VTSP", "VTST", "VTSS", "VTSC"]
    while True:
        indexOrigin = random.randint(0, len(orig) - 1)
        indexDest = random.randint(0, len(dest) - 1)
        if orig[indexOrigin] != dest[indexDest]:
            break
        
    txtstr = "Today route is: " + orig[indexOrigin] + "-" + dest[indexDest] + "."
    textLabel = tk.Label(app, text=txtstr)
    textLabel.pack(pady=10)
    generate_button['state'] = tk.DISABLED
    delete_button['state'] = tk.NORMAL

app = tk.Tk()
s_width = app.winfo_screenwidth() // 10
s_height = app.winfo_screenheight() // 10
app.title("Route Generator")
app.geometry("%dx%d" % (s_width, s_height))
app.resizable(False, False)

generate_button = tk.Button(app, text='Genarate', command=showText)
generate_button.pack()
delete_button = tk.Button(app, text='Delete', command=deleteText)
delete_button.pack(pady=10)
delete_button['state'] = tk.DISABLED

app.mainloop()