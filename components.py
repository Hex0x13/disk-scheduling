import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from displaychart import displayChart, fig, optionMenuChange
from display_array import *

example = [70, 118, 59, 110, 25, 105, 63, 100, 28, 80]
array = example.copy()

def header_section(root, outputframe, algorithm_var):
    header_frame = ctk.CTkFrame(root)

    algorithm_menu = ctk.CTkOptionMenu(header_frame, variable=algorithm_var, values=['FCFS', 'SSTF', 'Scan Disk', 'C-Scan', 'LOOK', 'C-LOOK'], height=30, width=140, font=ctk.CTkFont(size=12), dropdown_font=ctk.CTkFont(size=12))
    algorithm_menu.pack(padx=10, side=ctk.LEFT)

    outermost_label = ctk.CTkLabel(header_frame, text='outermost track:')
    outermost_label.pack(padx=(10, 5), side=ctk.LEFT)
    outermost_track_entry = ctk.CTkEntry(header_frame, textvariable=outermost_track())
    outermost_track_entry.pack(side=ctk.LEFT)


    innermost_label = ctk.CTkLabel(header_frame, text='innermost track:')
    innermost_label.pack(padx=(10, 5), side=ctk.LEFT)
    innermost_track_entry = ctk.CTkEntry(header_frame, textvariable=innermost_track())
    innermost_track_entry.pack(side=ctk.LEFT)

    startButton = ctk.CTkButton(header_frame, text='start', command=lambda: displayChart(root, outputframe, array, algorithm_var.get(), int(outermost_track().get()), int(innermost_track().get())))
    startButton.pack(side=ctk.RIGHT, padx=10)

    algorithm_var.trace('w', lambda *args: optionMenuChange(outputframe))

    return header_frame


def output_section(root):
    outputframe = ctk.CTkScrollableFrame(root)
    return outputframe


def requestlist_section(root):
    arrayframe = ctk.CTkFrame(root)

    arrayparent = ctk.CTkFrame(arrayframe, height=100, fg_color='transparent')
    arrayparent.pack(anchor=ctk.CENTER)

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

    addbutton = ctk.CTkButton(valueframe, text='add', command=lambda: addElement(root, indexentry, elementry, arrayparent, array), width=80)
    addbutton.grid(row=0, column=2, padx=5, pady=2)

    return navframe
