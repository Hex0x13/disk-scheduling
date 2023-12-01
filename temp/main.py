import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


example = [70, 118, 59, 110, 25, 105, 63, 100, 28, 80]
array = example.copy()
root = ctk.CTk()
root.geometry("1000x800")
fig, ax = None, None

header_frame = ctk.CTkFrame(root)
header_frame.pack(fill='x')
outputframe = ctk.CTkScrollableFrame(root)
outputframe.pack(expand=True, fill='both', anchor=ctk.CENTER)
arrayframe = ctk.CTkFrame(root)
arrayframe.pack(fill='x', pady=0, ipady=0)
navframe = ctk.CTkFrame(root, fg_color='transparent')
navframe.pack(pady=10)

algorithm_var = ctk.StringVar(value='Select Algorithm')
algorithm_menu = ctk.CTkOptionMenu(
    header_frame, 
    variable=algorithm_var, 
    values=['FCFS', 'SSTF', 'Scan Disk', 'C-Scan', 'LOOK', 'C-LOOK'],
    height=30, width=140,
    font=ctk.CTkFont(size=12),
    dropdown_font=ctk.CTkFont(size=12)
    )
algorithm_menu.bind("")
algorithm_menu.pack(padx=10, side=ctk.LEFT)

def optionMenuChange(*args):
    plt.close(fig)
    for child in outputframe.winfo_children():
        child.destroy()

algorithm_var.trace('w', optionMenuChange)

def validate_input(value):
    return value.isdigit() or value == '' or value == 'New Element'

def validate_index_input(value):
    return value == 'top' or value == '' or (value.isdigit() and int(value) > 0 and int(value) <= len(array))

valueframe = ctk.CTkFrame(navframe, fg_color='transparent')
valueframe.grid(row=0, column=1, sticky=ctk.NSEW)
indexentry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='top',
    validate='key',
    validatecommand=(valueframe.register(validate_index_input), '%P'),
    width=80
    )
indexentry.grid(row=0, column=0, padx=5, pady=2)

elementry = ctk.CTkEntry(
    valueframe, 
    justify='center', 
    placeholder_text='New Element',
    validate='key',
    validatecommand=(valueframe.register(validate_input), '%P'),
    width=120
    )
elementry.grid(row=0, column=1, padx=5, pady=2)

def destroy_children(widget: ctk.CTkFrame):
    children = widget.winfo_children()
    for child in children:
        child.destroy()

arrayparent = ctk.CTkFrame(arrayframe, height=100, fg_color='transparent')
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
            font=ctk.CTkFont(size=14),
            border_color='white',
            border_width=1,
            fg_color='transparent',
            width=44,
            height=44,
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
        var.trace('w', lambda *args, index=k, var=var: edit_array(args, index=index, var=var))
    
    for i in range(len(array)):
        text = ctk.CTkLabel(arrayparent, text=f'{i+1}', font=ctk.CTkFont(size=11))
        text.grid(row=2, column=i)

def addElement(indexentry, elementry, array):
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


addbutton = ctk.CTkButton(valueframe, text='add', command=addElement, width=80)
addbutton.grid(row=0, column=2, padx=5, pady=2)


def sstf_sort(disks):
    head = disks[0]
    for i in range(len(disks)):
        min = i
        for j in range(i + 1, len(disks)):
            if abs(disks[min] - head) > abs(disks[j] - head):
                min = j

        disks[i], disks[min] = disks[min], disks[i]
        head = disks[i]

def startAlgorithm():
    global fig
    global ax
    plt.close(fig)
    for child in outputframe.winfo_children():
        child.destroy()
    requests = array.copy()

    match algorithm_var.get():
        case 'FCFS':
            pass
        case 'SSTF':
            sstf_sort(requests)
        case 'Scan Disk':
            ...
        case 'C-Scan':
            ...
        case 'LOOK':
            ...
        case 'C-LOOK':
            ...
        case _ :
            CTkMessagebox(root, title="", message="Select Algorithm!")
            return

    totalOfHeadMove = 0
    for i in range(len(requests) - 1):
        totalOfHeadMove += abs(requests[i] - requests[i + 1])
    
    fig, ax = plt.subplots()

    ax.plot(requests, marker='o')
    ax.set_xlabel = "time"
    ax.set_ylabel = "Track Number"
    ax.set_title(f"The {algorithm_var.get()} Disk Scheduling")
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    canvas = FigureCanvasTkAgg(fig, master=outputframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

    total_label = ctk.CTkLabel(outputframe, text=f"The total number of head movement is {totalOfHeadMove} tracks", font=ctk.CTkFont(size=14))
    total_label.pack()

startButton = ctk.CTkButton(header_frame, text='start', command=startAlgorithm)
startButton.pack(side=ctk.RIGHT, padx=10)

display_array()


def on_closing():
    plt.close(fig)
    root.destroy()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
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
