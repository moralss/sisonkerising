from tkinter import*
from tkinter import ttk
root = Tk()

def show_picture_for_bmw():
    global photo
    photo = PhotoImage(file = "images.gif")
    label = Label(root, image = photo)
    label.pack()
    
def show_picture_for_audi():
    global photo
    photo = PhotoImage(file = "2015audis8plusplacement626x382.gif")
    label = Label(root, image = photo)
    label.pack()

def show_picture_for_golf():
    global photo
    photo = PhotoImage(file = "maxresdefault.gif")
    label = Label(root, image = photo)
    label.pack()
    


def create_button_for_bmw():
    Button = ttk.Button(text = "bmw" , command = lambda:show_picture_for_bmw())
    Button.pack()

def create_button_for_audi():
    Button = ttk.Button(text = "audi" , command = lambda:show_picture_for_audi())
    Button.pack()

def create_button_for_golf():
    Button = ttk.Button(text = "golf" , command = lambda:show_picture_for_golf())
    Button.pack()
   
        

create_button_for_bmw()
create_button_for_audi()
create_button_for_golf()
root.mainloop()

