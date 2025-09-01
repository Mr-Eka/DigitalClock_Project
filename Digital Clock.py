#Digital clock application using Tkinter in python
from tkinter import Label, Tk  
import time 
 
# Create the main application window
app = Tk()  
app.title("🕒 Digital Clock")  
app.geometry("300x100")  
app.resizable(False, False)  
app.configure(bg="black") 
 
# Create a label to display the time
clock_label = Label(app, bg="black", fg="blue", font=("Helvetica", 40), relief='flat')  
clock_label.place(x=20, y=20) 

# Function to update the time every second
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

update_time()  
app.mainloop()
