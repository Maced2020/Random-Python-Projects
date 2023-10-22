# this will be turned into a password generator 
# all i need to do is combine this and the password generator app I made


import tkinter as tk
import random
import sys



#this creates the window and the buttons.
def create_ui_window():
    window = tk.Tk()
    window.title("Password generator")
    window.geometry('800x600')

# this is the main window getting created
    main_window = tk.Label(window, text="Password Generator!")
    main_window.pack()

    popup_button = tk.Button(window, text="open Popup", command=popup_window)
    popup_button.pack(pady=20)

#this is the end of the popup window


#this is creating the click me button
    click_me_button = tk.Button(window, text="Click Me", command=lambda: print("Ouch!"))
    click_me_button.pack()
    window.mainloop()



# creating a Pop up window 

def popup_window():
    popup = tk.Tk()
    popup.title("Popup Window")
    
    # Add widgets to the popup window
    label = tk.Label(popup, text="This is a pop-up window.")
    label.pack(padx=20, pady=20)
    
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Start the Tkinter main loop
    popup.mainloop()


create_ui_window()