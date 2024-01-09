import customtkinter as ctk
from CTkMessagebox import *

outermost_track_var = None
innermost_track_var = None

def validate_outermost_track(value):
    return (value.isdigit() or (value == ''))

def validate_innermost_track(value):
    return (value.isdigit() or (value == ''))

def load_dependency():
    global outermost_track_var
    global innermost_track_var

    outermost_track_var = ctk.StringVar(value='0')
    innermost_track_var = ctk.StringVar(value='199')

def innermost_track():
    global innermost_track_var
    return innermost_track_var

def outermost_track():
    global outermost_track_var
    return outermost_track_var


def destroy_children(widget: ctk.CTkFrame):
    children = widget.winfo_children()
    for child in children:
        child.destroy()

def edit_array(*args, var, index, array):
    if var.get() != '':
        array[index] = int(var.get())

def validate_array_input(value):
    global outermost_track_var
    global innermost_track_var

    min_t = int(outermost_track_var.get())
    max_t = int(innermost_track_var.get())
    return (value.isdigit() and min_t <= int(value) and max_t >= int(value)) or value == ''

def remove_element(index, arrayparent, array):
    array.pop(index)
    display_array(arrayparent, array)

def on_focus_out(event, array, index):
    if event.widget.get() == '':
        event.widget.insert(0, array[index])

def display_array(arrayparent, array):
    destroy_children(arrayparent)
    
    for k, v in enumerate(array):
        if k != 0:
            deletebutton = ctk.CTkButton(
                arrayparent, text='remove',
                width=36, height=10,
                font=ctk.CTkFont(size=8), 
                fg_color='transparent', 
                border_width=1, 
                border_color='white',
                command=lambda index=k: remove_element(index, arrayparent, array)
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
        element.bind("<FocusOut>", lambda e, array=array, k=k: on_focus_out(e, array, k))
        var.trace('w', lambda *args, index=k, var=var: edit_array(args, index=index, var=var, array=array))
    
    for i in range(len(array)):
        textval = f'{i}' if i != 0 else 'head'
        text = ctk.CTkLabel(arrayparent, text=f'{textval}', font=ctk.CTkFont(size=11))
        text.grid(row=2, column=i)


def addElement(root, indexentry, elementry, arrayparent, array):
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
            array.insert(index, int(elementry.get()))

        if indexentry.get().isdigit():
            indexentry.delete(0, ctk.END)
        elementry.delete(0, ctk.END)
        display_array(arrayparent, array)
    else:
        CTkMessagebox(root, title='', message='Please Enter a valid value')

    
