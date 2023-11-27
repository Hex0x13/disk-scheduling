import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

array = []
root = ctk.CTk()
root.geometry("800x600")

outputframe = ctk.CTkFrame(root)
outputframe.pack(expand=True, fill='both')
arrayframe = ctk.CTkFrame(root)
arrayframe.pack(fill='x', pady=0, ipady=0)
navframe = ctk.CTkFrame(root)
navframe.pack(pady=10)

def validate_input(value):
    return value.isdigit() or value == '' or value == 'New Element'

def validate_index_input(value):
    return value == 'top' or value == '' or (value.isdigit() and int(value) > 0 and int(value) <= len(array))

valueframe = ctk.CTkFrame(navframe)
valueframe.grid(row=0, column=1)
validation = valueframe.register(validate_input)
validation2 = valueframe.register(validate_index_input)
indexentry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='top',
    validate='key',
    validatecommand=(validation2, '%P')
    )
indexentry.grid(row=0, column=0)

elementry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='New Element',
    validate='key',
    validatecommand=(validation, '%P')
    )
elementry.grid(row=0, column=1)

def destroy_children(widget: ctk.CTkFrame):
    children = widget.winfo_children()
    for child in children:
        child.destroy()

arrayparent = ctk.CTkFrame(arrayframe, height=50, fg_color='transparent')
arrayparent.pack(anchor=ctk.CENTER)

def display_array():
    global arrayparent
    global array
    destroy_children(arrayparent)
    
    for k, v in enumerate(array):
        frame = ctk.CTkFrame(arrayparent, border_color='white', border_width=1)
        frame.grid(row=0, column=k)
        text = ctk.CTkLabel(frame, text=v, fg_color='transparent', font=ctk.CTkFont(size=10))
        text.pack(pady=5, padx=20)
    
    for i in range(len(array)):
        text = ctk.CTkLabel(arrayparent, text=f'{i+1}', font=ctk.CTkFont(size=8))
        text.grid(row=1, column=i)

def addElement():
    global indexentry
    global elementry
    global array
    
    index = indexentry.get()
    if len(index) == 0:
        index = len(array)
    elif index.isdigit():
        index = int(index)
    else:
        index = -1

    if index > -1 and elementry.get().isdigit():
        if (index == len(array)):
            array.append(int(elementry.get()))
        else:
            array.insert(index - 1, int(elementry.get()))
        
        if indexentry.get().isdigit():
            indexentry.delete(0, ctk.END)
        elementry.delete(0, ctk.END)
        display_array()
    else:
        CTkMessagebox(root, title='', message='Please Enter a valid value')


addbutton = ctk.CTkButton(navframe, text='add', command=addElement)
addbutton.grid(row=0, column=2)

root.mainloop()

# root = ctk.CTk()
# root.title("Disk Scheduling")
# root.geometry("800x600")

# fig, ax = plt.subplots()
# disk_q = [70, 118, 59, 110, 25, 105, 63, 100, 28, 80]

# ax.plot(disk_q, marker='o')
# ax.set_xlabel = "Time"
# ax.set_ylabel = "Track Number"
# ax.set_title("Disk Scheduling Algorithm")
# ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# ax.set_yticks([x for x in range(0, 200, 20)], [x for x in range(0, 200, 20)])

# plot = FigureCanvasTkAgg(fig, master=root)
# plot.draw()
# plot.get_tk_widget().pack()

# root.mainloop()
