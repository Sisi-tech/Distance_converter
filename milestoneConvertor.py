import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Distance converter')
window.geometry('300x200')
window.resizable(False, False)

main = ttk.Frame(window, padding=(30, 15))
main.grid()


metres_lab = ttk.Label(main, text="Metres: ", font=('Helvatical bold', 20))
metres_input = ttk.Entry(main, width=10, font=('Helvatical bold', 16))
feet_lab = ttk.Label(main, text="Feet: ", font=('Helvatical bold', 20))
feet_display = ttk.Label(main, text="Feet shown here", font=('Helvatical bold', 16))
calc_button = ttk.Button(main, text='Calculate')

window.columnconfigure((0, 1), weight=1)
window.rowconfigure((0, 1, 1), weight=1)

metres_lab.grid(row=0, column=0, padx=2, pady=2, sticky='sw')
metres_input.grid(row=0, column=1, padx=2, pady=2,)
feet_lab.grid(row=1, column=0, padx=2, pady=2, sticky='sw')
feet_display.grid(row=1, column=0, padx=2, pady=2)
feet_display.grid(row=1, column=1, padx=2, pady=2)
calc_button.grid(row=2, column=0, columnspan=2)


window.mainloop()