import customtkinter as ctk
import matplotlib.pyplot as plt
from displaychart import display_chart, fig
from components import *
from display_array import *

root = ctk.CTk()
root.geometry("1000x800")
load_dependency()
algorithm_var = ctk.StringVar(value='Select Algorithm')

outputframe = output_section(root)
arrayframe, arrayparent = requestlist_section(root)
header_frame = header_section(root, outputframe, algorithm_var, arrayparent)
navframe = nav_section(root, arrayparent)


header_frame.pack(fill='x', ipady=10, ipadx=10)
outputframe.pack(expand=True, fill='both', anchor=ctk.CENTER)
arrayframe.pack(fill='x', pady=0, ipady=0)
navframe.pack(pady=10)

display_array(arrayparent, array)


def on_closing():
    plt.close(fig)
    root.destroy()
    root.quit()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
