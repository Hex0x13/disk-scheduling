import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = ctk.CTk()
root.title("Disk Scheduling")
root.geometry("800x600")

fig, ax = plt.subplots()
disk_q = [70, 118, 59, 110, 25, 105, 63, 100, 28, 80]

ax.plot(disk_q, marker='o')
ax.set_xlabel = "Time"
ax.set_ylabel = "Track Number"
ax.set_title("Disk Scheduling Algorithm")
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_yticks([x for x in range(0, 200, 20)], [x for x in range(0, 200, 20)])

plot = FigureCanvasTkAgg(fig, master=root)
plot.draw()
plot.get_tk_widget().pack()

root.mainloop()
