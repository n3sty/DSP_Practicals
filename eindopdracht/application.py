import tkinter as tk
import subprocess
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import SigFFT, sig
import sys

def show_plots():
    
    # Load and display the plots in the tkinter application
    fig, ax = plt.subplots()
    plt.clf()
    
    # Set the values for the plot
    window_type = "Rectangular"
    window_params = None
    frequency = 55
    
    SigFFT(sig, window_type, window_params, frequency, fig)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    # Customize the canvas
    canvas.get_tk_widget().config(bg='white', bd=2, relief='groove')

# Create the tkinter application window
root = tk.Tk()
root.geometry("800x600")  # Set the window size to 800x600
root.title("Application")

# Create a button to show the plots
show_plots_button = tk.Button(root, text="Show Plots", command=show_plots)
show_plots_button.pack(pady=10)  # Center the button vertically with padding

# Configure the button to have rounded edges
show_plots_button.config(relief="groove", bd=2, borderwidth=4, padx=20)  # Add padding to make it bigger
show_plots_button.pack()

# Start the tkinter event loop
def on_closing():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
