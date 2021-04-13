import tkinter as tk
import easygui
import pandas as pd
from time import strftime
import visualizer

window = tk.Tk()

window.title("Average Ebay Prices")
# window.geometry("600x600") hardcoded window size
window.resizable(width = "false", height = "false")
# resizeable will scale with linked buttons for scripts

# three frames on top of each other
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

# label header to be placed in the frame_header
header = tk.Label(frame_header, text = "RTX 3080", bg='SpringGreen4',
 fg='white', height='3', width='30', font=("Helvetica 16 bold"))
# inside the grid of frame_header, place it in the position 0,0

header.grid(row=0, column=0)

# close app
def close_app():
    window.destroy()

# run app
def run_app():
    print ('running rtx 3080 visualizer!')
    visualizer.runVisualizer()

button_run = tk.Button(bottom_frame, text="Start Script", command=run_app,
 bg='dark green', fg='white', relief='raised', width=10,
  font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=100, pady=2)


button_close = tk.Button(bottom_frame, text="Exit App", command=close_app,
 bg='dark red', fg='white', relief='raised', width=10,
  font=('Helvetica 9'))
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)



window.mainloop()