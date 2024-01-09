import customtkinter as ctk
from CTkMessagebox import *
from displaychart import display_chart, optionMenuChange, destroy_chart
from display_array import *


sample_array = (70, 118, 59, 110, 25, 105, 63, 100, 28, 80)
array = ['']


def clear_array(arrayparent, outputframe):
    global array
    array = ['']
    display_array(arrayparent, array)
    destroy_chart(outputframe)


def generate_sample(arrayparent, outputframe):
    global array

    outermost_track().set('0')
    innermost_track().set('199')
    array = [*sample_array]
    display_array(arrayparent, array)
    destroy_chart(outputframe)


def header_section(root, outputframe, algorithm_var, arrayparent):
    header_frame = ctk.CTkFrame(root, fg_color='#444')

    algorithm_menu = ctk.CTkOptionMenu(header_frame, variable=algorithm_var, values=['FCFS', 'SSTF', 'Scan Disk', 'C-Scan', 'LOOK', 'C-LOOK'], height=30, width=140, font=ctk.CTkFont(size=12), dropdown_font=ctk.CTkFont(size=12))
    algorithm_menu.pack(padx=10, side=ctk.LEFT)

    outermost_label = ctk.CTkLabel(header_frame, text='Outermost Track:', font=ctk.CTkFont(size=14))
    outermost_label.pack(padx=(10, 5), side=ctk.LEFT)
    outermost_track_entry = ctk.CTkEntry(header_frame, textvariable=outermost_track(), width=50)
    outermost_track_entry.configure(validate='key', validatecommand=(header_frame.register(validate_outermost_track), '%P'))
    outermost_track_entry.pack(side=ctk.LEFT)
    outermost_track().trace('w', lambda *args: clear_array(arrayparent, outputframe))

    innermost_label = ctk.CTkLabel(header_frame, text='Innermost Track:', font=ctk.CTkFont(size=14))
    innermost_label.pack(padx=(10, 5), side=ctk.LEFT)
    innermost_track_entry = ctk.CTkEntry(header_frame, textvariable=innermost_track(), width=50)
    innermost_track_entry.configure(validate='key', validatecommand=(header_frame.register(validate_innermost_track), '%P'))
    innermost_track_entry.pack(side=ctk.LEFT)
    innermost_track().trace('w', lambda *args: clear_array(arrayparent, outputframe))

    generate_sample_btn = ctk.CTkButton(header_frame, text='Sample Array', fg_color='transparent', border_color='white', border_width=1)
    generate_sample_btn.configure(command=lambda: generate_sample(arrayparent, outputframe))
    generate_sample_btn.pack(side=ctk.RIGHT, padx=10)

    destroy_array_btn = ctk.CTkButton(header_frame, text='Clear Request', fg_color='transparent', border_color='white', border_width=1)
    destroy_array_btn.configure(command=lambda: clear_array(arrayparent, outputframe))
    destroy_array_btn.pack(side=ctk.RIGHT, padx=10)

    def start():
        if not outermost_track().get().isdigit():
            CTkMessagebox(root, title='', message='Please fill outermost track!')
            return
        
        if not innermost_track().get().isdigit():
            CTkMessagebox(root, title='', message='Please fill innermost track!')
            return

        display_chart(root, outputframe, array, algorithm_var.get(), int(outermost_track().get()), int(innermost_track().get()))

    startButton = ctk.CTkButton(header_frame, text='Start', command=start, fg_color='transparent', border_color='white', border_width=1)
    startButton.pack(side=ctk.RIGHT, padx=10)

    algorithm_var.trace('w', lambda *args: optionMenuChange(outputframe))

    return header_frame


def output_section(root):
    outputframe = ctk.CTkScrollableFrame(root)
    return outputframe


def requestlist_section(root):
    arrayframe = ctk.CTkFrame(root)

    arrayparent = ctk.CTkFrame(arrayframe, fg_color='transparent')
    arrayparent.pack(anchor=ctk.CENTER, pady=(5, 0))

    return arrayframe, arrayparent


def nav_section(root, arrayparent):
    navframe = ctk.CTkFrame(root, fg_color='transparent')
    valueframe = ctk.CTkFrame(navframe, fg_color='transparent')
    valueframe.grid(row=0, column=1, sticky=ctk.NSEW)

    def validate_input(value):
        max_t = int(innermost_track().get())
        min_t = int(outermost_track().get())
        return (value.isdigit() and int(value) >= min_t and int(value) <= max_t)\
            or value == '' or value == 'New Element'

    def validate_index_input(value):
        return value == 'top' or value == '' or (value.isdigit() and int(value) > 0 and int(value) <= len(array))

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

    addbutton = ctk.CTkButton(valueframe, text='add', command=lambda: addElement(
        root, indexentry, elementry, arrayparent, array), width=80)
    addbutton.grid(row=0, column=2, padx=5, pady=2)

    return navframe
