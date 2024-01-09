import customtkinter as ctk
from CTkMessagebox import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

fig, ax = None, None


def isort(arr: list, start: int, stop: int, reverse=False):
    for i in range(start + 1, stop):
        key = arr[i]
        j = i - 1

        while j >= start and ((reverse and key > arr[j]) or (not reverse and key < arr[j])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def sstf_sort(disks: list):
    head = disks[0]
    for i in range(len(disks)):
        min = i
        for j in range(i + 1, len(disks)):
            if abs(disks[min] - head) > abs(disks[j] - head):
                min = j

        disks[i], disks[min] = disks[min], disks[i]
        head = disks[i]


def scan_disk(disks: list):
    pivot = disks[0]
    i = 0
    for j in range(1, len(disks)):
        if disks[j] >= pivot:
            i += 1
            disks[i], disks[j] = disks[j], disks[i]

    isort(disks, 0, i + 1)
    isort(disks, i + 1, len(disks), reverse=True)


def c_scan_disk(disks: list):
    pivot = disks[0]
    i = 0
    for j in range(1, len(disks)):
        if disks[j] >= pivot:
            i += 1
            disks[i], disks[j] = disks[j], disks[i]

    isort(disks, 0, i + 1)
    isort(disks, i + 1, len(disks))


def destroy_chart(outputframe):
    global fig
    plt.close(fig)
    for child in outputframe.winfo_children():
        child.destroy()


def display_chart(root, outputframe, array, algorithm, outermost_track, innermost_track):
    global fig
    global ax

    if innermost_track <= outermost_track:
        CTkMessagebox(root, title="", message="Please make sure outermost track is lesser than innermost")

    if not isinstance(array[0], int):
        CTkMessagebox(root, title="", message="Please enter head")
        return

    destroy_chart(outputframe)
    requests = array.copy()

    match algorithm:
        case 'FCFS':
            pass
        case 'SSTF':
            sstf_sort(requests)
        case 'Scan Disk':
            requests.append(innermost_track)
            scan_disk(requests)
        case 'C-Scan':
            requests.append(innermost_track)
            requests.append(outermost_track)
            c_scan_disk(requests)
        case 'LOOK':
            scan_disk(requests)
        case 'C-LOOK':
            c_scan_disk(requests)
        case _:
            CTkMessagebox(root, title="", message="Select Algorithm!")
            return

    totalOfHeadMove = 0
    for i in range(len(requests) - 1):
        totalOfHeadMove += abs(requests[i] - requests[i + 1])

    fig, ax = plt.subplots()

    ax.plot(requests, marker='o')
    ax.set_xlabel = "time"
    ax.set_ylabel = "Track Number"
    ax.set_title(f"The {algorithm} Disk Scheduling")
    ax.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
    yticks = np.arange(outermost_track, innermost_track + 1,(innermost_track + 1) // len(requests))
    ax.set_yticks(yticks)

    canvas = FigureCanvasTkAgg(fig, master=outputframe)
    canvas.draw()
    canvas.get_tk_widget().configure(width=800, height=600)
    canvas.get_tk_widget().pack(pady=(40, 5))

    total_label = ctk.CTkLabel(outputframe, text=f"The total number of head movement is {totalOfHeadMove} tracks", font=ctk.CTkFont(size=16))
    total_label.pack()


def optionMenuChange(outputframe):
    plt.close(fig)
    for child in outputframe.winfo_children():
        child.destroy()
