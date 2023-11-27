import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

array = []
root = ctk.CTk()
root.geometry("800x600")

headerframe = ctk.CTkFrame(root)
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
indexentry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='top',
    validate='key',
    validatecommand=(valueframe.register(validate_index_input), '%P')
    )
indexentry.grid(row=0, column=0)

elementry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='New Element',
    validate='key',
    validatecommand=(valueframe.register(validate_input), '%P')
    )
elementry.grid(row=0, column=1)

def destroy_children(widget: ctk.CTkFrame):
    children = widget.winfo_children()
    for child in children:
        child.destroy()

arrayparent = ctk.CTkFrame(arrayframe, height=80, fg_color='transparent')
arrayparent.pack(anchor=ctk.CENTER)

def validate_array_input(value):
    return value.isdigit() or value == ''

def edit_array(*args, var, index):
    global array
    if var.get() != '':
        array[index] = int(var.get())

def remove_element(index):
    global array
    array.pop(index)
    display_array()

def display_array():
    global arrayparent
    global array
    destroy_children(arrayparent)
    
    for k, v in enumerate(array):
        deletebutton = ctk.CTkButton(
            arrayparent, text='remove',
            width=36, height=10, 
            font=ctk.CTkFont(size=8), 
            fg_color='transparent', 
            border_width=1, 
            border_color='white',
            command=lambda index=k: remove_element(index)
        )
        deletebutton.grid(row=0, column=k, ipady=0, pady=5)

        var = ctk.StringVar()
        element = ctk.CTkEntry(
            arrayparent,
            textvariable=var,
            font=ctk.CTkFont(size=12),
            border_color='white',
            border_width=1,
            fg_color='transparent',
            width=40,
            height=40,
            justify='center',
            validate='key',
            validatecommand=(arrayparent.register(validate_array_input), '%P')
        )
        element.insert(0, v)
        element.grid(row=1, column=k)
        def on_focus_out(event):
            if element.get() == '':
                element.insert(0, array[k])
        element.bind("<FocusOut>", on_focus_out)
        var.trace('w', lambda *args, index=k, var=var, elem=element, val=v: edit_array(args, index=index, var=var))
        # deletebutton = ctk.CTkButton(arrayparent, text='remove', font=ctk.CTkFont(size=10), height=12, width=36)
        # deletebutton.grid(row=0, column=k)

        # editbutton = ctk.CTkButton(arrayparent, text='edit', font=ctk.CTkFont(size=10), height=12, width=36)
        # editbutton.grid(row=1, column=k)

        # frame = ctk.CTkFrame(arrayparent, border_color='white', border_width=1, width=40, height=40)
        # frame.grid(row=2, column=k)
        # text = ctk.CTkLabel(frame, text=v, fg_color='transparent', font=ctk.CTkFont(size=12))
        # text.pack(pady=5, padx=20)
    
    for i in range(len(array)):
        text = ctk.CTkLabel(arrayparent, text=f'{i+1}', font=ctk.CTkFont(size=10))
        text.grid(row=2, column=i)

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
